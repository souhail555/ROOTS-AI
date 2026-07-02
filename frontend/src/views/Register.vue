<template>
  <div>
    <h2>Register</h2>

    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />

    <button @click="register">Register</button>

    <p>{{ message }}</p>
  </div>
</template>

<script>
import api from "../api/axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      message: "",
    };
  },

  methods: {
    async register() {
      try {
        await api.post("register/", {
          username: this.username,
          password: this.password,
          role: "participant",
        });

        this.message = "User created successfully";
      } catch (err) {
        this.message = "Error creating user";
      }
    },
  },
};
</script>
