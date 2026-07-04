<template>
  <div class="min-h-screen p-6 bg-gradient-to-br from-blue-50 to-white">
    <div class="max-w-7xl mx-auto">
      <header class="flex items-center justify-between mb-6">
        <div>
          <h1 class="text-2xl font-semibold text-primary-700">Projects Dashboard</h1>
          <p class="text-sm text-gray-600">Overview of your projects</p>
        </div>

        <div class="flex items-center gap-3">
          <input
            v-model="query"
            @input="onSearch"
            placeholder="Search projects..."
            class="px-3 py-2 rounded border border-gray-200 focus:ring-primary-500 focus:border-primary-500"
          />

          <button
            @click="showForm = !showForm"
            class="inline-flex items-center gap-2 bg-primary-600 text-white px-4 py-2 rounded shadow hover:bg-primary-700"
          >
            <span v-if="!showForm">New Project</span>
            <span v-else>Close</span>
          </button>
        </div>
      </header>

      <section v-if="showForm" class="mb-6 bg-white p-4 rounded shadow-sm border">
        <h2 class="text-lg font-medium text-gray-800 mb-3">Create Project</h2>
        <form @submit.prevent="addProject" class="grid grid-cols-1 gap-3 sm:grid-cols-2">
          <input v-model="newProject.name" required placeholder="Project name" class="p-2 border rounded" />
          <input v-model="newProject.description" required placeholder="Short description" class="p-2 border rounded" />
          <div class="sm:col-span-2 flex gap-3">
            <button type="submit" :disabled="loading" class="bg-primary-600 text-white px-4 py-2 rounded">
              <span v-if="!loading">Create</span>
              <span v-else>Creating...</span>
            </button>
            <button type="button" @click="resetForm" class="px-4 py-2 rounded border">Reset</button>
            <p v-if="error" class="text-red-600 ml-4">{{ error }}</p>
          </div>
        </form>
      </section>

      <section>
        <div class="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
          <div v-for="p in filtered" :key="p.id" class="bg-white rounded-lg p-4 shadow hover:shadow-md border">
            <div class="flex items-start justify-between">
              <div>
                <h3 class="text-lg font-semibold text-gray-800">{{ p.name }}</h3>
                <p class="text-sm text-gray-600 mt-2">{{ p.description }}</p>
              </div>
              <div class="flex flex-col items-end gap-2">
                <button @click="deleteProject(p.id)" class="text-sm text-red-600 hover:underline">Delete</button>
              </div>
            </div>
          </div>
        </div>

        <p v-if="!filtered.length" class="text-center text-gray-500 mt-8">No projects found.</p>
      </section>
    </div>
  </div>
</template>

<script>
import api from "../api/axios"

export default {
  data() {
    return {
      projects: [],
      newProject: { name: "", description: "" },
      loading: false,
      error: null,
      showForm: false,
      query: ''
    }
  },

  computed: {
    filtered() {
      if (!this.query) return this.projects
      const q = this.query.toLowerCase()
      return this.projects.filter(p => (p.name || '').toLowerCase().includes(q) || (p.description || '').toLowerCase().includes(q))
    }
  },

  mounted() {
    this.getProjects()
  },

  methods: {
    async getProjects() {
      try {
        const res = await api.get('projects/')
        this.projects = res.data
      } catch (err) {
        console.error('Failed to load projects', err)
        this.error = 'Failed to load projects'
      }
    },

    async addProject() {
      this.error = null
      this.loading = true
      try {
        await api.post('projects/', this.newProject)
        this.resetForm()
        this.showForm = false
        await this.getProjects()
      } catch (err) {
        console.error('Create failed', err)
        this.error = err.response?.data?.detail || 'Create failed'
      } finally {
        this.loading = false
      }
    },

    resetForm() {
      this.newProject.name = ''
      this.newProject.description = ''
      this.error = null
    },

    async deleteProject(id) {
      if (!confirm('Delete this project?')) return
      try {
        await api.delete(`projects/${id}/`)
        await this.getProjects()
      } catch (err) {
        console.error('Delete failed', err)
        this.error = 'Delete failed'
      }
    },

    onSearch() {
      // computed `filtered` will react
    }
  }
}
</script>
