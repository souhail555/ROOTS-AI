<template>
  <div class="relative min-h-screen overflow-hidden bg-slate-950">
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_left,rgba(59,130,246,0.28),transparent_35%),radial-gradient(circle_at_bottom_right,rgba(6,182,212,0.2),transparent_35%)]"></div>

    <div class="relative mx-auto flex min-h-screen max-w-7xl items-center justify-center px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid w-full max-w-5xl overflow-hidden rounded-[1.75rem] border border-white/10 bg-white/95 shadow-2xl backdrop-blur lg:grid-cols-[1.05fr_0.95fr]">
        <div class="flex flex-col justify-between bg-linear-to-br from-blue-700 via-blue-600 to-cyan-500 p-6 text-white sm:p-8">
          <div>
            <div class="inline-flex items-center rounded-full bg-white/15 px-3 py-1 text-sm font-medium backdrop-blur">
              Welcome back
            </div>
            <h1 class="mt-5 text-xl font-semibold sm:text-2xl">Turn ideas into clear project momentum.</h1>
            <p class="mt-2 max-w-md text-sm leading-6 text-blue-50">
              Keep your team aligned, track work effortlessly, and move from planning to delivery in one calm workspace.
            </p>
          </div>

          <div class="mt-8 space-y-3 text-sm text-blue-50">
            <div class="flex items-center gap-3 rounded-2xl bg-white/10 px-3 py-2">
              <span class="h-2.5 w-2.5 rounded-full bg-cyan-200"></span>
              <span>Shared project visibility for every teammate</span>
            </div>
            <div class="flex items-center gap-3 rounded-2xl bg-white/10 px-3 py-2">
              <span class="h-2.5 w-2.5 rounded-full bg-cyan-200"></span>
              <span>Fast onboarding with a simple sign-in flow</span>
            </div>
          </div>
        </div>

        <div class="p-6 sm:p-8">
          <div class="mb-6 text-center lg:text-left">
            <p class="text-sm font-medium uppercase tracking-[0.25em] text-blue-600">Sign in</p>
            <h2 class="mt-2 text-lg font-semibold text-slate-900">Access your workspace</h2>
            <p class="mt-2 text-sm leading-6 text-slate-500">Use your credentials to continue where you left off.</p>
          </div>

          <form @submit.prevent="login" class="space-y-3">
            <div>
              <label class="mb-1.5 block text-sm font-medium text-slate-700">Username</label>
              <input
                v-model="username"
                type="text"
                required
                class="block w-full rounded-xl border border-slate-200 bg-slate-50 px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
                placeholder="your username"
              />
            </div>

            <div>
              <label class="mb-1.5 block text-sm font-medium text-slate-700">Password</label>
              <div class="relative">
                <input
                  :type="show ? 'text' : 'password'"
                  v-model="password"
                  required
                  class="block w-full rounded-xl border border-slate-200 bg-slate-50 px-3.5 py-2.5 pr-16 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
                  placeholder="••••••••"
                />
                <button type="button" @click="show = !show" class="absolute inset-y-0 right-0 flex items-center pr-4 text-sm font-medium text-slate-500">
                  {{ show ? "Hide" : "Show" }}
                </button>
              </div>
            </div>

            <div class="flex items-center justify-between gap-3 text-sm">
              <label class="inline-flex items-center text-slate-600">
                <input type="checkbox" v-model="remember" class="h-4 w-4 rounded border-slate-300 text-blue-600 focus:ring-blue-500" />
                <span class="ml-2">Remember me</span>
              </label>
              <router-link to="/register" class="font-medium text-blue-600 transition hover:text-blue-700">Create account</router-link>
            </div>

            <button
              type="submit"
              :disabled="loading"
              class="flex w-full items-center justify-center rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white shadow-lg shadow-blue-600/20 transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-70"
            >
              <span v-if="!loading">Sign in</span>
              <span v-else>Signing in...</span>
            </button>

            <p class="mt-3 text-sm text-slate-500">
              Default login: <strong>Admin</strong> / <strong>Admin#12345</strong>
            </p>
            <p v-if="error" class="rounded-xl border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-600">{{ error }}</p>
          </form>
        </div>
      </div>
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
      remember: false,
      loading: false,
      error: null,
      show: false,
    };
  },
  methods: {
    async login() {
      this.error = null;
      this.loading = true;
      try {
        const res = await api.post("token/", {
          username: this.username,
          password: this.password,
        });

        const token = res.data.access;
        const refresh = res.data.refresh;
        localStorage.setItem("token", token);
        localStorage.setItem("refresh", refresh);
        localStorage.setItem("username", this.username);
        this.$router.push("/dashboard");
      } catch (err) {
        console.error("Login failed:", err);
        this.error = err.response?.data?.detail || "Cannot reach server. Please make sure backend is running.";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
