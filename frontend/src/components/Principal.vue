<template>
  <div>
    <div class="background-image"></div> <!-- Fondo elegante -->
    <header>
      <div class="logo">
        <img src="../assets/logo2.png" alt="Logo">
      </div>
      <div></div> <!-- Espacio para alinear botones a la derecha -->
      <div class="auth-buttons" v-if="!isLogedIn">
        <a href="#" @click="login">Iniciar sesión</a>
        <a href="#" @click="register">Registrarse</a>
      </div>
      <div class="auth-buttons" v-if="isLogedIn">
        <a href="#" @click="profile">Ver perfil</a>
        <a href="#" @click="logOut">Cerrar sesión</a>
      </div>
    </header>

    <div class="hero">
      <h1>
        <span translate="no" class="melo">¡MELO</span><span translate="no" class="tunes">TUNES!</span>
      </h1>
    </div>

    <div class="search-bar">
      <input type="text" placeholder="Busca canciones, artistas" v-model="searchQuery" @keyup.enter="searchSong" />
      <button @click="searchSong">
        <img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:20%; vertical-align: middle;">
        Buscar
      </button>
    </div>

    <div class="album-grid">
      <div v-for="(song) in songs_list" :key="song.id" class="album" @click="handleClick(song)">
        <img :src="getAlbumImage(song.album)" alt="Portada del álbum">
        <div class="album-info">
          <p>{{ song.title }}</p>
          <p>{{ song.artist }}</p>
          <p>{{ song.album }}</p>
          <p>{{ getYear(song.timestamp) }}</p>
        </div>
      </div>
    </div>

    <div v-if="!searchQuery" class="artist-section">
      <h2>Artistas Populares</h2>
      <div class="artist-grid">
        <div v-for="artist in artists" :key="artist" class="artist" @click="goArtist(artist)">
          <img :src="getArtistImage(artist)" alt="Artista">
          <p class="artist-name">{{ artist }}</p>
        </div>
      </div>
    </div>

    <footer>
      <div class="legal">
        <v-flex class="mt-12 mb-3">
          <popuplegal ref="popuplegal" />
          <button class="legal" @click="$refs.popuplegal.openPopup()">Legal</button>
        </v-flex>
        <v-flex class="mt-12 mb-3">
          <popuppolitica ref="popuppolitica" />
          <button class="legal" @click="$refs.popuppolitica.openPopup()">Política de privacidad</button>
        </v-flex>
        <v-flex class="mt-12 mb-3">
          <popupcookies ref="popupcookies" />
          <button class="legal" @click="$refs.popupcookies.openPopup()">Cookies</button>
        </v-flex>
      </div>
      <div class="social-icons">
        <a href="#"><img src="../assets/facebook.png" alt="Logo de Facebook"></a>
        <a href="#"><img src="../assets/instagram.png" alt="Logo de Instagram"></a>
        <a href="#"><img src="../assets/twitter.png" alt="Logo de Twitter"></a>
      </div>
    </footer>
  </div>
</template>

<script>
import SongService from '../services/SongService'
import popuplegal from './popupLegal'
import popuppolitica from './popupPolitica'
import popupcookies from './popupCookies'
export default {
  components: { popuplegal, popuppolitica, popupcookies },
  name: 'Home',
  computed: {
    isLogedIn () {
      return this.$route.query.logged === 'true'
    }
  },
  mounted () {
    if (this.isLogedIn) {
      this.user_name = this.$route.query.email
    }
    SongService.getAll().then(response => {
      this.all_songs = response.data.data
      this.songs_list = response.data.data.slice(0, 8)
      for (const song of this.songs_list) {
        if (!this.artists.includes(song.artist)) {
          this.artists.push(song.artist)
        }
      }
      const savedSearchQuery = localStorage.getItem('searchQuery')
      console.log(savedSearchQuery)
      if (savedSearchQuery !== '') {
        this.searchQuery = savedSearchQuery
        this.searchSong()
      }
    })
  },
  data () {
    return {
      searchQuery: '',
      songs_list: [],
      all_songs: [],
      artists: [],
      user_name: null
    }
  },
  methods: {
    register () {
      this.$router.push('/register')
      this.$router.go()
    },
    login () {
      this.$router.push('/login')
      this.$router.go()
    },
    logOut () {
      this.$router.push('/home')
      this.$router.go()
    },
    profile () {
      this.$router.push({ path: '/perfil_user', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token } })
      this.$router.go()
    },
    goArtist (artist) {
      this.$router.push({ path: '/artist_profile', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token, artist: artist } })
      this.$router.go()
    },
    getYear (timestamp) {
      const date = new Date(timestamp)
      return date.getFullYear()
    },
    handleClick (song) {
      this.$router.push({ path: '/song', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token, song: song.id } })
      this.$router.go()
    },
    removeAccents (str) {
      return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Elimina los acentos
    },
    getArtistImage (artist) {
      const sanitizedArtist = this.removeAccents(artist.toLowerCase().replace(/ /g, ''))
      return require(`@/assets/artistas/${sanitizedArtist}.jpeg`)
    },
    getAlbumImage (artist) {
      const sanitizedArtist = this.removeAccents(artist.toLowerCase().replace(/ /g, ''))
      return require(`@/assets/albumes/${sanitizedArtist}.jpeg`)
    },
    searchSong () {
      // Si la búsqueda está vacía, mostrar todas las canciones
      if (!this.searchQuery.trim()) {
        SongService.getAll().then(response => {
          this.songs_list = response.data.data.slice(0, 8)
        })
        return
      }

      const normalizedSearchQuery = this.removeAccents(this.searchQuery.toLowerCase())
      // Filtra las canciones que coinciden parcialmente con el título
      this.songs_list = this.all_songs.filter(song =>
        this.removeAccents(song.title.toLowerCase()).includes(normalizedSearchQuery) ||
        this.removeAccents(song.artist.toLowerCase()).includes(normalizedSearchQuery) ||
        this.removeAccents(song.album.toLowerCase()).includes(normalizedSearchQuery)
      ).slice(0, 8)
      localStorage.removeItem('searchQuery')
    }
  }
}
</script>

