<script>
  import axios from 'axios';
  
  export default {
    props: {
      tasks: Array,
      test: String
    },
    emits: ['update'],
    methods: {
      update() {
        this.$emit('update');
      },
      async stop(id) {
        const resp = await axios.patch(
          `http://localhost/api/v1/tasks/${id}`,
          {
            end: new Date()
          }
        );

        if(resp.status === 200) {
          this.update()
          this.$emit('update');
        }
      }
    }
  }
</script>

<template>
  <h2>Task List</h2>
  <table>
    <thead>
      <th>Name</th>
      <th>From</th>
      <th>To</th>
      <th>Action</th>
    </thead>
    <tbody>
      <tr v-for="task in tasks" :key="task.id">
        <td>{{ task.name }}</td>
        <td>{{ task.start }}</td>
        <td>{{ task.end }}</td>
        <td><button @click="stop(task.id)">Stop</button></td>
      </tr>
    </tbody>
    {{ test }}
  </table>
</template>

<style scoped>
</style>