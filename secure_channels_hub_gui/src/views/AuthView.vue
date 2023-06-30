<template>
  <div class="vh-100">
    <!-- <div
      class="text-white h6 d-flex justify-content-center align-items-center fixed-top"
    >
      <div
        class="bg-success p-3 mt-3 notif-anim"
        style="max-width: 30rem; border-radius: 12px"
      >
        Successfully created
      </div>
    </div> -->
    <SignUpView v-if="authStep === 0" @changeStep="changeStep" />
    <LoginView v-else-if="authStep === 1" @changeStep="changeStep" />
  </div>
</template>

<script setup>
import { ROUTE_CONSTANTS } from "@/common/constants/routes";
import LoginView from "@/components/LoginView.vue";
import SignUpView from "@/components/SignUpView.vue";
import { useAuthStore } from "@/stores/auth/authStore";
import { storeToRefs } from "pinia";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const store = useAuthStore();
const router = useRouter();

const authStep = ref(1);
const { auth } = storeToRefs(store);

onMounted(() => {
  if (Object.keys(auth.value).length) {
    router.push(ROUTE_CONSTANTS.HOME.PATH);
  }
});

const changeStep = (e) => {
  authStep.value = e;
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.notif-anim {
  animation: fadeIn 1.5s;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  25% {
    opacity: 0.5;
  }
  50% {
    opacity: 1;
  }
}

.form-input::placeholder {
  color: white;
  opacity: 1; /* Firefox */
}
.cursor-pointer {
  cursor: pointer;
}
</style>
