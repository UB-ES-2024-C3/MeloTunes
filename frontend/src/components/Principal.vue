<template>
  <body>
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
    <button @click="searchSong"><img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:20%; vertical-align: middle;">
      Buscar
    </button>
  </div>

  <div class="album-grid">
    <!-- Aquí cambiamos las canciones por un bucle que renderiza cada álbum dinámicamente -->
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
      <div v-for="artist in artists" :key="artist" class="artist">
        <img
          :src="getArtistImage(artist)"
          alt="Artista"
          style="width: 25vw; height: 25vh;"
        >
        <p>{{ artist }}</p>
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
  </body>
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
    }
  }
}
</script>

<style scoped>
/* Estilos básicos */
.logo img {
  width: 3.5vw; /* Adaptable */
  margin-top: -2vh;
  margin-left: -1vw;
}

body {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  background-color: black;
  color: white;
  padding-top: 17vh; /* Ajuste para adaptarse a la altura del header */
  overflow-y: auto; /* Habilita el scroll */

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
  background: linear-gradient(to bottom, #e53935, #000);
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
  transition: top 0.3s;
  z-index: 1000;
}

header .auth-buttons a {
  text-decoration: none;
  color: white;
  padding: 1.5vh 1vw;
  border: 1px solid white;
  border-radius: 25px;
  margin-left: 1vw;
  transition: background-color 0.3s ease, color 0.3s ease;
  font-size: 1rem;
}

header .auth-buttons a:hover {
  background-color: white;
  color: #e53935;
}

.hero {
  text-align: center;
  margin-top: 12vh;
}

.hero h1 {
  font-size: 6vw;
  color: white;
  letter-spacing: 0.5vw;
  margin-bottom: 15vh;
}

.hero h1 .melo {
  color: #e53935;
}

.search-bar {
  display: flex;
  justify-content: center;
  margin: 10vh 10vh 30vh;
  color: white;
}

.search-bar input[type="text"] {
  width: 60vw;
  padding: 1.2vw;
  font-size: 1.5rem;
  border: none;
  border-radius: 30px;
  margin-right: 1vw;
  outline: none;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
  background-color: white;
}

.search-bar button {
  padding: 1vh;
  font-size: 1.5rem;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 10vw;

}

.search-bar button:hover {
  background-color: #c62828;
}

.album-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.5vw;
  margin: 1vh  0.15vw 1vh;

}
.album:hover {
  transform: scale(1.1);
  box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.5);
}

.album img {
  width: 8vw;
  height: 8vw;
  border-radius: 10px;
  margin-right: 0.3vw;
  object-fit: cover;
}
.album img:hover {
  transform: scale(1.1);

}
.album-info {
  display: flex;
  flex-direction: column;
}

.album-info p {
  margin: 0.2vw;
  color: white;
  font-size: 1rem;
  text-align: left;
}

.album {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 24vw;
  text-align: center;
  padding: 0.5vh 0.1vw;
  background-color: #1f1f1f;
  border-radius: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.artist-section h2 {
  font-size: 5vw;
  text-align: center;
  margin: 5vh 0 5vh;
  color: #e53935;
}

.artist-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 2vw;
  margin-bottom: 5vh;
}

.artist {
  text-align: center;
  font-size: 1.2rem;
}

.artist img {
  width: 12vw;
  height: 12vw;
  border-radius: 50%;
  border: 3px solid #e53935;
  transition: transform 0.3s ease;
}

.artist img:hover {
  transform: scale(1.1);
}

footer {
  background-color: #1f1f1f;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2vh 2vw;
}

footer .legal {
  display: flex;
  flex-direction: column;
  gap: 0.1vh;
  width: 25vw;
  font-size: 1.5rem;
}

footer .social-icons a {
  display: inline-block;
}

footer .social-icons img {
  width: 3vw;
  margin-top: 1vh;
  margin-right: 0.4vw;
}

footer .legal a {
  color: white;
  font-size: 1.5rem;
}

/* Media Queries para mejorar la adaptabilidad */

  .hero h1 {
    font-size: 12vw;
  }

  .search-bar input[type="text"] {
    width: 45vw;
  }

  .search-bar button {
    width: 15vw;
  }

  .album img, .artist img {
    width: 10vw;
    height: 10vw;
  }

  .artist-section h2 {
    font-size: 5rem;
  }

</style>
