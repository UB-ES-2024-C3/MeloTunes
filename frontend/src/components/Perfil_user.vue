<template>
  <div class="perfil">
    <div class="logo-link" @click="goHome">
      <img src="../assets/Im_logo.png" alt="Logo" class="logo" />
    </div>
    <header class="perfil-header">
      <div class="avatar-container">
        <img src="../assets/facebook.png" alt="Avatar del usuario" class="avatar" />
      </div>
      <div class="user-details">
        <h1>{{ this.user_logged.first_name }} {{ this.user_logged.second_name }}</h1>
        <h4>{{ this.user_logged.email }}</h4>
        <p class="location" v-if="this.user_logged.isArtist">{{ location }}</p>
        <div v-if="this.user_logged.isArtist">
          <p v-if="expandedBio" class="bio">{{ bio }}</p>
          <p v-else class="bio-short">{{ shortBio }}</p>
          <button class="btn-toggle-bio" @click="toggleBio">
            {{ expandedBio ? 'Ver menos' : 'Ver más' }}
          </button>
        </div>
        <div class="btn-group">
          <button class="btn-favoritos" @click="showFavorites = true">Ver mis favoritos</button>
          <router-link to="/addsong" class="btn-upload-song"><span>Subir canción (+)</span></router-link>
        </div>
      </div>
    </header>

    <!-- Popup modal de favoritos -->
    <div v-if="showFavorites" class="modal-overlay">
      <div class="modal-content">
        <button class="close-button" @click="showFavorites = false">×</button>
        <h2>Mis Favoritos</h2>
        <ul v-if="this.fav_songs && this.fav_songs.length" class="favorites-list">
          <li v-for="favorite in this.fav_songs" :key="favorite.id" class="favorite-item">
            <a :href="favorite.cover" target="_blank" rel="noopener noreferrer">
              <img :src="getAlbumImage(favorite.album)" alt="Cover Image" class="favorite-cover" />
            </a>
            <div class="favorite-details">
              <h3>{{ favorite.title }}</h3>
              <p>{{ favorite.artist }}</p>
              <span class="song-duration">{{ getYear(favorite.timestamp) }}</span>
            </div>
          </li>
        </ul>
        <p v-else>No tienes favoritos aún.</p>
      </div>
    </div>

    <!-- Sección Top Canciones y Álbumes en columnas con línea divisoria -->
    <section class="top-section">
      <div class="top-columns">
        <!-- Top 3 Canciones -->
        <div class="top-songs">
          <h2>MI TOP 3 CANCIONES</h2>
          <ul>
            <li v-for="song in fav_songs.slice(0, 3)" :key="song.id">{{ song.title }} - {{ song.artist }}</li>
          </ul>
        </div>

        <!-- Línea divisoria -->
        <div class="divider"></div>
        <!-- Top 3 Álbumes -->
        <div class="top-albums">
          <h2>MI TOP 3 ÁLBUMES</h2>
          <ul>
            <li v-for="song in fav_songs.slice(0, 3)" :key="song.id">{{ song.album }} - {{ song.artist }}</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Recomendaciones Musicales -->
    <section class="music-recommendations">
      <h2>Recomendaciones Musicales</h2>
      <div class="recommendations-grid">
        <div v-for="recommendation in musicRecommendations" :key="recommendation.id" class="recommendation">
          <img :src="recommendation.cover" alt="Portada recomendada" class="recommendation-cover" />
          <p>{{ recommendation.title }} - {{ recommendation.artist }}</p>
        </div>
      </div>
    </section>

    <!-- Eventos y Conciertos Cercanos -->
    <section class="events">
      <h2>Eventos y Conciertos</h2>
      <ul>
        <li v-for="event in upcomingEvents" :key="event.id">{{ event.name }} - {{ event.date }} - {{ event.location }}</li>
      </ul>
    </section>
  </div>
</template>

<script>
import UserService from '../services/UserService'
import vertigoCover from '../assets/facebook.png'
import lagrimasCover from '../assets/instagram.png'
import sinFronterasCover from '../assets/twitter.png'

export default {
  name: 'Perfil_user',
  mounted () {
    UserService.get().then(response => {
      this.user_logged = response.data
      console.log(response.data)
    })
    UserService.getMyFavouriteSongs().then(response => {
      this.fav_songs = response
      console.log(response)
    })
  },
  data () {
    return {
      user_logged: {},
      fav_songs: [],
      location: 'Barcelona',
      bio: 'Amante de la música rock y pop. ...',
      shortBio: 'Amante de la música r...',
      expandedBio: false,
      showFavorites: false,
      musicRecommendations: [
        { id: 1, title: 'Vértigo', artist: 'Pablo Alborán', cover: vertigoCover },
        { id: 2, title: 'Lágrimas desordenadas', artist: 'Melendi', cover: lagrimasCover },
        { id: 3, title: 'Sin fronteras', artist: 'Luis Fonsi', cover: sinFronterasCover }
      ],
      upcomingEvents: [
        { id: 1, name: 'Concierto de Melendi', date: '15 de diciembre', location: 'Girona' },
        { id: 2, name: 'Festival de Pop español', date: '23 de noviembre', location: 'Palau Sant Jordi, Barcelona' }
      ]
    }
  },
  methods: {
    toggleBio () {
      this.expandedBio = !this.expandedBio
    },
    getYear (timestamp) {
      const date = new Date(timestamp)
      return date.getFullYear()
    },
    goHome () {
      this.$router.push({ path: '/home', query: {email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token} })
      this.$router.go()
    },
    removeAccents (str) {
      return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Elimina los acentos
    },
    getAlbumImage (album) {
      console.log(album)
      const sanitizedAlbum = this.removeAccents(album.toLowerCase().replace(/ /g, ''))
      return require(`@/assets/albumes/${sanitizedAlbum}.jpeg`)
    }
  },
  uploadSong () {
    this.$router.push('/addsong')
  }
}
</script>

