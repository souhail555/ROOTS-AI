<template>
  <div>
    <h2>Login</h2>

    <input v-model="username" placeholder="username" />
    <input v-model="password" type="password" placeholder="password" />

    <button @click="login">Login</button>

    <p>
      No account?
      <router-link to="/register">Register</router-link>
    </p>
  </div>
</template>

<script>
import api from "../api/axios";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },

  methods: {
    async login() {
      const res = await api.post("token/", {
        username: this.username,
        password: this.password,
      });

      localStorage.setItem("token", res.data.access);

      this.$router.push("/dashboard");
    },
  },
};
</script>
