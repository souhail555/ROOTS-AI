<template>
  <div class="p-6">

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
import axios from "axios"

export default {
  data() {
    return {
      username: "",
      password: ""
    }
  },

  methods: {

    async login() {

      try {

        const res = await axios.post(
          "http://127.0.0.1:8000/api/token/",
          {
            username: this.username,
            password: this.password
          }
        )

        console.log("LOGIN SUCCESS:", res.data)

        // save token
        localStorage.setItem("token", res.data.access)

        alert("Login successful!")

        this.$router.push("/dashboard")

      } catch (error) {

        console.log("LOGIN ERROR FULL:", error)
        console.log("DETAIL:", error.response?.data)

        alert("Login failed - check console")

      }

    }

  }
}
</script>
