<template>
  <div class="space-y-6">
    <section class="rounded-[1.75rem] border border-slate-200 bg-linear-to-br from-slate-900 via-blue-900 to-cyan-700 p-5 text-white shadow-xl sm:p-6">
      <div class="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p class="text-sm font-medium uppercase tracking-[0.25em] text-blue-100">Project details</p>
          <h1 class="mt-2 text-xl font-semibold sm:text-2xl">{{ project.name || "Loading project..." }}</h1>
          <p class="mt-2 max-w-2xl text-sm leading-6 text-blue-50">{{ project.description || "No description available yet." }}</p>
        </div>
        <router-link to="/dashboard" class="rounded-xl border border-white/20 bg-white/10 px-4 py-2 text-sm font-semibold text-white transition hover:bg-white/20">
          Back to dashboard
        </router-link>
      </div>
    </section>

    <section class="rounded-[1.75rem] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
      <div class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h2 class="text-lg font-semibold text-slate-900">Add a car</h2>
          <p class="text-sm leading-6 text-slate-500">Add one or more cars to this project.</p>
        </div>
      </div>

      <form @submit.prevent="addCar" class="mt-4 grid gap-3 lg:grid-cols-[1fr_1fr_auto]">
        <div>
          <label class="mb-1.5 block text-sm font-medium text-slate-700">Car name</label>
          <input v-model="newCar.name" required placeholder="Enter car name" class="w-full rounded-xl border border-slate-200 bg-slate-50 px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100" />
        </div>
        <div>
          <label class="mb-1.5 block text-sm font-medium text-slate-700">Car type</label>
          <input v-model="newCar.car_type" required placeholder="Enter car type" class="w-full rounded-xl border border-slate-200 bg-slate-50 px-3.5 py-2.5 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100" />
        </div>
        <div class="flex items-end">
          <button type="submit" class="w-full rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white shadow-lg shadow-blue-600/20 transition hover:bg-blue-700">
            Add car
          </button>
        </div>
      </form>
    </section>

    <section class="rounded-[1.75rem] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-lg font-semibold text-slate-900">Cars in this project</h2>
          <p class="text-sm leading-6 text-slate-500">All cars linked to this project appear here.</p>
        </div>
      </div>

      <div v-if="cars.length" class="mt-4 grid gap-4 md:grid-cols-2">
        <article v-for="car in cars" :key="car.id" class="rounded-3xl border border-slate-200 bg-slate-50 p-4">
          <div class="flex items-start justify-between gap-3">
            <div>
              <h3 class="text-base font-semibold text-slate-900">{{ car.name }}</h3>
              <p class="mt-1 text-sm text-slate-600">{{ car.car_type }}</p>
            </div>
            <button @click="deleteCar(car.id)" class="text-sm font-medium text-red-500 transition hover:text-red-600">Delete</button>
          </div>
        </article>
      </div>

      <div v-else class="mt-4 rounded-3xl border border-dashed border-slate-300 bg-slate-50 p-8 text-center">
        <h3 class="text-base font-semibold text-slate-800">No cars yet</h3>
        <p class="mt-2 text-sm text-slate-500">Use the form above to add your first car.</p>
      </div>
    </section>
  </div>
</template>

<script>
import api from "../api/axios";

export default {
  data() {
    return {
      project: {},
      cars: [],
      newCar: {
        name: "",
        car_type: "",
      },
    };
  },
  mounted() {
    this.getProject();
    this.getCars();
  },
  methods: {
    getToken() {
      return localStorage.getItem("token");
    },
    async getProject() {
      try {
        const id = this.$route.params.id;
        const res = await api.get(`projects/${id}/`);
        this.project = res.data;
      } catch (error) {
        console.error("PROJECT ERROR:", error.response?.data || error);
      }
    },
    async getCars() {
      try {
        const projectId = Number(this.$route.params.id);
        const res = await api.get("cars/");
        this.cars = res.data.filter((car) => car.project === projectId);
      } catch (error) {
        console.error("CARS ERROR:", error.response?.data || error);
      }
    },
    async addCar() {
      try {
        if (!this.newCar.name || !this.newCar.car_type) return;

        const projectId = Number(this.$route.params.id);
        await api.post("cars/", {
          name: this.newCar.name,
          car_type: this.newCar.car_type,
          project: projectId,
        });

        this.newCar = { name: "", car_type: "" };
        this.getCars();
      } catch (error) {
        console.error("ADD CAR ERROR:", error.response?.data || error);
      }
    },
    async deleteCar(id) {
      try {
        await api.delete(`cars/${id}/`);
        this.getCars();
      } catch (error) {
        console.error("DELETE CAR ERROR:", error.response?.data || error);
      }
    },
  },
};
</script>
