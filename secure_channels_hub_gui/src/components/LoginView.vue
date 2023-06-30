<template>
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-7">
        <div class="card bg-dark text-white" style="border-radius: 1rem">
          <div class="card-body p-5 text-center">
            <form @submit.prevent="login" class="mb-md-5 mt-md-4 pb-5">
              <h2 class="font-weight-bold mb-2 text-uppercase">Login</h2>
              <p class="text-white-50 mb-5">
                Please enter your login and password!
              </p>

              <div class="form-outline form-white mb-4">
                <input
                  type="username"
                  id="typeUsernameL"
                  class="form-control form-control-lg bg-dark text-light form-input"
                  placeholder="Username"
                  v-model="loginForm.username"
                />
              </div>

              <div class="form-outline form-white mb-4">
                <input
                  type="password"
                  id="typePasswordL"
                  class="form-control form-control-lg bg-dark text-light form-input"
                  placeholder="Password"
                  v-model="loginForm.password"
                />
              </div>

              <p class="small mb-5 pb-lg-2">
                <a class="text-white-50" href="#!">Forgot password?</a>
              </p>

              <button class="btn btn-outline-light btn-lg px-5" type="submit">
                Login
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
            </form>

            <div class="mb-0">
              Don't have an account?
              <div
                class="text-white-50 fw-bold cursor-pointer"
                @click="$emit('changeStep', 0)"
              >
                Sign Up
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import fetchApi from "@/common/fetch";
import { useAuthStore } from "@/stores/auth/authStore";
import { useRouter } from "vue-router";
import { ROUTE_CONSTANTS } from "@/common/constants/routes";

const router = useRouter();
const store = useAuthStore();

const { setAuthDetails } = store;

const loginForm = ref({
  username: null,
  password: null,
});
const login = async () => {
  if (loginForm.value && Object.values(loginForm.value).every((val) => !!val)) {
    fetchApi({
      endpoint: "login/",
      body: loginForm.value,
    })
      .then((res) => res.json())
      .then((res) => {
        delete res.message;
        setAuthDetails(res);
        router.push(ROUTE_CONSTANTS.HOME.PATH);
      })
      .catch((err) => {
        console.error(err);
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
