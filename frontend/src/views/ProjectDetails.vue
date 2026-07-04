<template>
  <div class="min-h-screen bg-slate-100 p-8">

    <div class="max-w-6xl mx-auto">

      <!-- PROJECT INFO -->
      <div class="bg-white shadow-xl rounded-2xl p-8 mb-8">

        <h1 class="text-4xl font-bold mb-4">
          {{ project.name }}
        </h1>

        <p class="text-gray-600 text-lg">
          {{ project.description }}
        </p>

      </div>

      <!-- ADD CAR -->
      <div class="bg-white shadow-xl rounded-2xl p-8 mb-8">

        <h2 class="text-2xl font-bold mb-6">
          Add Car
        </h2>

        <div class="grid grid-cols-3 gap-4">

          <input
            v-model="newCar.name"
            placeholder="Car Name"
            class="border p-3 rounded-xl"
          />

          <input
            v-model="newCar.car_type"
            placeholder="Car Type"
            class="border p-3 rounded-xl"
          />

          <button
            @click="addCar"
            class="bg-blue-600 text-white px-4 py-2 rounded-xl"
          >
            Add Car
          </button>

        </div>

      </div>

      <!-- CARS TABLE -->
      <div class="bg-white shadow-xl rounded-2xl p-8">

        <h2 class="text-2xl font-bold mb-6">
          Cars
        </h2>

        <table class="w-full border">

          <thead class="bg-slate-800 text-white">
            <tr>
              <th class="p-4 text-left">Name</th>
              <th class="p-4 text-left">Type</th>
              <th class="p-4 text-center">Actions</th>
            </tr>
          </thead>

          <tbody>

            <tr
              v-for="car in cars"
              :key="car.id"
              class="border-t"
            >

              <td class="p-4">
                {{ car.name }}
              </td>

              <td class="p-4">
                {{ car.car_type }}
              </td>

              <td class="p-4 text-center">

                <button
                  @click="deleteCar(car.id)"
                  class="bg-red-500 text-white px-4 py-2 rounded-lg"
                >
                  Delete
                </button>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>
</template>

<script>
import axios from "axios"

export default {

  data() {
    return {

      project: {},

      cars: [],

      newCar: {
        name: "",
        car_type: ""
      }

    }
  },

  mounted() {
    this.getProject()
    this.getCars()
  },

  methods: {

    getToken() {
      return localStorage.getItem("token")
    },

    async getProject() {

      try {

        const id = this.$route.params.id

        const res = await axios.get(
          `http://127.0.0.1:8000/api/projects/${id}/`,
          {
            headers: {
              Authorization: `Bearer ${this.getToken()}`
            }
          }
        )

        this.project = res.data

      } catch (error) {

        console.log(
          "PROJECT ERROR:",
          error.response?.data || error
        )

      }

    },

    async getCars() {

      try {

        const projectId = Number(
          this.$route.params.id
        )

        const res = await axios.get(
          "http://127.0.0.1:8000/api/cars/",
          {
            headers: {
              Authorization: `Bearer ${this.getToken()}`
            }
          }
        )

        this.cars = res.data.filter(
          car => car.project === projectId
        )

      } catch (error) {

        console.log(
          "CARS ERROR:",
          error.response?.data || error
        )

      }

    },

    async addCar() {

      try {

        if (
          !this.newCar.name ||
          !this.newCar.car_type
        ) {
          return
        }

        const projectId = Number(
          this.$route.params.id
        )

        await axios.post(
          "http://127.0.0.1:8000/api/cars/",
          {
            name: this.newCar.name,
            car_type: this.newCar.car_type,
            project: projectId
          },
          {
            headers: {
              Authorization: `Bearer ${this.getToken()}`
            }
          }
        )

        this.newCar = {
          name: "",
          car_type: ""
        }

        this.getCars()

      } catch (error) {

        console.log(
          "ADD CAR ERROR:",
          error.response?.data || error
        )

      }

    },

    async deleteCar(id) {

      try {

        await axios.delete(
          `http://127.0.0.1:8000/api/cars/${id}/`,
          {
            headers: {
              Authorization: `Bearer ${this.getToken()}`
            }
          }
        )

        this.getCars()

      } catch (error) {

        console.log(
          "DELETE CAR ERROR:",
          error.response?.data || error
        )

      }

    }

  }

}
</script>
