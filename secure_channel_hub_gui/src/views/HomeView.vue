<template>
  <div class="vh-100 gradient-custom">
    <SignUpView v-if="authStep === 0" @changeStep="changeStep" />
    <LoginView v-else-if="authStep === 1" @changeStep="changeStep" />
  </div>
</template>

<script setup>
import LoginView from "@/components/LoginView.vue";
import SignUpView from "@/components/SignUpView.vue";
import { ref } from "vue";

const authStep = ref(1);
const changeStep = (e) => {
  authStep.value = e;
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.gradient-custom {
  /* fallback for old browsers */
  background: #6a11cb;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );
}
.form-input::placeholder {
  color: white;
  opacity: 1; /* Firefox */
}
.cursor-pointer {
  cursor: pointer;
}
</style>
