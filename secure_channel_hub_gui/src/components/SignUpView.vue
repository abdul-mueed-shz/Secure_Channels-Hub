<template>
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-7">
        <div class="card bg-dark text-white" style="border-radius: 1rem">
          <div class="card-body p-5 text-center">
            <form
              @submit.prevent="create(signUpForm)"
              class="mb-md-5 mt-md-4 pb-5"
            >
              <h2 class="font-weight-bold mb-2 text-uppercase">Sign Up</h2>
              <p class="text-white-50 mb-5">
                Please enter your login and password!
              </p>

              <div class="form-outline form-white mb-4">
                <input
                  type="text"
                  id="typeUsernameX"
                  class="form-control form-control-lg bg-dark text-light form-input"
                  placeholder="Username"
                  v-model="signUpForm.username"
                />
              </div>
              <div class="form-outline form-white mb-4">
                <input
                  type="email"
                  id="typeEmailX"
                  class="form-control form-control-lg bg-dark text-light form-input"
                  placeholder="Email"
                  v-model="signUpForm.email"
                />
              </div>

              <div class="form-outline form-white mb-4">
                <input
                  type="password"
                  id="typePasswordX"
                  class="form-control form-control-lg bg-dark text-light form-input"
                  placeholder="Password"
                  v-model="signUpForm.password"
                />
              </div>
              <div class="form-outline form-white mb-4">
                <input
                  type="password"
                  id="typePassword2X"
                  class="form-control form-control-lg bg-dark text-light form-input"
                  placeholder="Confirm Password"
                  v-model="signUpForm.password2"
                />
              </div>

              <p class="small mb-5 pb-lg-2">
                <a class="text-white-50" href="#!">Forgot password?</a>
              </p>

              <button class="btn btn-outline-light btn-lg px-5" type="submit">
                Sign Up
              </button>

              <div class="d-flex justify-content-center text-center mt-4 pt-1">
                <a href="#!" class="text-white"
                  ><i class="fab fa-facebook-f fa-lg"></i
                ></a>
                <a href="#!" class="text-white"
                  ><i class="fab fa-twitter fa-lg mx-4 px-2"></i
                ></a>
                <a href="#!" class="text-white"
                  ><i class="fab fa-google fa-lg"></i
                ></a>
              </div>

              <div class="pt-4N">
                <div
                  class="text-white-50 font-weight-bold cursor-pointer"
                  @click="$emit('changeStep', 1)"
                >
                  Log In
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import fetchApi from "@/common/fetch";
import useAuthStore from "@/stores/auth/authStore";

// eslint-disable-next-line
const emit = defineEmits(["changeStep"]);
const store = useAuthStore();

console.log(store);
const signUpForm = ref({
  email: null,
  username: null,
  password: null,
  password2: null,
});

const create = async () => {
  if (
    signUpForm.value &&
    Object.values(signUpForm.value).every((val) => !!val)
  ) {
    try {
      await fetchApi({
        endpoint: "register/",
        body: signUpForm.value,
      });
      emit("changeStep", 1);
    } catch (err) {
      console.error(err);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
