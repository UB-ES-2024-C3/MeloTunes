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
          <button class="btn" @click="toggleBio">
            {{ expandedBio ? 'Ver menos' : 'Ver más' }}
          </button>
        </div>
        <div class="btn-group">
          <button class="btn" @click="showFavorites = true">Ver mis favoritos</button>
          <router-link to="/addsong" class="btn"><span>Subir canción</span></router-link>
          <button class="btn" @click="showEditProfile = true">Modificar perfil</button>
        </div>
      </div>
    </header>

    <!-- Popup modal de favoritos -->
    <div v-if="showFavorites" class="modal-overlay">
      <div class="modal-content">
        <button class="close-button" @click="showFavorites = false">×</button>
        <h2>Mis Favoritos</h2>
        <ul v-if="fav_songs && fav_songs.length" class="favorites-list">
          <li v-for="favorite in fav_songs" :key="favorite.id" class="favorite-item">
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

    <!-- Modal para editar el perfil -->
    <div v-if="showEditProfile" class="modal-overlay">
      <div class="modal-content">
        <button class="close-button" @click="showEditProfile = false">×</button>
        <h2>Editar Perfil</h2>
        <form @submit.prevent="saveProfile">
          <div class="form-group">
            <label for="firstName">Nombre:</label>
            <input type="text" id="firstName" v-model="editProfile.first_name" />
          </div>
          <div class="form-group">
            <label for="secondName">Apellido:</label>
            <input type="text" id="secondName" v-model="editProfile.second_name" />
          </div>
          <div class="form-group">
            <label for="bio">Biografía:</label>
            <textarea id="bio" v-model="editProfile.bio"></textarea>
          </div>
          <button type="submit">Guardar</button>
        </form>
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
      showEditProfile: false,
      editProfile: {
        first_name: '',
        second_name: '',
        bio: ''
      },
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
      return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    },
    getAlbumImage (album) {
      console.log(album)
      const sanitizedAlbum = this.removeAccents(album.toLowerCase().replace(/ /g, ''))
      return require(`@/assets/albumes/${sanitizedAlbum}.jpeg`)
    }
  },
  uploadSong () {
    this.$router.push('/addsong')
  },
  saveProfile () {
    Object.assign(this.user_logged, this.editProfile)
    this.showEditProfile = false
    alert('Perfil actualizado con éxito')
  }
}
</script>

<style scoped>
.perfil {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  background-color: #121212;
  color: white;
  padding: calc(2vh + 6vw) 3vw 3vh;
  min-height: 100vh;
  overflow-y: auto;
  box-sizing: border-box;
}

.perfil-header {
  background: #1f1f1f;
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

 .btn {
   background-color: #bf0000;
   padding: 1.5vh 2vw;
   border-radius: 2vw;
   color: white;
   font-size: 1.2rem;
   text-decoration: none;
   display: flex;
   align-items: center;
   justify-content: center;
   border: none;
   cursor: pointer;
 }

.btn:hover {
  background-color: #a30000;
}

.logo-link {
  position: fixed;
  top: 2vh;
  left: 2vw;
  z-index: 10000;
  cursor: pointer;
}

.logo {
  width: 8vw;
  max-width: 50px;
  height: auto;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.1);
}

section {
  margin-top: 2vh;
  width: 100%;
  background-color: #1f1f1f;
  padding: 2vh 2vw;
  border-radius: 1vw;
  box-sizing: border-box;
}

.top-section {
  background-color: #1f1f1f;
  padding: 2vh 2vw;
  border-radius: 1vw;
  margin-top: 3vh;
  width: 100%;
}

.top-columns {
  display: flex;
  gap: 2vw;
  justify-content: space-between; /* Espacio entre los dos bloques */
}

.top-songs, .top-albums {
  flex: 1; /* Ambos bloques ocupan el mismo espacio */
  padding: 1vh 1vw;
  background-color: #333;
  border-radius: 1vw;
  color: white;
  box-sizing: border-box;
}

.top-songs h2, .top-albums h2 {
  color: #ff3d00;
  font-size: 2rem;
  margin-bottom: 1.5vh;
}

.top-songs ul, .top-albums ul {
  list-style: none;
  padding: 0;
}

.top-songs li, .top-albums li {
  color: #ddd;
  margin-bottom: 1vh;
}

.divider {
  width: 1px;
  background-color: #555;
  height: 100%;
  align-self: stretch; /* Hace que la barra divisora ocupe todo el alto */
}

.top-section h2 {
  color: #ff3d00;
  font-size: 2rem;
  margin-bottom: 2vh;
  text-align: center;
}

.recommendations-grid {
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  gap: 2vw;
}

.recommendation-column h3 {
  font-size: 1.8rem;
  color: #ff3d00;
  margin-bottom: 1.5vh;
}

.recommendation-column ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1vh;
}

