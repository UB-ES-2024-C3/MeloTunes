<template class="body">
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
  <div class="album">
    <img :src="getAlbumImage(song.album)" alt="Album Cover">
    <p class="album-title">{{ song.album }}</p>
    <p class="album-author">{{ song.artist }}</p>
  </div>
    <div class="items">
      <span class="song_name">{{ song.title }}</span>
      <div class="favorito">
        <i
          :class="isFavorited ? 'fas fa-heart' : 'far fa-heart'"
          @click="addFavorites"
          style="cursor: pointer; font-size: 24px; color: red;"
        ></i>
      </div>
    </div>
  <div class="items">
    <span class="song_name">{{ song.title }}</span>
    <div class="favorito">
      <i
        :class="isFavorited ? 'fas fa-heart' : 'far fa-heart'"
        @click="addFavorites"
        style="cursor: pointer; font-size: 24px; color: red;"
      ></i>
    </div>
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
.main-container, body {
  background-color: black !important;
  flex-direction: row;
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
  margin-left: 1vw;
}
.album {
  display: flex;
  justify-content: center; /* Centra horizontalmente */
  align-items: center; /* Centra verticalmente */
  height: 100vh; /* Hace que el contenedor ocupe toda la altura de la ventana */
  margin: 0; /* Elimina cualquier margen */
  flex-direction: column;
  padding: 0;
  margin-top: -35vh;
}

.album-title {
  font-size: 1.5rem; /* Ajusta el tamaño de la fuente */
  color: white; /* Color del texto */
  text-align: center; /* Centra el texto */
  margin: 0; /* Elimina márgenes adicionales */
}

.album-author {
  font-size: 1.3rem; /* Ajusta el tamaño de la fuente */
  color: white; /* Color del texto */
  text-align: center; /* Centra el texto */
  margin-bottom: -40vh;
  }

/* Elimina espacio entre el recuadro y el nombre del autor */
.items {
  display: flex;
  justify-content: space-between; /* Espaciar elementos */
  align-items: center; /* Centra verticalmente los elementos */
  width: 90vw; /* Ocupa todo el ancho */
  padding: 1rem 1rem; /* Espaciado interno */
  background-color: #1e1e1e; /* Fondo oscuro para el recuadro */
  color: white; /* Texto en blanco */
  margin-left: 4vw;
  margin-bottom: 2vh;
  border-radius: 20px;

}

.song_name {
  font-size: 1.3rem; /* Tamaño del texto del nombre de la canción */

}

.favorito {
  width: 5vw; /* Tamaño de la imagen */
  height: auto; /* Mantiene la proporción de la imagen */
  object-fit: cover; /* Asegura que la imagen no se deforme */
  border-radius: 10px; /* Bordes redondeados para un toque estilizado */
}

</style>
