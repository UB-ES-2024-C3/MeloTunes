<template>
  <div class="perfil-artist">
    <!-- Encabezado del perfil con fondo -->
    <header class="perfil-header">
      <div class="avatar-container">
        <img src="../assets/artistas/melendi.jpeg" alt="Avatar del artista" class="avatar" />
      </div>
      <div class="artist-details">
        <h1>{{ artistStageName }}</h1>
        <p class="genre">{{ genre }}</p>
        <p v-if="expandedBio" class="bio">{{ bio }}</p>
        <p v-else class="bio-short">{{ shortBio }}</p>
        <button class="btn-toggle-bio" @click="toggleBio">{{ expandedBio ? 'Ver menos' : 'Ver más' }}</button>
      </div>
    </header>

    <!-- Sección Discografía y Colaboraciones en columnas con línea divisoria -->
    <section class="top-section">
      <div class="top-columns">
        <!-- Discografía Destacada -->
        <div class="top-discography">
          <h2>Discografía Destacada</h2>
          <ul>
            <li v-for="album in discography" :key="album.id">{{ album.title }} - {{ album.releaseYear }}</li>
          </ul>
        </div>

        <!-- Línea divisoria -->
        <div class="divider"></div>

        <!-- Colaboraciones -->
        <div class="top-collaborations">
          <h2>Colaboraciones</h2>
          <ul>
            <li v-for="collab in collaborations" :key="collab.id">{{ collab.title }} - {{ collab.artist }}</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Próximos Conciertos -->
    <section class="events">
      <h2>Próximos Conciertos</h2>
      <ul>
        <li v-for="event in upcomingEvents" :key="event.id">{{ event.name }} - {{ event.date }} - {{ event.location }}</li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ArtistProfile',
  data () {
    return {
      artistStageName: 'MELENDI',
      genre: 'Rumba - Pop - Rock',
      bio: 'Artista con un estilo único que combina pop, rock y flamenco. Con más de dos décadas en la industria, 20 años sin noticias de holanda...',
      shortBio: 'Artista de pop rock y flamenco...',
      expandedBio: false,
      discography: [
        { id: 1, title: 'Sin Noticias de Holanda', releaseYear: '2003' },
        { id: 2, title: 'Que el Cielo Espere Sentao', releaseYear: '2005' },
        { id: 3, title: 'Volvamos a Empezar', releaseYear: '2010' }
      ],
      collaborations: [
        { id: 1, title: 'Destino o Casualidad', artist: 'Ha*Ash' },
        { id: 2, title: 'Desde que estamos juntos', artist: 'Alejandro Sanz' }
      ],
      upcomingEvents: [
        { id: 1, name: 'Gira 2024 - Madrid', date: '15 de marzo', location: 'Wizink Center, Madrid' },
        { id: 2, name: 'Gira 2024 - Sevilla', date: '29 de marzo', location: 'Auditorio Rocío Jurado, Sevilla' }
      ]
    }
  },
  methods: {
    toggleBio () {
      this.expandedBio = !this.expandedBio
    }
  }
}
</script>

<style scoped>
/* Nuevos estilos para el nombre real */
.real-name {
  color: #ccc;
  font-size: 1rem;
  margin-top: 0.5rem;
}

.perfil-artist {
  background-color: #121212;
  color: white;
  padding: 2rem;
  min-height: 100vh;
}

.perfil-header {
  background: #1f1f1f;
  padding: 2rem;
  display: flex;
  align-items: center;
  border-radius: 12px;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  margin-bottom: 2rem;
}

.avatar-container {
  flex-shrink: 0;
  margin-right: 1.5rem;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 3px solid #ff3d00;
  object-fit: cover;
}

.artist-details {
  flex-grow: 1;
  max-width: 500px;
}

.artist-details h1 {
  font-size: 2rem;
  margin: 0;
  font-weight: 700;
}

.genre {
  color: #aaa;
  margin-top: 0.5rem;
}

.bio, .bio-short {
  margin-top: 1rem;
  font-size: 1rem;
}

.btn-toggle-bio {
  background-color: #ff3d00;
  color: white;
  padding: 0.5rem 1.2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.top-section {
  background-color: #1f1f1f;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 2rem;
}

.top-section h2 {
  color: #ff3d00;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.top-columns {
  display: flex;
  align-items: stretch;
  gap: 1rem;
}

.top-discography, .top-collaborations {
  flex: 1;
}

.top-discography ul, .top-collaborations ul {
  list-style: none;
  padding: 0;
  margin-top: 0;
}

li {
  color: #ddd;
  margin-bottom: 0.5rem;
}

.divider {
  width: 1px;
  background-color: #555;
  height: auto;
  align-self: stretch;
}

.events {
  margin-top: 2rem;
  background-color: #1f1f1f;
  padding: 1rem;
  border-radius: 8px;
}

.events h2 {
  color: #ff3d00;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.events ul {
  list-style: none;
  padding: 0;
}

.events li {
  color: #ddd;
  margin-bottom: 0.5rem;
}
</style>
