<div align="center">
  <img src="https://media.giphy.com/media/MfnJATkfrAIBG/giphy.gif" width="100"/>
  
</div>

<h1><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>Secure Channels Hub</h1>

This is a full-stack project built with Vue.js and Django Rest Framework. The project implements web sockets using Django Channels for real-time communication. The backend provides JWT authentication and RESTful APIs for user authentication (login, register, logout). Redis is used as a backing storage for caching and session management.

## Architecture

The project follows a client-server architecture, with the frontend built using Vue.js and the backend developed with Django Rest Framework. Communication between the client and server is established using WebSockets via Django Channels. Redis serves as the backing storage for managing WebSocket connections and caching data.

## Features

- JWT authentication for secure user login and registration
- RESTful APIs for user authentication
- Web socket implementation using Django Channels
- Real-time communication between clients
- Automatic connection management and heartbeat functionality to ensure active connections
- Custom middleware for authentication and request processing
- Redis for caching and session management
- Responsive Design


## Technologies used

<div style="display:flex">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
  <img src="https://img.shields.io/badge/Python-1572B6?style=for-the-badge&logo=python&logoColor=F7DF1E" />
  <img src="https://img.shields.io/badge/Django-323330?style=for-the-badge&logo=django&logoColor=F7DF1E" />
  <img src="https://img.shields.io/badge/Redis-white?style=for-the-badge&logo=redis&logoColor=red" />
  <img src="https://img.shields.io/badge/Pinia-orange?style=for-the-badge&logo=pinia&logoColor=red" />
  <img src="https://img.shields.io/badge/Pinia_Persistent-yellow?style=for-the-badge&logo=pinia&logoColor=red&color=orange" />
  <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />  
  <img src="https://img.shields.io/badge/Django_Channels-blue?style=for-the-badge&logo=django&logoColor=yellow&color=blue" />
  <img src="https://img.shields.io/badge/Bootstrap-blue?style=for-the-badge&logo=bootstrap&logoColor=white&color=purple" />
   <img src="https://img.shields.io/badge/Font_Awesome-purple?style=for-the-badge&logo=fontawesome&logoColor=white&color=2321b0" />
  
</div>

<h2><img  width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0115.gif" border="0" alt="animated-television-image-0115" />
  Screenshots</h2>

![image](https://github.com/Abdul-Mueed-Shahbaz/Secure_Channels-Hub/assets/52679916/3a889a29-4a23-4304-89a9-01388d739472)
![image](https://github.com/Abdul-Mueed-Shahbaz/Secure_Channels-Hub/assets/52679916/da1ff96b-4fe9-45e1-b724-82650213a0a3)
![image](https://github.com/Abdul-Mueed-Shahbaz/Secure_Channels-Hub/assets/52679916/274d839b-2526-42f2-af70-f6ed0d5a5a9a)
![image](https://github.com/Abdul-Mueed-Shahbaz/Secure_Channels-Hub/assets/52679916/ef942bc8-24db-4784-9412-616f03cd37f1)
![image](https://github.com/Abdul-Mueed-Shahbaz/Secure_Channels-Hub/assets/52679916/6a2ca107-3d77-4c04-b07e-4a4501731ccc)
![image](https://github.com/Abdul-Mueed-Shahbaz/Secure_Channels-Hub/assets/52679916/3a2f8cb9-6d77-468e-8637-3852982165b3)


## Additional Notes

- For more information about Redis, visit the [Redis official website](https://redis.io/).
- Learn more about Pinia, the state management library, [here](https://pinia.esm.dev/).
- The threading implementation is used to start a coroutine that sends a ping message to the client and waits for a pong response. If the client does not respond within a specified timeout, it is disconnected to ensure connection reliability.

<h2><img width="30px" src="https://www.animatedimages.org/data/media/318/animated-computer-smiley-image-0080.gif" border="0" alt="animated-computer-smiley-image-0080" />  Setup:</h2>

- Prerequisites

1. Docker: Install Docker from the official website ([https://www.docker.com/](https://www.docker.com/)) and set up the Redis server.



- Backend Setup

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the backend directory: `cd secure_channel_hub_api`
3. Install dependencies: `pip install -r requirements/base.txt`
4. Apply database migrations: `python manage.py migrate`
5. Start the Django development server: `python manage.py runserver`
6. Set the Redis server configuration in `base.py` or your preferred configuration file.
7. Start the Redis server using Docker: `docker run -p 6379:6379 -d redis`

- Frontend Setup

1. Navigate to the frontend directory: `cd secure_channels_hub_gui`
2. Install dependencies: `npm install`
3. Start the development server: `npm run serve`

## Usage

1. Access the application at [http://localhost:8080](http://localhost:8080)
2. Register a new user or login with an existing account
3. After logging in, you will be redirected to the home page
4. Enter a room name to connect to
5. Start sending messages and see real-time updates from other connected clients


## Contributors

- [Abdul Mueed Shahbaz]([https://github.com/your-username](https://github.com/Abdul-Mueed-Shahbaz))

## License

This project is licensed under the [MIT License](LICENSE).

