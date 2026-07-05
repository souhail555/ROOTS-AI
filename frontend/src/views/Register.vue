<template>
  <div class="flex min-h-screen items-center justify-center bg-slate-950 px-4 py-10">
    <div class="w-full max-w-md rounded-[1.75rem] border border-slate-200 bg-white p-6 shadow-2xl shadow-slate-900/10 sm:p-7">
      <div class="text-center">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-linear-to-br from-blue-600 to-cyan-500 text-lg font-semibold text-white shadow-lg">
          R
        </div>
        <h2 class="mt-4 text-lg font-semibold text-slate-900">Create your account</h2>
        <p class="mt-2 text-sm leading-6 text-slate-500">Start building your project workspace in minutes.</p>
      </div>

      <form @submit.prevent="register" class="mt-6 space-y-3">
        <div>
          <label class="mb-1.5 block text-sm font-medium text-slate-700">Username</label>
          <input
            v-model="username"
            placeholder="Choose a username"
            class="block w-full rounded-xl border border-slate-200 bg-slate-50 px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
          />
        </div>

        <div>
          <label class="mb-1.5 block text-sm font-medium text-slate-700">Password</label>
          <input
            v-model="password"
            type="password"
            placeholder="Create a secure password"
            class="block w-full rounded-xl border border-slate-200 bg-slate-50 px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
          />
        </div>

        <button
          type="submit"
          class="flex w-full items-center justify-center rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white shadow-lg shadow-blue-600/20 transition hover:bg-blue-700"
        >
          Register
        </button>

        <p v-if="message" :class="message.includes('success') ? 'text-emerald-600' : 'text-red-600'" class="rounded-xl border px-3 py-2 text-sm">
          {{ message }}
        </p>

        <p class="text-center text-sm text-slate-500">
          Already have an account?
          <router-link to="/" class="font-medium text-blue-600 hover:text-blue-700">Sign in</router-link>
        </p>
      </form>
    </div>
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
