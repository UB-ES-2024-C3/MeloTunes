<template class="main">
  <div class="main-container">
    <div class="background-image"></div>
      <header>
        <div class="logo">
          <button @click="goHome" style="border: none; background: none;">
            <img src="../assets/logo2.png" alt="Logo" />
          </button>
        </div>
        <div class="search-bar">
          <input type="text" placeholder="Busca canciones, artistas" v-model="searchQuery" @keyup.enter="searchSong" />
          <button @click="goHome">
            <img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width: 2vw; vertical-align: middle;" />
            Buscar
          </button>
        </div>
      </header>

    <div>
      <div class="perfil">
        <div class="album">
          <img :src="getAlbumImage(album.title)" alt="Album Cover" class="album-img" />
        </div>

        <div class="information">
          <p class="album-info">{{ album.title }}</p>
          <p class="album-info">{{ album.artist }}</p>
          <p class="album-info">{{ getYear(album.timestamp) }}</p>
        </div>

        <div v-if="user_logged.is_superuser || isOwner" class="admin-controls">
          <button @click="openDeleteDialog" class="delete-button">Eliminar canción</button>
        </div>

        <v-dialog v-model="deleteDialog" max-width="500px">
          <v-card>
            <v-card-title class="headline">Confirmar eliminación</v-card-title>
            <v-card-text>
              ¿Estás seguro de que quieres eliminar esta canción?
            </v-card-text>
            <v-card-actions>
              <v-btn color="green" text @click="deleteSong">Sí</v-btn>
              <v-btn color="red" text @click="cancelDelete">No</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-app class="main-container">
          <v-btn color="black" @click="toggleDrawer" class="floating-btn" :class="{ mirrored: drawer }">
            <img src="../assets/avance-rapido.png" alt="Botón Imagen" height="40" width="40" />
          </v-btn>
        </v-app>
      </div>
    </div>

    <v-app class="main-container">
      <v-navigation-drawer v-model="drawer" app right persistent style="background-color: #212121; margin-top: 12vh" height="100vh" width="22vw">
        <v-list>
          <v-list-item v-for="song in album_songs" :key="song.id" @click="handleClick(song)">
            <v-list-item-content>
              <v-list-item-title class="item">
                <img :src="getAlbumImage(song.album)" alt="Portada del álbum" />
                <div class="item-info">
                  <p>{{ song.title }}</p>
                </div>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-app>
  </div>
</template>

<script>
import SongService from '../services/SongService'
import UserService from '../services/UserService'
import AlbumService from '../services/AlbumService'
export default {
  data () {
    return {
      all_songs: [],
      album_songs: [],
      album: {},
      album_id: 0,
      drawer: false, // Estado del drawer
      searchQuery: '',
      isOwner: false,
      deleteDialog: false
    }
  },
  mounted () {
    UserService.getAll().then(response => {
      this.user_logged = this.getUser(response.data.data, this.$route.query.email)
      this.album_id = this.$route.query.album
      AlbumService.get(this.album_id).then(response => {
        this.album = response.data
        SongService.getAll().then(response => {
          this.all_songs = response.data.data
          this.album_songs = this.all_songs.filter(song => song.album === this.album.title)
        })
      })
    })
  },
  methods: {
    toggleDrawer () {
      this.drawer = !this.drawer // Alterna el estado del drawer
    },
    getYear (timestamp) {
      const date = new Date(timestamp)
      return date.getFullYear()
    },
    removeAccents (str) {
      return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Elimina los acentos
    },
    getAlbumImage (album) {
      console.log(album)
      const sanitizedAlbum = this.removeAccents(album.toLowerCase().replace(/ /g, ''))
      return require(`@/assets/albumes/${sanitizedAlbum}.jpeg`)
    },
    handleClick (song) {
      const currentSongId = this.$route.query.song
      const targetSongId = song.id

      // Si el ID de la canción es el mismo que el actual, no realizamos la navegación
      if (currentSongId === targetSongId) {
        return
      }
      this.$router.push({
        path: '/song',
        query: {
          email: this.$route.query.email,
          logged: this.$route.query.logged,
          token: this.$route.query.token,
          song: song.id
        }
      })
      this.$router.go()
    },
    goHome () {
      localStorage.setItem('searchQuery', this.searchQuery)
      this.$router.push({
        path: '/home',
        query: {email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token}
      })
      this.$router.go()
    },
    getUser (usersList, email) {
      for (const user of usersList) {
        if (email === user.email) {
          return user
        }
      }
      return NaN
    },
    openDeleteDialog () {
      this.deleteDialog = true
    },
    cancelDelete () {
      this.deleteDialog = false
    },
    deleteSong () {
      /*
      // Backend: Eliminar la canción del backend
      SongService.deleteSong(this.song.id, this.user_logged.id).then(response => {
        console.log('Canción eliminada:', response)
        this.deleteDialog = false
        // Redirigimos a home después de eliminar la canción
        this.$router.push({
          path: '/home',
          query: {email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token}
        })
        this.$router.go()
      }).catch(error => {
        console.error('Error al eliminar la canción:', error)
        this.deleteDialog = false
      }) */
    }
  }
}
</script>

