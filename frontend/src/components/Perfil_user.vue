<template>
  <div class="perfil">
    <div class="logo-link" @click="goHome">
      <img src="../assets/Im_logo.png" alt="Logo" class="logo" />
    </div>
    <header class="perfil-header">
      <div class="avatar-container">
        <div v-if="this.user_logged.is_artist">
          <img :src="getArtistImage(this.user_logged.artist_name)" alt="Avatar del usuario" class="avatar" />
        </div>
        <div v-if="!this.user_logged.is_artist">
          <img src="../assets/user.png" alt="Avatar del usuario" class="avatar" />
        </div>
      </div>
      <div class="user-details">
        <h1 v-if="!this.user_logged.is_artist">{{ this.user_logged.first_name }} {{ this.user_logged.second_name }}</h1>
        <h4 v-if="!this.user_logged.is_artist">{{ this.user_logged.email }}</h4>
        <h1 v-if="this.user_logged.is_artist">{{ this.user_logged.artist_name }}</h1>
        <p class="location" v-if="this.user_logged.is_artist">{{ location }}</p>
        <div v-if="this.user_logged.is_artist">
          <p v-if="expandedBio" class="bio">{{ this.user_logged.description }}</p>
          <p v-else class="bio-short">{{ truncatedDescription }}</p>
          <button class="btn-toggle-bio" @click="toggleBio">
            {{ expandedBio ? 'Ver menos' : 'Ver más' }}
          </button>
        </div>
        <div class="btn-group">
          <button class="btn" @click="showFavorites = true">Ver mis favoritos</button>
          <button class="btn" v-if="this.user_logged.is_artist" @click="showSongs = true">Ver mis canciones</button>
          <button v-if="this.user_logged.is_artist" class="btn" @click="uploadSong">
            Subir canción
          </button>
          <button class="btn" @click="showEditProfile = true">Modificar perfil</button>
        </div>
      </div>
    </header>

    <!-- Popup modal de canciones -->
    <div v-if="showSongs" class="modal-overlay">
      <div class="modal-content">
        <button class="close-button" @click="showSongs = false">×</button>
        <h2>Mis Canciones</h2>
        <ul v-if="this.my_songs && this.my_songs.length" class="favorites-list">
          <li v-for="uploaded_song in this.my_songs" :key="uploaded_song.id" class="favorite-item" @click="handleClick(uploaded_song)">
            <a :href="uploaded_song.cover" target="_blank" rel="noopener noreferrer">
              <img :src="getAlbumImage(uploaded_song.album)" alt="Cover Image" class="favorite-cover" style="width: 10vw; height: 10vh"/>
            </a>
            <div class="favorite-details">
              <h3>{{ uploaded_song.title }}</h3>
              <p>{{ uploaded_song.artist }}</p>
              <span class="song-duration">{{ getYear(uploaded_song.timestamp) }}</span>
            </div>
          </li>
        </ul>
        <p v-else>No tienes canciones aún.</p>
      </div>
    </div>

    <!-- Popup modal de favoritos -->
    <div v-if="showFavorites" class="modal-overlay">
      <div class="modal-content">
        <button class="close-button" @click="showFavorites = false">×</button>
        <h2>Mis Favoritos</h2>
        <ul v-if="fav_songs && fav_songs.length" class="favorites-list">
          <li v-for="favorite in fav_songs" :key="favorite.id" class="favorite-item" @click="handleClick(favorite)">
            <a :href="favorite.cover" target="_blank" rel="noopener noreferrer">
              <img :src="getAlbumImage(favorite.album)" alt="Cover Image" class="favorite-cover" style="width: 10vw; height: 10vh" />
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
        <form>
          <div class="form-group">
            <label for="firstName">Nombre:</label>
            <input type="text" id="firstName" v-model="editProfile.firstName" />
          </div>
          <div class="form-group">
            <label for="secondName">Apellido:</label>
            <input type="text" id="secondName" v-model="editProfile.secondName" />
          </div>
          <div v-if="this.user_logged.is_artist" class="form-group">
            <label for="bio">Biografía:</label>
            <textarea id="bio" v-model="editProfile.bio"></textarea>
          </div>
          <button class="btn-save" @click="enviarModificacion">Guardar</button>
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
import vertigoCover from '../assets/albumes/antesdequecuentediez.jpeg'
import lagrimasCover from '../assets/albumes/lagrimasdesordenadas.jpeg'
import sinFronterasCover from '../assets/albumes/estopa1.jpeg'
import SongService from '../services/SongService'

