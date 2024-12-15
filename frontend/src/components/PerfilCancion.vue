<template class="main">
  <div class="main-container background-image">
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
          <img :src="getAlbumImage(song.album)" alt="Album Cover" class="album-img" />

          <div class="details">
            <p class="song-title">{{ song.title }}</p>
            <p class="song-author">{{ song.artist }}</p>
            <button class="play-button" @click="playAudio">
              <img :src="isPlaying ? require('../assets/pausa.png') : require('../assets/play.png')" style="width: 10vw; height: 10vh; object-fit: contain;" />
            </button>
          </div>
        </div>

        <div class="information">
          <p class="album-info">{{ song.album }}</p>
          <p class="album-info">{{ getYear(song.timestamp) }}</p>
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

        <div class="favorite-btn-container" v-if="this.user_logged">
          <i :class="isFavorited ? 'fas fa-heart' : 'far fa-heart'" @click="addFavorites" style="cursor: pointer; font-size: 24px; color: #ff0000;"></i>
        </div>
      </div>

      <div v-if="comments.length > 0" class="comments-section">
        <h3>Comentarios:</h3>
        <div v-for="comment in comments" :key="comment.id" class="comment-item">
          <p><strong>{{ comment.user }}</strong>: {{ comment.text }}</p>
          <button v-if="comment.user === currentUser || user_logged.is_superuser" @click="deleteComment(comment.id)" style="background: red; color: white; border: none; border-radius: 5px; cursor: pointer; padding: 5px;">
            Eliminar
          </button>
        </div>
      </div>

      <div v-if="user_logged" class="comment-input-container">
        <textarea v-model="newComment" placeholder="Escribe un comentario..." rows="4"></textarea>
        <button @click="postComment">Comentar</button>
      </div>
    </div>

    <v-app class="main-container">
      <v-navigation-drawer v-model="drawer" app right persistent style="background-color: #212121; margin-top: 12vh" height="100vh" width="22vw">
        <v-list>
          <v-list-item v-for="song in artist_songs" :key="song.id" @click="handleClick(song)">
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
import CommentService from '../services/CommentService'
import SongService from '../services/SongService'
import UserService from '../services/UserService'
export default {
  data () {
    return {
      all_songs: [],
      artist_songs: [],
      song: {},
      user_logged: {},
      song_id: 0,
      drawer: false, // Estado del drawer
      isFavorited: false,
      searchQuery: '',
      audio: null,
      isPlaying: false,
      comments: [], // Lista de comentarios
      newComment: '', // Texto del nuevo comentario
      currentUser: 'Usuario', // DIANA: Cambiar por el usuario, este es para probar
      isOwner: false,
      deleteDialog: false
    }
  },
  mounted () {
    UserService.getAll().then(response => {
      this.user_logged = this.getUser(response.data.data, this.$route.query.email)
      this.song_id = this.$route.query.song
      SongService.get(this.song_id).then(response => {
        this.song = response.data
        SongService.getAll().then(response => {
          this.all_songs = response.data.data
          this.artist_songs = this.all_songs.filter(song => song.artist === this.song.artist)
          this.loadComments()
        })
        if (this.user_logged) {
          this.checkIfFavorite()
        }
      })
      this.audio = new Audio(require(`@/assets/canciones/${this.artist.toLowerCase()}_${this.song.title.toLowerCase()}.mp3`))
      this.audio.addEventListener('ended', () => {
        this.isPlaying = false
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
    addFavorites () {
      if (!this.isFavorited) {
        UserService.addToFavoriteSongs(this.song_id, this.user_logged.id).then(response => {
          console.log(response)
          this.isFavorited = true
          alert(response.message)
        })
      } else {
        UserService.deleteOfFavoriteSongs(this.song_id, this.user_logged.id).then(response => {
          console.log(response)
          this.isFavorited = false
          alert(response.message)
        })
      }
    },
    checkIfFavorite () {
      UserService.getMyFavouriteSongs(this.user_logged.id).then(response => {
        const favorites = response // Asumiendo que la API devuelve un arreglo de canciones favoritas
        console.log(favorites)
        this.isFavorited = favorites.some(fav => Number(fav.id) === Number(this.song_id))
        console.log(this.isFavorite)
      })
    },
    loadComments () {
      // Simulamos la carga de comentarios
      // DIANA: Llamada a la API para obtener los comentarios de la canción
      CommentService.getAllSong(this.song.title).then(response => {
        this.comments = response.data.data
      })
    },
    postComment () {
      if (this.newComment.trim() !== '') {
        console.log(this.newComment)
        // Agregar comentario al backend
        CommentService.createComment(this.newComment, this.user_logged.first_name, this.song.title).then(response => {
          this.comments.push({ id: Date.now(), user: this.user_logged.first_name, text: this.newComment })
          this.newComment = '' // Limpiar el campo de comentario después de enviar
        })
      }
    },
    deleteComment (commentId) {
      // Encuentra el índice del comentario
      const index = this.comments.findIndex((comment) => comment.id === commentId)
      if (index !== -1) {
        CommentService.deleteComment(commentId).then(response => {
          this.comments.splice(index, 1)
        })
        console.log(`Comentario con ID ${commentId} eliminado.`)
      }
    },
    playAudio () {
      if (this.audio) {
        if (this.isPlaying) {
          // Si ya está reproduciendo, pausa el audio
          this.audio.pause()
          this.isPlaying = false
        } else {
          // Si está pausado o no ha comenzado, reproduce el audio
          this.audio.play()
          this.isPlaying = true

          // Detecta cuándo termina la canción para actualizar el estado
          this.audio.addEventListener('ended', () => {
            this.isPlaying = false
          })
        }
      } else {
        // Carga y reproduce el audio si no existe
        const sanitizedArtist = this.removeAccents(
          this.song.artist.toLowerCase().replace(/ /g, '')
        )
        const sanitizedTitle = this.removeAccents(
          this.song.title.toLowerCase().replace(/ /g, '')
        )

        try {
          this.audio = new Audio(
            require(`@/assets/canciones/${sanitizedArtist}_${sanitizedTitle}.mp3`)
          )
          this.audio.play()
          this.isPlaying = true

          // Detecta cuándo termina la canción
          this.audio.addEventListener('ended', () => {
            this.isPlaying = false
          })
        } catch (e) {
          console.error('Archivo de audio no encontrado:', e)
          alert('No se encontró el archivo de audio para esta canción.')
          this.isPlaying = false
        }
      }
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
      })
    }
  }
}
</script>

<style>

::-webkit-scrollbar {
  display: none;
}

.main-container, main {
  background-color: transparent !important;
  min-height: 100vh; /* Asegura que el contenedor tenga al menos la altura de la ventana */
  display: flex;
  flex-direction: column;
  padding-top: 15vh;
  padding-bottom: 5vh;
  position: relative;
}

.v-navigation-drawer .v-list-item {
  color: #000000 !important;
}

/* Estilo para el botón flotante */
.floating-btn {
  position: fixed; /* Posiciona el botón de forma fija */
  top: 50%; /* Centrado verticalmente */
  right: 0; /* Pegado al lado derecho */
  transform: translateY(-50%); /* Ajusta el centrado vertical */
  width: 50px; /* Ajusta el tamaño según sea necesario */
  height: 50px;
  background-color: transparent; /* Fondo transparente */
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 1000; /* Asegúrate de que esté sobre otros elementos */
  transition: transform 0.3s ease; /* Transición suave */
}
.floating-btn img {
  transform: scaleX(1); /* Estado inicial de la imagen */
  transition: transform 0.3s ease; /* Asegura la transición al volver */
}

/* Estilo para mover el botón hacia la izquierda cuando el drawer está abierto */
.floating-btn:hover, .floating-btn:focus {
  box-shadow: none;
  outline: none;
  background: transparent;
}

.floating-btn:active {
  outline: none;
  box-shadow: none;
  background-color: transparent;
}

body {
  background-color: #000000;
  height: 100vh;
}

.background-image {
  background: url('../assets/fondo.jpg') no-repeat center center fixed; /* Imagen de fondo centrada */
  background-size: cover; /* Asegura que la imagen cubra toda la pantalla */
  position: fixed; /* Mantiene el fondo fijo mientras haces scroll */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%; /* Se asegura de cubrir toda la altura de la ventana */
  z-index: -1; /* Mantiene el fondo detrás de todo el contenido */
  filter: brightness(0.7); /* Oscurece la imagen */
}

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

/* Aseguramos que el logo se mantenga fijo y no se mueva */
.logo img {
  width: 3.5vw; /* Adaptable */
  margin-top: -2vh;
  margin-left: -1vw;
}

/* Estilos de la barra de búsqueda */
.search-bar {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  height: auto;

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

.perfil {
  height: 80vh;
  display: flex;
  padding: 2vw;
  margin-top: 5vh;
  flex-direction: column;
  align-items: flex-start;
}
.play-button {
  background: none; /* Sin fondo extra */
  border: none; /* Sin borde */
  cursor: pointer; /* Cambia el puntero al pasar el mouse */
  display: flex; /* Para ajustar alineación interna */
  align-items: center; /* Centra el contenido verticalmente */
  justify-content: flex-start; /* Alinea el contenido a la izquierda */
  padding: 0; /* Sin espacio interno */
  margin: 0; /* Sin márgenes extra */
  width: 3000vw;
}
.play-button img {
  margin-top: 5vh;
  margin-left: -3vw;
}

.album {
  display: flex;
  flex-direction: row; /* Imagen a la izquierda, texto a la derecha */
  align-items: flex-start; /* Alinea verticalmente al inicio */
  gap: 2vw; /* Espaciado entre la imagen y el texto */
  margin-bottom: 2vh; /* Espacio debajo de la sección de detalles */
}

.album img {
  width: 20vw;
  height: 40vh;
  object-fit: cover;
  border-radius: 10px;
}
.album-info {
  margin: 0;
}

.details {
  display: flex;
  flex-direction: column;
  justify-content: center; /* Centrar verticalmente */

}

.song-info p {
  margin: 1vw 0;
  color: white;
}

.song-info img {
  justify-content: center;
  width: 20vw;
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

/* Estilos de la información del álbum */
.information {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 0 0.5vw;
  color: #ffffff;
  flex-direction: column;
  gap: 0.5vh;
  font-size: 1.5rem;
}
.information v-btn {
  background-color: black;
  color: black;
}

.favorite-btn-container {
  position: absolute;
  top: 80vh; /* Distancia desde la parte inferior de la pantalla */
  right: 5vw;/* Distancia desde el lado derecho de la pantalla */
  z-index: 1; /* Asegúrate de que el botón esté encima de otros elementos */
}

.favorite-btn-container i {
  font-size: 3rem; /* Puedes ajustar el tamaño del icono */
  color: #ff0000; /* Color del icono */
  cursor: pointer;
}

.comments-section {
  margin-top: 20px;
  color: white;
  position: relative;
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
  z-index: 9999;
}

.comment-input-container button {
  padding: 10px;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  z-index: 9999;
}

.comment-input-container button:hover {
  background-color: #f44336;
}

.item:hover {
  transform: scale(1.1);
  box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.5);
}

.item img {
  width: 5vw;
  height: 5vw;
  border-radius: 10px;
  margin-right: 0.2vw;
  object-fit: cover;
  margin-left: 0.1vw;

}

.item img:hover {
  transform: scale(1.1);

}

.item-info p {
  margin: 0.5vw;
  color: white;
  font-size: 1rem;
  text-align: left;
}

.item {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 24vw;
  text-align: center;
  background-color: #1f1f1f;
  border-radius: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.mirrored {
  transform: rotate(180deg); /* Rota la imagen 180 grados */
  transition: transform 0.3s ease;
}

.delete-button{
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

</style>
