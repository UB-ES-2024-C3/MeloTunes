<template>
  <div class="card">
    <h5 class="card-header">{{ name }}</h5>
    <div class="card-body">
      <h5 class="card-title">Informació</h5>
      <p class="card-text"><strong>ID:</strong> {{id}}</p>
      <p class="card-text"><strong>email:</strong> {{email}}</p>
      <p class="card-text"><strong>Nombre:</strong> {{full_name}}</p>
    </div>
    <div v-if="description" class="card-footer">{{description}}</div>
  </div>
</template>

<script>
export default {
  name: 'Team',
  props: ['id', 'email', 'full_name']
}
</script>
