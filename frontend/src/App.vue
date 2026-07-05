<template>
  <div class="min-h-screen bg-slate-50 text-slate-800">
    <header v-if="showShell" class="border-b border-slate-200 bg-white/80 backdrop-blur">
      <div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
        <router-link to="/dashboard" class="flex items-center gap-3">
          <div class="flex h-10 w-10 items-center justify-center rounded-2xl bg-linear-to-br from-blue-600 to-cyan-500 text-sm font-semibold text-white shadow-lg">
            RA
          </div>
          <div>
            <p class="text-base font-semibold text-slate-900">Roots AI</p>
            <p class="text-sm text-slate-500">Project workspace</p>
          </div>
        </router-link>

        <div class="flex items-center gap-4">
          <div class="hidden rounded-full bg-slate-100 px-3 py-2 text-sm font-medium text-slate-700 sm:inline-flex">
            Hello, {{ currentUser || 'Team member' }}
          </div>
          <router-link
            to="/dashboard"
            class="hidden rounded-full px-3 py-2 text-sm font-medium text-slate-600 transition hover:bg-slate-100 hover:text-slate-900 sm:inline-flex"
          >
            Dashboard
          </router-link>
          <button
            @click="logout"
            class="rounded-full border border-slate-200 px-3 py-2 text-sm font-medium text-slate-600 transition hover:border-blue-200 hover:text-blue-600"
          >
            Logout
          </button>
        </div>
      </div>
    </header>

    <main class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  computed: {
    showShell() {
      return this.$route.path !== "/" && this.$route.path !== "/register";
    },
    currentUser() {
      return localStorage.getItem("username");
    },
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      this.$router.push("/");
    },
  },
};
</script>
