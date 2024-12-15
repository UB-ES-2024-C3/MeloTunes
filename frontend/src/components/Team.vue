<template>
  <div class="card">
    <h5 class="card-header">{{ name }}</h5>
    <div class="card-body">
      <h5 class="card-title">Informació</h5>
      <p class="card-text"><strong>ID:</strong> {{title}}</p>
      <p class="card-text"><strong>email:</strong> {{artist}}</p>
      <p class="card-text"><strong>Nombre:</strong> {{album}}</p>
    </div>
    <div v-if="description" class="card-footer">{{description}}</div>
  </div>
</template>

<script>
export default {
  name: 'Team',
  props: ['title', 'artist', 'album']
}
</script>
