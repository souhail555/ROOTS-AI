<template>
  <div class="space-y-6">
    <section class="rounded-[1.75rem] border border-slate-200 bg-linear-to-br from-slate-900 via-blue-900 to-cyan-700 p-5 text-white shadow-xl sm:p-6">
      <div class="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
        <div>
          <p class="text-sm font-medium uppercase tracking-[0.25em] text-blue-100">Project overview</p>
          <h1 class="mt-2 text-xl font-semibold sm:text-2xl">Your workspace looks ready.</h1>
          <p class="mt-2 max-w-2xl text-sm leading-6 text-blue-50">
            Track ideas, create new deliverables, and stay organized with a more polished experience.
          </p>
        </div>

        <div class="grid gap-3 sm:grid-cols-2">
          <div class="rounded-2xl bg-white/10 px-4 py-3 backdrop-blur">
            <p class="text-sm text-blue-100">Projects</p>
            <p class="text-2xl font-semibold">{{ projects.length }}</p>
          </div>
          <div class="rounded-2xl bg-white/10 px-4 py-3 backdrop-blur">
            <p class="text-sm text-blue-100">Status</p>
            <p class="text-2xl font-semibold">Live</p>
          </div>
        </div>
      </div>
    </section>

    <section class="rounded-[1.75rem] border border-slate-200 bg-white p-4 shadow-sm sm:p-5">
      <div class="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h2 class="text-lg font-semibold text-slate-900">Projects</h2>
          <p class="mt-1 text-sm leading-6 text-slate-500">Create projects and open them to manage their cars.</p>
        </div>

        <div class="flex flex-col gap-2 sm:flex-row sm:items-center">
          <input
            v-model="query"
            @input="onSearch"
            placeholder="Search projects..."
            class="rounded-xl border border-slate-200 bg-slate-50 px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
          />

          <button
            @click="showForm = !showForm"
            class="rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white shadow-lg shadow-blue-600/20 transition hover:bg-blue-700"
          >
            <span v-if="!showForm">New Project</span>
            <span v-else>Close</span>
          </button>
        </div>
      </div>

      <section v-if="showForm" class="mt-6 rounded-3xl border border-blue-100 bg-blue-50/70 p-4 sm:p-5">
        <h3 class="text-lg font-semibold text-slate-900">Create a new project</h3>
        <p class="mt-1 text-sm text-slate-600">Enter the project name and a short description.</p>
        <form @submit.prevent="addProject" class="mt-4 grid gap-3 lg:grid-cols-[1fr_1fr_auto]">
          <div>
            <label class="mb-1.5 block text-sm font-medium text-slate-700">Project name</label>
            <input v-model="newProject.name" required placeholder="Enter project name" class="w-full rounded-xl border border-slate-200 bg-white px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-100" />
          </div>
          <div>
            <label class="mb-1.5 block text-sm font-medium text-slate-700">Short description</label>
            <input v-model="newProject.description" required placeholder="Enter short description" class="w-full rounded-xl border border-slate-200 bg-white px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-100" />
          </div>
          <div class="flex gap-2">
            <button type="submit" :disabled="loading" class="rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-70">
              <span v-if="!loading">Create</span>
              <span v-else>Creating...</span>
            </button>
            <button type="button" @click="resetForm" class="rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-sm font-semibold text-slate-600 transition hover:bg-slate-100">Reset</button>
          </div>
        </form>
        <p v-if="error" class="mt-3 text-sm text-red-600">{{ error }}</p>
      </section>
    </section>

    <section class="grid gap-6 xl:grid-cols-[1.4fr_0.6fr]">
      <div class="rounded-4xl border border-slate-200 bg-white p-4 shadow-sm sm:p-6">
        <div v-if="filtered.length" class="grid gap-4 md:grid-cols-2">
          <article v-for="project in filtered" :key="project.id" class="rounded-3xl border border-slate-200 bg-slate-50 p-5 transition hover:-translate-y-0.5 hover:shadow-md">
            <div class="flex items-start justify-between gap-3">
              <div>
                <router-link :to="{ name: 'ProjectDetails', params: { id: project.id } }" class="text-lg font-semibold text-slate-900 transition hover:text-blue-600">
                  {{ project.name }}
                </router-link>
                <p class="mt-2 text-sm leading-6 text-slate-600">{{ project.description }}</p>
                <p class="mt-3 text-xs font-medium uppercase tracking-[0.2em] text-slate-400">Open to manage cars</p>
              </div>
              <button @click="deleteProject(project.id)" class="text-sm font-medium text-red-500 transition hover:text-red-600">Delete</button>
            </div>
          </article>
        </div>

        <div v-else class="rounded-3xl border border-dashed border-slate-300 bg-slate-50 p-10 text-center">
          <h3 class="text-lg font-semibold text-slate-800">No projects found</h3>
          <p class="mt-2 text-sm text-slate-500">Use “New Project” to add your first project and open it from here.</p>
        </div>
      </div>

      <aside class="rounded-[1.75rem] border border-slate-200 bg-slate-900 p-5 text-white shadow-sm">
        <p class="text-sm font-medium uppercase tracking-[0.25em] text-blue-200">Design focus</p>
        <h3 class="mt-3 text-lg font-semibold">A refined experience for everyday work</h3>
        <ul class="mt-4 space-y-3 text-sm text-slate-300">
          <li class="rounded-2xl bg-white/10 px-3 py-2">Clear layout with calm contrast and strong hierarchy</li>
          <li class="rounded-2xl bg-white/10 px-3 py-2">Modern cards that make project details easy to scan</li>
          <li class="rounded-2xl bg-white/10 px-3 py-2">Focused actions to reduce clutter and speed up entry</li>
        </ul>
      </aside>
    </section>
  </div>
</template>

<script>
import api from "../api/axios";

export default {
  data() {
    return {
      projects: [],
      newProject: { name: "", description: "" },
      loading: false,
      error: null,
      showForm: false,
      query: "",
    };
  },
  computed: {
    filtered() {
      if (!this.query) return this.projects;
      const q = this.query.toLowerCase();
      return this.projects.filter(
        (project) =>
          (project.name || "").toLowerCase().includes(q) ||
          (project.description || "").toLowerCase().includes(q)
      );
    },
  },
  mounted() {
    this.getProjects();
  },
  methods: {
    async getProjects() {
      try {
        const res = await api.get("projects/");
        this.projects = res.data;
      } catch (err) {
        console.error("Failed to load projects", err);
        this.error = "Failed to load projects";
      }
    },
    async addProject() {
      this.error = null;
      this.loading = true;
      try {
        await api.post("projects/", this.newProject);
        this.resetForm();
        this.showForm = false;
        await this.getProjects();
      } catch (err) {
        console.error("Create failed", err);
        this.error = err.response?.data?.detail || "Create failed";
      } finally {
        this.loading = false;
      }
    },
    resetForm() {
      this.newProject.name = "";
      this.newProject.description = "";
      this.error = null;
    },
    async deleteProject(id) {
      if (!confirm("Delete this project?")) return;
      try {
        await api.delete(`projects/${id}/`);
        await this.getProjects();
      } catch (err) {
        console.error("Delete failed", err);
        this.error = "Delete failed";
      }
    },
    onSearch() {
      // computed `filtered` will react
    },
  },
};
</script>
