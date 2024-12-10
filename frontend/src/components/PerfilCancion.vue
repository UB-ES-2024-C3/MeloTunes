<template class="main">
  <div class="main-container">
    <header>
      <div class="logo">
        <button @click="goHome" style="border: none; background: none;">
          <img src="../assets/logo2.png" alt="Logo"></button>
      </div>

      <div class="search-bar">
        <input type="text" placeholder="Busca canciones, artistas" v-model="searchQuery" @keyup.enter="searchSong" />
        <button @click="goHome"><img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:2vw; vertical-align: middle;">
          Buscar
        </button>
      </div>
    </header>
    <div>
      <div class="perfil">
        <div class="album">
          <img :src="getAlbumImage(song.album)" alt="Album Cover" class="album-img">

          <!-- Contenedor para el título y el autor -->
          <div class="details">
            <p class="song-title">{{ song.title }}</p>
            <p class="song-author">{{ song.artist }}</p>
            <button class="play-button" @click="goHome"> <img src="../assets/play.png" style="width:10vw; height:10vh;object-fit: contain;">
            </button>
          </div>

        </div>

        <!-- Información del álbum -->
        <div class="information">
          <p class="album-info">{{ song.album }}</p>
          <p class="album-info">{{ getYear(song.timestamp) }}</p></div>
        <v-app class="main-container">
          <v-btn color="black"  @click="toggleDrawer" class="floating-btn" :class="{ mirrored: drawer }">
            <img
              src="../assets/avance-rapido.png"
              alt="Botón Imagen"
              height=40
              width="40"
            />
          </v-btn>
        </v-app>
        <div class="favorite-btn-container">
          <i
            :class="isFavorited ? 'fas fa-heart' : 'far fa-heart'"
            @click="addFavorites"
            style="cursor: pointer; font-size: 24px; color: #ff0000;"
          ></i>
        </div>
      </div>

    </div>
    <div>
      <v-app class="main-container">
        <!-- Drawer en la parte derecha con 'persistent' para que no se cierre cuando haga clic fuera -->
        <v-navigation-drawer v-model="drawer" app right persistent style="background-color: #212121; margin-top: 12vh" height="100vh" width="22vw">
          <v-list>
            <v-list-item v-for="song in artist_songs" :key="song.id" @click="handleClick(song)">
              <v-list-item-content>
                <v-list-item-title class="item">
                  <!-- Muestra la portada del álbum o una imagen por defecto -->
                  <img :src="getAlbumImage(song.album)" alt="Portada del álbum">
                  <div class="item-info">
                    <!-- Muestra el título de la canción y el nombre del artista -->
                    <p>{{ song.title }}</p>
                  </div>
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
      </v-app>
    </div>
  </div>
</template>

<script>
import SongService from '../services/SongService'
import UserService from '../services/UserService'
export default {
  data () {
    return {
      all_songs: [],
      artist_songs: [],
      song: {},
      song_id: 0,
      drawer: false, // Estado del drawer
      isFavorited: false,
      searchQuery: ''
    }
  },
  mounted () {
    this.song_id = this.$route.query.song
    SongService.get(this.song_id).then(response => {
      this.song = response.data
      SongService.getAll().then(response => {
        this.all_songs = response.data.data
        this.artist_songs = this.all_songs.filter(song => song.artist === this.song.artist)
      })
      this.checkIfFavorite()
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
        UserService.addToFavoriteSongs(this.song_id).then(response => {
          console.log(response)
          this.isFavorited = true
        })
      } else {
        UserService.deleteOfFavoriteSongs(this.song_id).then(response => {
          console.log(response)
          this.isFavorited = false
        })
      }
    },
    checkIfFavorite () {
      UserService.getMyFavouriteSongs().then(response => {
        const favorites = response // Asumiendo que la API devuelve un arreglo de canciones favoritas
        console.log(favorites)
        this.isFavorited = favorites.some(fav => Number(fav.id) === Number(this.song_id))
        console.log(this.isFavorite)
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
  background-color: black !important;

}

.v-navigation-drawer .v-list-item {
  color: #000000 !important;
}

/* Estilo para el botón flotante */
.floating-btn {
  border: none;
  box-shadow: none;
  cursor: pointer;
  width: 5vw;
  height: 10vh !important;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  transform: scaleX(1);
  transition: transform 0.3s ease;
  margin-top: 5vh;
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
  overflow: hidden;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to bottom, #e53935, #000);
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
  transition: top 0.3s;
  z-index: 1000;

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

/* Estilos de logo */
.logo img {
  width: 5vw;
  margin-top: 1vh;
  margin-left: 1.0vw;
}

.perfil {
  height: 80vh;
  display: flex;
  padding: 2vw;
  margin-top: 15vh;
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
  position: fixed;
  bottom: 5vh; /* Distancia desde la parte inferior de la pantalla */
  right: 5vw;/* Distancia desde el lado derecho de la pantalla */
}

.favorite-btn-container i {
  font-size: 3rem; /* Puedes ajustar el tamaño del icono */
  color: #ff0000; /* Color del icono */
  cursor: pointer;
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

</style>