<style>
/* Ocultar scrollbars en navegadores que soporten esta regla */
::-webkit-scrollbar {
  display: none;
}

/* Estilos generales */
body {
  background-color: #000000;
  height: 100vh;
  margin: 0;
  font-family: Arial, sans-serif;
}

/* Contenedor principal */
.main-container, main {
  background-color: transparent !important;
  min-height: 100vh; /* Altura mínima de toda la vista */
  display: flex;
  flex-direction: column;
  padding-top: 15vh;
  padding-bottom: 5vh;
  position: relative;
}

/* Fondo de imagen fija */
.background-image {
  background: url('../assets/fondo.jpg') no-repeat center center fixed;
  background-size: cover;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  filter: brightness(0.7);
}

/* Cabecera */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 3vh 2vw;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.logo img {
  width: 3.5vw;
  margin-top: -2vh;
  margin-left: -1vw;
}

/* Barra de búsqueda */
.search-bar {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.search-bar input[type="text"] {
  width: 50vw;
  padding: 0.5vw;
  font-size: 1rem;
  border: none;
  border-radius: 20px;
  margin-right: 0.5%;
  outline: none;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
  background-color: white;
}

.search-bar button {
  width: 10vw;
  font-size: 1rem;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}

.search-bar button:hover {
  background-color: #ffffff;
}

.search-bar button img {
  width: 1.5vw;
  height: 3.5vh;
}

/* Perfil */
.perfil {
  height: 80vh;
  display: flex;
  padding: 2vw;
  margin-top: 5vh;
  flex-direction: column;
  align-items: flex-start;
}

/* Detalles de la canción */
.album {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 2vw;
  margin-bottom: 2vh;
}

.album img {
  width: 20vw;
  height: 40vh;
  object-fit: cover;
  border-radius: 10px;
}

.details {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.song-title {
  font-weight: bold;
  font-size: 3.5rem;
  color: white;
  margin: 0;
}

.song-author {
  color: #ffffff;
  font-size: 2rem;
  margin: 0;
}

.information {
  display: flex;
  flex-direction: column;
  gap: 0.5vh;
  font-size: 1.5rem;
  color: white;
}

/* Botón de reproducción */
.play-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  margin: 0;
}

.play-button img {
  width: 10vw;
  height: 10vh;
  object-fit: contain;
}

/* Botón flotante */
.floating-btn {
  position: fixed;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  background-color: transparent;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 1000;
  transition: transform 0.3s ease;
}

.floating-btn img {
  transform: scaleX(1);
  transition: transform 0.3s ease;
}

.floating-btn:hover img {
  transform: scaleX(-1);
}

.mirrored {
  transform: rotate(180deg);
  transition: transform 0.3s ease;
}

/* Botón de favoritos */
.favorite-btn-container {
  position: absolute;
  top: 80vh;
  right: 5vw;
  z-index: 1;
}

.favorite-btn-container i {
  font-size: 3rem;
  color: #ff0000;
  cursor: pointer;
}

/* Comentarios */
.comments-section {
  margin-top: 20px;
  color: white;
}

.comment-item {
  background-color: #333;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 8px;
}

.comment-input-container {
  margin-top: 20px;
}

.comment-input-container textarea {
  width: 100%;
  padding: 10px;
  background-color: #2c2c2c;
  color: white;
  border: none;
  border-radius: 8px;
  margin-bottom: 10px;
}

.comment-input-container button {
  padding: 10px;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.comment-input-container button:hover {
  background-color: #f44336;
}

/* Lista de canciones */
.v-navigation-drawer .v-list-item {
  color: #000000 !important;
}

.item {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 24vw;
  background-color: #1f1f1f;
  border-radius: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.item img {
  width: 5vw;
  height: 5vw;
  border-radius: 10px;
  margin-right: 0.2vw;
  object-fit: cover;
}

.item-info p {
  margin: 0.5vw;
  color: white;
  font-size: 1rem;
}

.item:hover {
  transform: scale(1.1);
  box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.5);
}

/* Botón de eliminar canción */
.delete-button {
  padding: 10px;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  width: 100%;
  margin-top: 10px;
}

.delete-button:hover {
  background-color: #f44336;
}

/* Estilo base para dispositivos móviles pequeños (pantallas hasta 480px de ancho) */
@media screen and (max-width: 480px) {

  /* Cabecera */
  header {
    padding: 2vh 2vw;
  }

  .logo img {
    width: 40vw; /* Ajuste de tamaño de logo en móvil */
  }

  /* Barra de búsqueda */
  .search-bar input[type="text"] {
    width: 60vw; /* Ajuste de tamaño para campo de búsqueda */
  }

  .search-bar button {
    width: 30vw; /* Botón de búsqueda más pequeño */
  }

  .search-bar button img {
    width: 12vw; /* Ajuste para el icono del botón */
  }

  /* Perfil */
  .perfil {
    padding: 4vw;
  }

  .album img {
    width: 45vw; /* Ajustar el tamaño de la imagen del álbum */
    height: 40vh;
  }

  .details {
    gap: 2vw;
  }

  .song-title {
    font-size: 2rem; /* Ajustar tamaño de texto en móvil */
  }

  .song-author {
    font-size: 1.3rem; /* Ajuste en el tamaño del autor */
  }

  .information {
    font-size: 1.1rem;
  }

  /* Botón de reproducción */
  .play-button img {
    width: 50vw; /* Ajuste del tamaño del botón de reproducción */
    height: 50vh;
  }

  /* Botón flotante */
  .floating-btn {
    width: 35px;
    height: 35px;
  }

  .floating-btn img {
    width: 20px;
    height: 20px;
  }

  /* Favoritos */
  .favorite-btn-container {
    top: 70vh;
    right: 5vw;
  }

  /* Comentarios */
  .comment-item {
    padding: 6px;
  }

  .comment-input-container textarea {
    padding: 6px;
  }

  .comment-input-container button {
    padding: 6px;
  }

  /* Lista de canciones */
  .item {
    flex-direction: column;
    width: 90vw;
    margin: 2vh 0;
  }

  .item img {
    width: 60vw;
    height: 60vw;
    margin-bottom: 8px;
  }

  .item-info p {
    font-size: 0.9rem;
  }

  .item:hover {
    transform: scale(1);
  }

  .delete-button {
    padding: 6px;
    font-size: 1.1rem;
  }
}

/* Dispositivos con pantallas medianas (entre 481px y 768px de ancho, tablets y teléfonos grandes) */
@media screen and (min-width: 481px) and (max-width: 768px) {

  /* Cabecera */
  header {
    padding: 3vh 3vw;
  }

  .logo img {
    width: 25vw;
  }

  /* Barra de búsqueda */
  .search-bar input[type="text"] {
    width: 65vw;
  }

  .search-bar button {
    width: 30vw;
  }

  .search-bar button img {
    width: 10vw;
  }

  /* Perfil */
  .perfil {
    padding: 3vw;
  }

  .album img {
    width: 35vw;
    height: 45vh;
  }

  .details {
    gap: 1.5vw;
  }

  .song-title {
    font-size: 2.5rem;
  }

  .song-author {
    font-size: 1.5rem;
  }

  .information {
    font-size: 1.2rem;
  }

  /* Botón de reproducción */
  .play-button img {
    width: 40vw;
    height: 40vh;
  }

  /* Botón flotante */
  .floating-btn {
    width: 45px;
    height: 45px;
  }

  .floating-btn img {
    width: 25px;
    height: 25px;
  }

  /* Favoritos */
  .favorite-btn-container {
    top: 60vh;
    right: 4vw;
  }

  /* Comentarios */
  .comment-item {
    padding: 8px;
  }

  .comment-input-container textarea {
    padding: 8px;
  }

  .comment-input-container button {
    padding: 8px;
  }

  /* Lista de canciones */
  .item {
    flex-direction: row;
    width: 85vw;
    margin: 2vh 0;
  }

  .item img {
    width: 40vw;
    height: 40vw;
  }

  .item-info p {
    font-size: 1rem;
  }

  .item:hover {
    transform: scale(1.05);
  }

  .delete-button {
    padding: 8px;
  }
}

</style>