<style scoped>
/* Estilos generales del body */
body {
  margin: 0;
  padding: 0;
  font-family: 'Poppins', sans-serif;
  background-color: black;
  color: white;
  position: relative;
  min-height: 100vh; /* Asegura que el cuerpo ocupe al menos la altura de la ventana */
  display: flex;
  flex-direction: column;
}

div {
  flex-grow: 1; /* Permite que los contenidos de la página se estiren si el contenido es mayor que la ventana */
}

/* Fondo elegante con gradiente y foto */
.background-image {
  background: url('../assets/fondo.png') no-repeat center center fixed; /* Imagen de fondo centrada */
  background-size: cover; /* Asegura que la imagen cubra toda la pantalla */
  position: fixed; /* Mantiene el fondo fijo mientras haces scroll */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%; /* Se asegura de cubrir toda la altura de la ventana */
  z-index: -1; /* Mantiene el fondo detrás de todo el contenido */
  filter: brightness(0.7); /* Oscurece la imagen */
}

/* Estilo para el header y los textos */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 3vh 2vw;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7); /* Fondo oscuro semitransparente */
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

/* Aseguramos que el logo se mantenga fijo y no se mueva */
.logo img {
  width: 3.5vw; /* Adaptable */
  margin-top: -2vh;
  margin-left: -1vw;
}

/* Aseguramos que los botones de autenticación estén en línea y en la parte superior derecha */
header .auth-buttons {
  display: flex; /* Cambiado a flex para alinear los botones en línea */
  gap: 1vw; /* Espacio entre los botones */
  position: absolute; /* Posición absoluta dentro del header */
  top: 50%; /* Centrado verticalmente */
  right: 2vw; /* Se mantiene a 2vw del borde derecho */
  transform: translateY(-50%); /* Para ajustar y centrar el bloque de botones */
}

header .auth-buttons a {
  text-decoration: none;
  color: white;
  padding: 1.5vh 1vw;
  border: 1px solid white;
  border-radius: 25px;
  transition: background-color 0.3s ease, color 0.3s ease;
  font-size: 1rem;
}

header .auth-buttons a:hover {
  background-color: white;
  color: black;
}

.hero {
  text-align: center;
  margin-top: 12vh;
}

.hero h1 {
  font-size: 6vw; /* Mantiene el tamaño grande del texto */
  color: white;
  letter-spacing: 0.5vw;
  margin-bottom: 15vh;
  background-color: rgba(0, 0, 0, 0.6); /* Fondo oscuro con opacidad para hacer que el texto resalte */
  display: inline-block;
  padding: 0.5em;
  border-radius: 10px;
  margin-top: 8vh; /* Baja el título un poco */
}

.hero h1 .melo {
  color: #e53935;
}

.hero h1 .tunes {
  color: #ffffff;
}

/* Fondo para los botones y la barra de búsqueda */
.search-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10vh; /* Reducido un poco el margen superior */
  background-color: rgba(0, 0, 0, 0.6); /* Fondo oscuro semitransparente */
  padding: 1.5em;
  border-radius: 10px;
}

