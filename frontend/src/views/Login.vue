<template>
  <div class="min-h-screen flex items-center justify-center px-4 bg-gradient-to-br from-blue-50 to-white">
    <div class="w-full max-w-md bg-surface shadow-lg rounded-lg p-6 border border-blue-50">
      <div class="text-center mb-6">
        <h1 class="text-2xl font-semibold text-primary-700">Roots AI</h1>
        <p class="text-sm text-gray-600">Sign in to your account</p>
      </div>

      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Username</label>
          <input
            v-model="username"
            type="text"
            required
            class="mt-1 block w-full rounded-md border-gray-200 shadow-sm focus:border-primary-500 focus:ring-primary-500"
            placeholder="your username"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Password</label>
          <div class="relative mt-1">
            <input
              :type="show ? 'text' : 'password'"
              v-model="password"
              required
              class="block w-full rounded-md border-gray-200 shadow-sm pr-10 focus:border-primary-500 focus:ring-primary-500"
              placeholder="••••••••"
            />
            <button type="button" @click="show = !show" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm">
              <span class="text-gray-500">{{ show ? 'Hide' : 'Show' }}</span>
            </button>
          </div>
        </div>

        <div class="flex items-center justify-between">
          <label class="inline-flex items-center text-sm">
            <input type="checkbox" v-model="remember" class="rounded text-primary-600" />
            <span class="ml-2 text-gray-600">Remember me</span>
          </label>
          <router-link to="/register" class="text-sm text-primary-600 hover:underline">Create account</router-link>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="w-full inline-flex justify-center rounded-md bg-primary-600 text-white px-4 py-2 font-medium hover:bg-primary-700 shadow-md disabled:opacity-60 transition-colors"
          >
            <span v-if="!loading">Sign in</span>
            <span v-else>Signing in...</span>
          </button>
        </div>

        <p v-if="error" class="text-sm text-red-600">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script>
import api from "../api/axios"

export default {
  data() {
    return {
      username: "",
      password: "",
      remember: false,
      loading: false,
      error: null,
      show: false
    }
  },

  methods: {
    async login() {
      this.error = null
      this.loading = true
      try {
        const res = await api.post('token/', {
          username: this.username,
          password: this.password
        })

        const token = res.data.access
        localStorage.setItem('token', token)

        // Optional: persist longer if "remember"
        if (this.remember) {
          // no-op here; localStorage persists by default
        }

        this.$router.push('/dashboard')
      } catch (err) {
        console.error('Login failed:', err)
        this.error = err.response?.data?.detail || 'Invalid credentials'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.bg-surface { background-color: var(--surface); }
</style>
