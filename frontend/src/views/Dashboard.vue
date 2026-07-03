<template>
  <div>

    <h1>Projects Dashboard</h1>

    <!-- ADD -->
    <input v-model="newProject.name" placeholder="name" />
    <input v-model="newProject.description" placeholder="description" />

    <button @click="addProject">Add</button>

    <hr />

    <!-- TABLE -->
    <table border="1" width="100%">
      <tr v-for="p in projects" :key="p.id">
        <td>{{ p.name }}</td>
        <td>{{ p.description }}</td>

        <td>
          <button @click="deleteProject(p.id)">
            Delete
          </button>
        </td>
      </tr>
    </table>

  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      projects: [],
      newProject: {
        name: "",
        description: ""
      }
    }
  },

  mounted() {
    this.getProjects()
  },

  methods: {

    async getProjects() {
      const res = await axios.get(
        "http://127.0.0.1:8000/api/projects/"
      )

      this.projects = res.data
    },

    async addProject() {
      await axios.post(
        "http://127.0.0.1:8000/api/projects/",
        this.newProject
      )

      this.newProject.name = ""
      this.newProject.description = ""

      this.getProjects()
    },

    async deleteProject(id) {
      await axios.delete(
        `http://127.0.0.1:8000/api/projects/${id}/`
      )

      this.getProjects()
    }

  }
}
</script>