.search-bar input {
  width: 40vw;
  padding: 1.5vh;
  font-size: 1.2rem;
  border-radius: 25px;
  border: none;
  color: white; /* Cambia el color del texto a blanco */
  background-color: rgba(0, 0, 0, 0.7); /* Fondo oscuro para que el texto sea legible */
}

.search-bar button {
  padding: 1.5vh 2vw;
  background-color: #f32121;
  border: none;
  color: white;
  border-radius: 25px;
  margin-left: 1vw;
  cursor: pointer;
}

.search-bar button:hover {
  background-color: #f32121;
}

/* Estilo para la sección de los álbumes */
.album-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 5vw 5vw;
  margin-top: 10vh;
}

/* Estilo individual para cada tarjeta de álbum */
.album {
  background-color: rgba(0, 0, 0, 0.6); /* Fondo oscuro semitransparente para resaltar */
  border-radius: 15px; /* Bordes suaves */
  overflow: hidden; /* Asegura que las imágenes se ajusten dentro de la tarjeta */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transición suave */
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Asegura que los elementos estén alineados dentro de la tarjeta */
}

.album:hover {
  transform: translateY(-5px); /* Efecto de hover que mueve la tarjeta hacia arriba */
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.7); /* Sombra más pronunciada al pasar el mouse */
}

/* Estilo para la imagen del álbum */
.album-image img {
  width: 100%;
  height: auto;
  object-fit: cover; /* Mantiene la proporción de la imagen */
  border-bottom: 2px solid rgba(255, 255, 255, 0.2); /* Línea sutil debajo de la imagen */
}

/* Estilo para la información de la canción */
.album-info {
  padding: 15px;
  background-color: rgba(0, 0, 0, 0.8); /* Fondo oscuro para resaltar el texto */
  border-radius: 0 0 15px 15px;
}

.album-info p {
  margin: 0;
  color: white; /* Color del texto blanco */
  font-size: 1.2rem;
  text-align: center; /* Centra el texto */
}

/* Estilos específicos para cada tipo de texto */
.album-title {
  font-weight: bold;
  font-size: 1.4rem;
}

.album-artist, .album-album, .album-year {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.8); /* Texto menos opaco para diferenciarlo */
}

/* Efectos de hover en los textos */
.album-info p:hover {
  color: #f32121; /* Color rojo al pasar el ratón */
}

/* Fondo para los artistas */
.artist-section {
  margin-top: 10vh;
  padding: 5vw;
  background-color: rgb(147, 134, 134); /* Fondo oscuro semitransparente */
  border-radius: 10px;
  text-align: center; /* Asegura que el texto esté centrado en la sección */
}

/* Ajustar la cuadrícula de los artistas */
.artist-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center; /* Centra los elementos de la cuadrícula */
  align-items: center; /* Asegura que los elementos estén alineados verticalmente */
}

/* Estilo para cada bloque de artista */
.artist {
  display: flex;
  flex-direction: column; /* Hace que la imagen y el nombre se alineen verticalmente */
  align-items: center; /* Centra los elementos dentro de cada bloque */
  justify-content: center; /* Asegura que los elementos estén centrados */
}

/* Ajustes a las imágenes de los artistas */
.artist img {
  width: 25vw;
  height: 25vh;
  object-fit: cover;
  border-radius: 10px;
  transition: transform 0.3s ease;
  margin-bottom: 10px; /* Añadido margen inferior para separar imagen del nombre */
}

.artist img:hover {
  transform: scale(1.05); /* Efecto de hover para las imágenes */
}

/* Estilo para los nombres de los artistas */
.artist-name {
  color: white; /* Blanco fuerte */
  font-size: 1.5rem;
  text-align: center;
  font-weight: bold;
  background-color: rgba(0, 0, 0, 0.6); /* Fondo oscuro semitransparente para que el texto resalte */
  padding: 0.5em;
  border-radius: 5px;
}

/* Footer */
footer {
  background-color: rgba(0, 0, 0, 0.7); /* Fondo oscuro con algo de transparencia */
  padding: 3vw;
  text-align: center;
  position: relative;
  bottom: 0;
}

footer .legal {
  color: white;
  font-size: 1rem;
  padding: 1em;
  border: none;
  background: none;
  cursor: pointer;
  text-align: center;
}

footer .social-icons {
  display: flex;
  justify-content: center;
  gap: 1em;
  margin-top: 2em;
}

footer .social-icons a {
  text-decoration: none;
}

footer .social-icons img {
  width: 2.5em;
  height: 2.5em;
  object-fit: cover;
  transition: transform 0.3s ease;
}

footer .social-icons img:hover {
  transform: scale(1.1); /* Efecto de hover para los iconos sociales */
}

</style>
