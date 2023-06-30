<template>
  <section
    class="vh-100 d-flex flex-column justify-content-center align-items-center w-100"
  >
    <!-- class="col-12 col-md-8 col-lg-6 col-xl-5" -->

    <div
      class="cursor-pointer d-flex h6 text-white font-weight-bold justify-content-end pr-3 pt-2 fixed-top"
      @click="logout"
    >
      <i class="pr-1 fas fa-sign-out-alt fa-lg"></i>
      Logout
    </div>
    <div class="container">
      <div class="row">
        <div class="col-9">
          <div class="pt-4">
            <div class="pb-3 h2 font-weight-bold username">
              {{ auth.user?.username }}
            </div>
            <div class="form-outline form-white mb-4">
              <input
                type="message"
                id="typeRoomL"
                class="form-control form-control-lg bg-dark text-light form-input"
                placeholder="Enter Room Name"
              />
            </div>
          </div>
          <div class="w-100 d-flex justify-content-center">
            <textarea class="w-100" id="chat-log" readonly></textarea><br />
          </div>
          <div class="pt-4">
            <div class="form-outline form-white mb-4">
              <input
                type="message"
                id="typeMessageL"
                class="form-control form-control-lg bg-dark text-light form-input"
                placeholder="Send Message"
              />
            </div>
          </div>
        </div>
        <div class="col-3 pt-5">
          <div
            class="h-100 card bg-dark text-white"
            style="border-radius: 1rem"
          >
            <div class="card-body p-5 text-center">
              <div class="font-weight-bold h5">Rooms</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ROUTE_CONSTANTS } from "@/common/constants/routes";
import { useAuthStore } from "@/stores/auth/authStore";
import { storeToRefs } from "pinia";
import {
  onMounted,
  // ref
} from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useAuthStore();
const { auth } = storeToRefs(store);
const { setAuthDetails } = store;

// let webSocket = ref(null);

const logout = () => {
  setAuthDetails({});
  router.push(ROUTE_CONSTANTS.AUTH.PATH);
};
onMounted(() => {
  if (!Object.keys(auth.value).length) {
    router.push({ path: ROUTE_CONSTANTS.AUTH.PATH });
  }
  // webSocket.value = new WebSocket("ws://127.0.0.1:8000/ws/chat/testroom/");
});
</script>

<style lang="scss" scoped>
.username {
  color: rgb(146, 146, 146);
}
#chat-log {
  background-color: rgb(56, 60, 68);
  color: white;
  border-radius: 1rem;
  padding: 1rem;
  border: none;
  height: 50dvh;
  resize: none;
}
#chat-log:focus {
  outline: none;
}
.rounded-borders_none {
  border: none;
  border-radius: 2rem;
}
#typeMessageL {
  @extend .rounded-borders_none;
}
#typeRoomL {
  @extend .rounded-borders_none;
}
</style>
