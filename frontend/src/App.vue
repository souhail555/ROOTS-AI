<template>
  <div>
    <h1>ROOTS AI 🚀</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Loading..."
    }
  },
  mounted() {
    fetch("http://127.0.0.1:8000/api/")
      .then(res => res.json())
      .then(data => {
        this.message = data.message
      })
  }
}
</script>