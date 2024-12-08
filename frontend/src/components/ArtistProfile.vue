<template>
  <div class="perfil-artist">
    <!-- Fondo animado -->
    <div class="background-animation"></div>

    <div class="logo-link" @click="goHome">
      <img src="../assets/Im_logo.png" alt="Logo" class="logo" />
    </div>
    <header class="perfil-header">
      <div class="avatar-container">
        <img src="../assets/artistas/melendi.jpeg" alt="Avatar del artista" class="avatar" />
      </div>
      <div class="artist-details">
        <h1>{{ artistStageName }}</h1>
        <p class="genre">{{ genre }}</p>
        <p v-if="expandedBio" class="bio">{{ bio }}</p>
        <p v-else class="bio-short">{{ shortBio }}</p>
        <button class="btn" @click="toggleBio">
          {{ expandedBio ? 'Ver menos' : 'Ver más' }}
        </button>
      </div>
    </header>

    <section class="top-section">
      <div class="top-columns">
        <!-- Discografía Destacada -->
        <div class="top-discography">
          <h2 class="title-red">Discografía Destacada</h2>
          <ul>
            <li v-for="album in discography" :key="album.id">
              {{ album.title }} ({{ album.releaseYear }})
            </li>
          </ul>
        </div>

        <!-- Línea divisoria -->
        <div class="divider"></div>

        <div class="top-collaborations">
          <h2 class="title-red">Colaboraciones</h2>
          <ul>
            <li v-for="collab in collaborations" :key="collab.id">
              {{ collab.title }} - {{ collab.artist }}
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Eventos Cercanos -->
    <div class="events-container">
      <section class="events">
        <h2 class="title-red">Próximos Eventos</h2>
        <ul>
          <li v-for="event in upcomingEvents" :key="event.id">
            {{ event.name }} - {{ event.date }} - {{ event.location }}
          </li>
        </ul>
      </section>
    </div>
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
      shortBio: 'Artista de pop rock y rumba...',
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
    },
    goHome () {
      this.$router.push({path: '/home'})
    }
  }
}
</script>

<style scoped>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden;
}

/* Fondo animado */
.background-animation {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('../assets/fondo.png'); /* Reemplazar con la textura del fondo animado */
  background-size: cover;
  filter: brightness(50%);
  z-index: -1;
}

.perfil-artist {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  color: white;
  padding: calc(2vh + 4vw) 3vw 3vh;
  min-height: 100vh;
  overflow-y: auto;
  box-sizing: border-box;
}

.perfil-header {
  background: rgba(31, 31, 31, 0.9);
  color: white;
  padding: 3vh 3vw;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  border-radius: 1.2vw;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  margin-bottom: 3vh;
  width: 100%;
  position: relative;
}

/* Resto de los estilos */
.logo {
  width: 8vw;
  max-width: 50px;
  height: auto;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.1);
}

.avatar-container {
  margin-right: 2vw;
}

.avatar {
  width: 15vw;
  height: 15vw;
  border-radius: 50%;
  border: 0.3vw solid #ff3d00;
}

.artist-details {
  flex-grow: 1;
  max-width: 500px;
}

.artist-details h1 {
  font-size: 2.5rem;
  margin: 0;
}

.btn {
  background-color: #bf0000;
  padding: 1.5vh 2vw;
  border-radius: 2vw;
  color: white;
}

.btn:hover {
  background-color: #a30000;
}

.genre {
  color: #aaa;
  margin-top: 1vh;
}

.bio, .bio-short {
  margin-top: 2vh;
  font-size: 1rem;
}

.top-section {
  margin-top: 2vh;
  width: 100%;
  background-color: rgba(31, 31, 31, 0.9);
  padding: 2vh 2vw;
  border-radius: 1vw;
}

.top-columns {
  display: flex;
  gap: 2vw;
}

.top-discography, .top-collaborations {
  flex: 1;
}

.top-discography ul, .top-collaborations ul {
  list-style: none;
  padding: 0;
  margin-top: 0;
}

.logo-link {
  position: fixed;
  top: 1rem;
  left: 1rem;
  z-index: 1000;
  cursor: pointer;
}

li {
  color: #ddd;
  margin-bottom: 0.5rem;
}

.divider {
  width: 2px;
  background-color: #555;
  margin: 0 1vw;
}

.title-red {
  color: red;
}

.events {
  margin-top: 2vh;
  background-color: rgba(31, 31, 31, 0.9);
  padding: 2vh 2vw;
  border-radius: 1vw;
}

.events-container {
  width: 100%;
  padding: 0;
  margin: 0 auto;
  box-sizing: border-box;
}
</style>