<style scoped>
.perfil {
  background-color: #121212;
  color: white;
  padding: 2rem;
  min-height: 100vh;
}

.perfil-header {
  background: #1f1f1f;
  color: white;
  padding: 2rem;
  display: flex;
  align-items: center;
  justify-content: flex-start; /* Alineamos a la izquierda */
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

.user-details {
  flex-grow: 1;
  max-width: 500px;
}

.user-details h1 {
  font-size: 2rem;
  margin: 0;
  font-weight: 700;
}

.location {
  color: #aaa;
  margin-top: 0.5rem;
}

.bio, .bio-short {
  margin-top: 1rem;
  font-size: 1rem;
}

/* Botones de Ver mis favoritos y Subir canción */
.btn-group {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.btn-toggle-bio {
  background-color: #ff3d00;
  color: white;
  padding: 0.5rem 1.2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.music-recommendations,
.top-songs,
.top-albums,
.events {
  margin-top: 2rem;
  background-color: #1f1f1f;
  padding: 1rem;
  border-radius: 8px;
}

.music-recommendations h2,
.top-songs h2,
.top-albums h2,
.events h2 {
  color: #ff3d00;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.recommendations-grid {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.recommendation {
  background-color: #333;
  padding: 0.5rem;
  border-radius: 8px;
  text-align: center;
}

.recommendation-cover {
  width: 100%;
  height: 200px;
  border-radius: 8px;
}

.music-stats ul,
.top-songs ul,
.events ul {
  list-style: none;
  padding: 0;
}

ul {
  margin-top: 1rem;
}

li {
  color: #ddd;
}

.top-songs ul,
.top-albums ul {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.album-info p,
.song-info p {
  font-size: 1rem;
  color: #ff3d00;
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
  gap: 2rem;
}

.top-songs, .top-albums {
  flex: 1;
}

.top-songs ul, .top-albums ul {
  list-style: none;
  padding: 0;
  margin-top: 0;
}

li {
  color: #ddd;
  margin-bottom: 0.5rem;
}

/* Estilos para Top Canciones y Álbumes en columnas con línea divisoria */
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
  align-items: stretch; /* Asegura que las columnas tengan la misma altura */
  gap: 1rem;
}

.top-songs, .top-albums {
  flex: 1;
}

.top-songs h3, .top-albums h3 {
  color: #ff3d00;
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
}

.top-songs ul, .top-albums ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  color: #ddd;
  margin-bottom: 0.5rem;
}

.btn-favoritos, .btn-upload-song {
  background-color: #ff3d00;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  text-decoration: none;
  margin-top: 2rem;
  display: inline-block;
  font-weight: bold;
}

.btn-group {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

/* Línea divisoria entre las columnas */
.divider {
  width: 1px;
  background-color: #555; /* Color gris */
  height: auto;
  align-self: stretch; /* Extiende la línea para abarcar la altura completa */
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: #333;
  color: white;
  padding: 1rem;
  border-radius: 10px;
  max-width: 400px; /* Tamaño reducido */
  max-height: 70%; /* Ajustar la altura del modal */
  overflow: hidden; /* Elimina la barra de desplazamiento */
  position: relative;
}

.modal-content::-webkit-scrollbar {
  width: 6px; /* Ajusta el tamaño de la barra */
  background-color: transparent; /* Fondo transparente */
}

.modal-content::-webkit-scrollbar-thumb {
  background-color: #333; /* Barra de desplazamiento negra */
  border-radius: 10px;
}

.modal-content::-webkit-scrollbar-track {
  background-color: transparent; /* Fondo transparente del track */
}

.modal-content {
  overflow-y: auto; /* Habilita el desplazamiento vertical */
  -webkit-overflow-scrolling: touch; /* Desplazamiento suave */
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 1.5rem;
  color: #ff3d00;
  background: none;
  border: none;
  cursor: pointer;
}

h2 {
  color: #ff3d00;
}

.favorites-list {
  list-style: none;
  padding: 0;
  margin-top: 1rem;
}

.favorite-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.favorite-cover {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  object-fit: cover;
  margin-right: 1rem;
}

.favorite-details h3 {
  margin: 0;
  font-size: 1.2rem;
}

.favorite-details p, .song-duration {
  color: #aaa;
}

.song-duration {
  color: #ff3d00;
}

.logo-link {
  display: inline-block;
  margin-bottom: 2rem; /* Espacio entre el logo y el contenido */
}

/* Estilo para el logo */
.logo {
  width: 60px;  /* Ajusta el tamaño del logo */
  height: auto;
  cursor: pointer;
  transition: transform 0.3s ease;  /* Para efecto de hover */
}

.logo:hover {
  transform: scale(1.1);  /* Efecto de hover (agranda el logo ligeramente) */
}
</style>
