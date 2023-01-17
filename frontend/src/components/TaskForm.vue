<script>
  import axios from 'axios';
  
  export default {
    emits: ['update'],
    data() {
      return {
        name: ''
      }
    },
    methods: {
      async add(event) {
        event.preventDefault();
        axios.post(
          'http://localhost/api/v1/tasks',
          {
            name: this.name,
            start: new Date()
          }
        );

        this.$emit('update')
      }
    }
  }
</script>

<template>
  <h2>Task List</h2>
  <form>
  	<label>Name</label><br />
  	<input v-model="name" type="text" name="name" />
  	<button @click="add">Add</button>
  </form>
</template>

<style scoped>
</style>