export default {
  name: 'Perfil_user',
  mounted () {
    UserService.getAll().then(response => {
      this.user_logged = this.getUser(response.data.data, this.$route.query.email)
      UserService.getMyFavouriteSongs(this.user_logged.id).then(response => {
        this.fav_songs = response
        if (this.user_logged.artist_name) {
          SongService.getAllArtist(this.user_logged.artist_name).then(response => {
            this.my_songs = response.data.data
            console.log(this.my_songs)
          })
        }
      })
    })
  },
  computed: {
    truncatedDescription () {
      return this.user_logged.description.length > 20
        ? this.user_logged.description.substring(0, 20) + '...'
        : this.user_logged.description
    }
  },
  data () {
    return {
      user_logged: {},
      fav_songs: [],
      my_songs: [],
      location: 'Barcelona',
      expandedBio: false,
      showFavorites: false,
      showSongs: false,
      showEditProfile: false,
      editProfile: {
        first_name: '',
        second_name: '',
        bio: ''
      },
      musicRecommendations: [
        { id: 1, title: 'Antes de que cuente 10', artist: 'Fito y Fitipaldis', cover: vertigoCover },
        { id: 2, title: 'Lágrimas desordenadas', artist: 'Melendi', cover: lagrimasCover },
        { id: 3, title: 'Paseo', artist: 'Estopa', cover: sinFronterasCover }
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
    },
    uploadSong () {
      this.$router.push({ path: '/addsong', query: {email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token} })
      this.$router.go()
    },
    saveProfile () {
      Object.assign(this.user_logged, this.editProfile)
      this.showEditProfile = false
      alert('Perfil actualizado con éxito')
    },
    getArtistImage (artist) {
      const sanitizedArtist = this.removeAccents(artist.toLowerCase().replace(/ /g, ''))
      return require(`@/assets/artistas/${sanitizedArtist}.jpeg`)
    },
    enviarModificacion () {
      this.showEditProfile = false
      UserService.updateUser(this.user_logged.id, this.editProfile.firstName, this.editProfile.secondName, this.editProfile.bio)
        .then(() => {
          this.$router.push({ path: '/perfil_user', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token } })
          this.$router.go()
        })
        .catch((error) => {
          console.error(error)
          alert('Algo ha fallado')
        })
    },
    getUser (usersList, email) {
      for (const user of usersList) {
        if (email === user.email) {
          return user
        }
      }
      return NaN
    },
    handleClick (song) {
      this.$router.push({ path: '/song', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token, song: song.id } })
      this.$router.go()
    }
  }
}
</script>

<style scoped>
.perfil {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  background-image: url('../assets/fondo.jpg'); /* Ruta a tu imagen de fondo */
  background-size: cover; /* Hace que la imagen cubra toda la pantalla */
  background-position: center; /* Centra la imagen */
  background-repeat: no-repeat; /* Evita que la imagen se repita */
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
  background-color: #f32121; /* Un rojo vibrante */
  color: white; /* Texto blanco para contraste */
  padding: 10px 1px; /* Reducir el padding horizontal */
  border: none; /* Sin borde */
  border-radius: 5px; /* Bordes redondeados */
  font-size: 17px; /* Tamaño de fuente legible */
  font-weight: bold; /* Texto destacado */
  cursor: pointer; /* Cambia el cursor al pasar el mouse */
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra sutil */
  transition: all 0.3s ease-in-out; /* Transición suave para los efectos */
}

.btn:hover {
  background-color: #d62828; /* Rojo más oscuro al pasar el mouse */
  box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.2); /* Más sombra */
}

.btn:active {
  transform: scale(0.95); /* Efecto de pulsación */
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
  background-color: #ce6c6c;
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
  font-size: 1rem;
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
  width: 25vw;
  box-sizing: border-box;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0.5vh; /* Espaciado entre elementos */
}

.modal-content h2 {
  color: #ff3d00; /* Título en color destacado */
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

.modal-content .form-group {
  display: flex;
  flex-direction: row;
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
  max-height: 100vh;
  margin: 0;
  padding: 0;
  list-style: none;
}

.favorite-item {
  display: flex;
  justify-content: space-between;
  gap: 1vw; /* Añade un pequeño espacio entre la imagen y el texto */
  padding: 0.5vh 0;
}
.favorite-item a {
  margin: 0;
  padding: 0;
  display: inline-block;
}

.favorite-cover {
  width: 70vw;
  margin-right: 0;
}

.favorite-details {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
  margin-left: 0;
}
.favorite-details h3 {
  font-size: 1.2rem;
  text-align: left;
  margin: 0;
}
.favorite-details h3, .favorite-details p, .favorite-details .song-duration {
  margin: 0; /* Elimina márgenes predeterminados */
}

@media (max-width: 768px) {
  .perfil {
    padding: 5vw 3vw;
  }

  .perfil-header {
    flex-direction: column;
    align-items: center;
    padding: 5vw 3vw;
    text-align: center;
  }

  .avatar {
    width: 30vw;
    height: 30vw;
  }

  .user-details {
    margin-top: 2vh;
  }

  .btn-group {
    display: flex;
    flex-direction: column;
    gap: 1vh;
    width: 100%;
  }

  .btn {
    width: 100%;
    font-size: 14px;
  }

  .top-columns {
    flex-direction: column;
    gap: 2vh;
  }

  .top-songs, .top-albums {
    width: 100%;
  }

  .divider {
    display: none;
  }

  .recommendations-grid {
    flex-direction: column;
    gap: 3vh;
  }

  .modal-content {
    padding: 4vw;
    max-width: 90%;
    gap: 3vh;
  }

  .modal-content button {
    font-size: 1rem;
    padding: 0.8rem;
  }

  .modal-content .form-group input,
  .modal-content .form-group textarea {
    font-size: 0.9rem;
    padding: 0.8rem;
  }

  .music-recommendations {
    padding: 3vw;
  }

  .events ul {
    padding-left: 0;
  }
}

</style>
