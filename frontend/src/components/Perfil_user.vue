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
          <router-link to="/addsong" class="btn-upload-song"><span>Subir canción</span></router-link>
          <button class="btn-modificar-perfil" @click="showEditProfile = true">Modificar perfil</button>
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
          <button type="submit" class="btn-save">Guardar</button>
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
  padding: 3vh 3vw;
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
  max-height: 50vh; /* Limita la altura */
  overflow: auto; /* Permite el scroll si el contenido excede el espacio */
  padding-right: 10px;
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

.btn-toggle-bio {
  background-color: #ff3d00;
  color: white;
  padding: 1vh 2vw;
  border: none;
  border-radius: 1vw;
  cursor: pointer;
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
  width: 10vw;
  height: 10vw;
  object-fit: cover;
  border-radius: 1vw;
}

.top-columns {
  display: flex;
  justify-content: space-between;
}

.top-songs,
.top-albums {
  width: 48%;
}

.divider {
  width: 1px;
  background-color: #ddd;
  margin: 0 2vw;
}

.favorite-item {
  display: flex;
  gap: 1vw;
  margin-bottom: 2vh;
  align-items: center;
}

.favorite-cover {
  width: 5vw;
  height: 5vw;
  object-fit: cover;
  border-radius: 10%;
}

.favorite-details {
  flex-grow: 1;
}

.song-duration {
  font-size: 1rem;
  color: #ff3d00;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 2vw;
  border-radius: 1.5vw;
  max-width: 80%;
  max-height: 80%;
  overflow-y: auto;
  color: #333;
}

.close-button {
  background-color: transparent;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  position: absolute;
  top: 1vh;
  right: 1vw;
  color: #ff3d00;
}

.favorites-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.favorite-item {
  display: flex;
  align-items: center;
  margin-bottom: 2vh;
}

.favorite-cover {
  width: 8vw;
  height: 8vw;
  object-fit: cover;
  border-radius: 8%;
  margin-right: 1.5vw;
}

.favorite-details {
  display: flex;
  flex-direction: column;
}

.favorite-details h3 {
  font-size: 1.5rem;
  margin: 0;
}

.favorite-details p {
  font-size: 1.2rem;
  color: #555;
}

.song-duration {
  font-size: 1rem;
  color: #ff3d00;
}

.btn-upload-song, .btn-modificar-perfil, .btn-favoritos {
  background-color: #ff3d00;
  color: white;
  padding: 1.2vh 3vw;
  border: none;
  border-radius: 1.5vw;
  cursor: pointer;
  text-decoration: none;
  font-size: 1.1rem;
}

.btn-upload-song {
  text-align: center;
}

.btn-favoritos {
  background-color: #222;
}

.btn-modificar-perfil {
  background-color: #444;
}

.btn-group button:hover {
  background-color: #e15c00;
}

.btn-toggle-bio:hover {
  background-color: #e15c00;
}

form {
  display: flex;
  flex-direction: column;
  gap: 2vh;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 1vh;
}

label {
  font-size: 1.2rem;
}

input[type="text"], textarea {
  padding: 1vh;
  border-radius: 1vw;
  border: 1px solid #ddd;
  background-color: #f9f9f9;
  font-size: 1rem;
}

textarea {
  resize: vertical;
  min-height: 5vh;
}

.btn-save {
  background-color: #ff3d00;
  color: white;
  padding: 1.5vh 3vw;
  border: none;
  border-radius: 1.5vw;
  cursor: pointer;
  font-size: 1.2rem;
}

.btn-save:hover {
  background-color: #e15c00;
}

@media (max-width: 768px) {
.perfil-header {
  flex-direction: column;
  align-items: center;
}

.avatar {
  width: 30vw;
  height: 30vw;
}

.user-details {
  max-width: 100%;
}

.top-columns {
  flex-direction: column;
}

.top-songs,
.top-albums {
  width: 100%;
}

.divider {
  display: none;
}
}
</style>
