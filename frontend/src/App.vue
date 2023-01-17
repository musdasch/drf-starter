<script setup>
import TaskList from './components/TaskList.vue'
import TaskForm from './components/TaskForm.vue'
</script>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      tasks: []
    }
  },
  methods: {
    async update() {
      this.tasks = [];

      const resp = await axios.get(
        'http://localhost/api/v1/tasks'
      );

      if(resp.status === 200) {
        this.tasks = resp.data.map((task) => {
          const start = new Date(task.start);
          task.start = `${start.getDay()}.${start.getMonth()}.${start.getFullYear()} ${start.getHours()}:${start.getMinutes()}`;
          const end = new Date(task.end);
          task.end = `${end.getDay()}.${end.getMonth()}.${end.getFullYear()} ${end.getHours()}:${end.getMinutes()}`;
          return task;
        });
      }
    }
  },
  mounted() {
    this.update()
  }
}
</script>

<template>
  <main>
    <TaskForm @update="update" />
    <TaskList @update="update" :tasks="tasks" />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
