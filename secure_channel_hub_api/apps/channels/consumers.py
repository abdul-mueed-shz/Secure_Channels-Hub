import asyncio
import json
import threading
import time

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class ChatConsumer(AsyncWebsocketConsumer):
    clients = {}
    room_name = None
    room_group_name = None
    routine_thread = None

    async def send_ping(self, channel_name):
        await self.channel_layer.send(channel_name, {
            "type": "chat_message",
            "message": json.dumps({"type": "heartbeat", "message": 'ping'})})

    def start_routine(self):
        async def routine():
            while len(self.clients) > 0:
                disconnected_clients = []
                try:
                    for key, client_info in self.clients.items():
                        try:
                            client = self.clients[client_info.get('client').channel_name]
                            client['connected'] = False
                            await self.send_ping(client_info.get('client').channel_name)
                            await asyncio.sleep(5)
                            if not client['connected']:
                                disconnected_clients.append(
                                    client_info
                                )
                        except asyncio.TimeoutError:
                            disconnected_clients.append(
                                client_info
                            )
                    for client_info in disconnected_clients:
                        await client_info.get('client').disconnect('heartbeat')
                    disconnected_clients.clear()
                except RuntimeError:
                    continue
                await asyncio.sleep(10)

            self.routine_thread = None

        thread = threading.Thread(target=asyncio.run, args=(routine(),))
        thread.start()
        return thread

    def stop_routine(self, thread):
        thread.join()

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.clients[self.channel_name] = {
            'client': self,
            'connected': True,
            'room': self.room_group_name
        }
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        if len(self.clients) == 1:
            self.routine_thread = self.start_routine()

    async def disconnect(self, close_code):
        await self.discard_and_disconnect(self.room_group_name, self.channel_name)

    async def discard_and_disconnect(self, room, channel_name):
        await self.channel_layer.group_discard(room, channel_name)
        if self.clients.get(self.channel_name):
            del self.clients[self.channel_name]

    async def receive(self, text_data):
        text_data_dict = json.loads(text_data)
        message = text_data_dict["message"]
        if text_data_dict.get('type') and text_data_dict.get('type') == 'heartbeat':
            client = self.clients[self.channel_name]
            client['connected'] = True
            return
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "chat_message", "message": json.dumps({"message": self.scope['user'].username + ': ' + message})}
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send(message)