.recommendation-column li {
  font-size: 1.2rem;
  color: #ddd;
}

.divider {
  width: 2px;
  background-color: #555;
  margin: 0 1vw;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8); /* Fondo translúcido oscuro */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999; /* Asegura que esté encima de todo */
}

.modal-content {
  background-color: #1f1f1f; /* Fondo gris oscuro */
  color: #ffffff; /* Texto blanco */
  padding: 3vh 3vw;
  border-radius: 1vw;
  width: 90%;
  max-width: 500px;
  box-sizing: border-box;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 2vh; /* Espaciado entre elementos */
}

.modal-content h2 {
  color: #ff3d00; /* Título en color destacado */
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

.modal-content .form-group {
  display: flex;
  flex-direction: column;
  gap: 1vh;
}

.modal-content .form-group label {
  color: #ff3d00;
  font-size: 1.2rem;
}

.modal-content .form-group input,
.modal-content .form-group textarea {
  background-color: #333; /* Fondo gris oscuro */
  color: #ffffff; /* Texto blanco */
  padding: 1rem;
  border: none;
  border-radius: 0.5vw;
  font-size: 1rem;
  width: 100%;
}

.modal-content button {
  background-color: #bf0000;
  color: #ffffff;
  padding: 1rem;
  border-radius: 0.5vw;
  font-size: 1.2rem;
  border: none;
  cursor: pointer;
}

.modal-content button:hover {
  background-color: #ff3d00;
}

.close-button {
  position: absolute;
  top: 1rem;
  right: 1rem;
  font-size: 1.5rem;
  color: #ffffff;
  background: none;
  border: none;
  cursor: pointer;
}

.modal-content::-webkit-scrollbar {
  width: 0.6vw;
  background-color: transparent;
}

.modal-content::-webkit-scrollbar-thumb {
  background-color: #333;
  border-radius: 10px;
}

.modal-content::-webkit-scrollbar-track {
  background-color: transparent;
}

.recommendation-column ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1vh;
}

.recommendation-column li {
  font-size: 1.2rem;
  color: #ddd;
}

.close-button {
  justify-content: flex-end;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Estilo base del body */
body {
  margin: 0;
  padding: 0;
  background-color: #1f1f1f; /* Fondo oscuro unificado */
  color: #f63b3b;
  font-family: 'Arial', sans-serif;
  min-height: 100vh; /* Asegura que ocupe toda la altura */
  overflow-x: hidden; /* Elimina el desplazamiento horizontal si es innecesario */
}

section {
  background-color: #1f1f1f; /* Fondo consistente con el body */
  padding: 2vh 2vw;
  width: 100%;
}

header, nav, footer {
  margin: 0;
  padding: 0;
  background-color: transparent; /* Elimina fondos que puedan causar problemas */
}

.avatar-container {
  flex-shrink: 0;
  margin-right: 2vw;
}

.avatar {
  width: 15vw;
  height: 15vw;
  border-radius: 50%;
  border: 0.3vw solid #ff3d00;
  object-fit: cover;
}

.user-details {
  flex-grow: 1;
  max-width: 50vw;
}

.user-details h1 {
  font-size: 2.5rem;
  margin: 0;
  font-weight: 700;
}

.location {
  color: #aaa;
  margin-top: 1vh;
}

.bio, .bio-short {
  margin-top: 2vh;
  font-size: 1rem;
  line-height: 1.5;
}

.btn-group {
  display: flex;
  gap: 2vw;
  margin-top: 2vh;
}

.music-recommendations,
.top-songs,
.top-albums,
.events {
  margin-top: 3vh;
  background-color: #1f1f1f;
  padding: 2vh 2vw;
  border-radius: 1vw;
  width: 100%;
}

.music-recommendations h2,
.top-songs h2,
.top-albums h2,
.events h2 {
  color: #ff3d00;
  font-size: 2rem;
  margin-bottom: 1.5vh;
}

.recommendations-grid {
  display: flex;
  gap: 2vw;
  flex-wrap: wrap;
}

.recommendation {
  background-color: #333;
  padding: 1vh;
  border-radius: 1vw;
  text-align: center;
}

.recommendation-cover {
  width: 100%;
  height: 15vw;
  border-radius: 1vw;
}

.music-stats ul,
.top-songs ul,
.events ul {
  list-style: none;
  padding: 0;
}

ul {
  margin-top: 1.5vh;
}

li {
  color: #ddd;
  font-size: 1rem;
  margin-bottom: 1vh;
}

.favorites-list {
  max-height: 40vh;
  overflow-y: auto;
}

.favorite-item {
  display: flex;
  justify-content: space-between;
  margin: 1vh 0;
}

.favorite-cover {
  width: 40px;
  height: 40px;
  object-fit: cover;
}

.favorite-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.divider {
  width: 1px;
  background-color: #ff3d00;
  margin: 0 3vw;
}

</style>
