<template>
  <div class="perfil-artist">
    <!-- Fondo animado -->
    <div class="background-animation"></div>

    <div class="logo-link" @click="goHome">
      <img src="../assets/Im_logo.png" alt="Logo" class="logo" />
    </div>
    <header class="perfil-header">
      <div class="avatar-container">
        <img :src="getArtistImage(artistStageName)" alt="Avatar del artista" class="avatar" />
      </div>
      <div class="artist-details">
        <h1>{{ artistStageName }}</h1>
        <p class="genre">{{ genre }}</p>
        <p v-if="expandedBio" class="bio">{{ bio }}</p>
        <p v-else class="bio-short">{{ shortBio }}</p>
        <button class="btn-toggle-bio" @click="toggleBio">
          {{ expandedBio ? 'Ver menos' : 'Ver más' }}
        </button>
      </div>
    </header>

    <section class="top-section">
      <div class="top-columns">
        <!-- Discografía Destacada -->
        <div class="top-discography">
          <h2 class="title-red">Discografía Destacada</h2>
          <ul>
            <li v-for="song in artist_songs" :key="song.id">{{ song.title }} - {{ getYear(song.timestamp) }}</li>
          </ul>
        </div>

        <!-- Línea divisoria -->
        <div class="divider"></div>

        <div class="top-collaborations">
          <h2 class="title-red">Colaboraciones</h2>
          <ul>
            <li v-for="collab in collaborations" :key="collab.id">{{ collab.title }} - {{ collab.artist }}</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Eventos Cercanos -->
    <div class="events-container">
      <section class="events">
        <h2 class="title-red">Próximos Eventos</h2>
        <ul>
          <li v-for="event in upcomingEvents" :key="event.id">{{ event.name }} - {{ event.date }} - {{ event.location }}</li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script>
import SongService from '../services/SongService'
import UserService from '../services/UserService'
export default {
  name: 'ArtistProfile',
  computed: {
    truncatedDescription () {
      return this.bio.length > 20
        ? this.bio.substring(0, 20) + '...'
        : this.bio
    }
  },
  data () {
    return {
      artistStageName: '',
      drawer: false,
      artist_songs: [],
      genre: 'Rumba - Pop - Rock',
      bio: '',
      shortBio: '',
      expandedBio: false,
      collaborations: [
        { id: 1, title: 'Destino o Casualidad', artist: 'Ha*Ash' },
        { id: 2, title: 'Desde que estamos juntos', artist: 'Alejandro Sanz' }
      ],
      upcomingEvents: [
        { id: 1, name: 'Gira 2024 - Madrid', date: '15 de marzo', location: 'Wizink Center, Madrid' },
        { id: 2, name: 'Gira 2024 - Sevilla', date: '29 de marzo', location: 'Auditorio Rocío Jurado, Sevilla' },
        { id: 3, name: 'Festival Primavera Sound', date: '5 de abril', location: 'Parc del Fòrum, Barcelona' }
      ]
    }
  },
  mounted () {
    this.artistStageName = this.$route.query.artist
    SongService.getAllArtist(this.artistStageName).then(response => {
      this.artist_songs = response.data.data
      UserService.getbyArtist(this.artistStageName).then(response => {
        this.bio = response.data.description
      })
    })
  },
  methods: {
    toggleBio () {
      this.expandedBio = !this.expandedBio
    },
    getArtistImage (artist) {
      const sanitizedArtist = this.removeAccents(artist.toLowerCase().replace(/ /g, ''))
      return require(`@/assets/artistas/${sanitizedArtist}.jpeg`)
    },
    removeAccents (str) {
      return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Elimina los acentos
    },
    toggleDrawer () {
      this.drawer = !this.drawer // Alterna el estado del drawer
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
      this.$router.push({path: '/song',
        query: {
          email: this.$route.query.email,
          logged: this.$route.query.logged,
          token: this.$route.query.token,
          song: song.id
        }
      })
      this.$router.go()
    },
    getYear (timestamp) {
      const date = new Date(timestamp)
      return date.getFullYear()
    },
    goHome () {
      this.$router.push({
        path: '/home',
        query: {email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token}
      })
      this.$router.go()
    }
  }
}
</script>

<style scoped>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden;
}

/* Fondo animado */
.background-animation {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('../assets/fondo.jpg'); /* Reemplazar con la textura del fondo animado */
  background-size: cover;
  filter: brightness(50%);
  z-index: -1;
}

.perfil-artist {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  color: white;
  padding: calc(2vh + 4vw) 3vw 3vh;
  min-height: 100vh;
  overflow-y: auto;
  box-sizing: border-box;
}

.perfil-header {
  background: rgba(31, 31, 31, 0.9);
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

.logo {
  width: 8vw;
  max-width: 50px;
  height: auto;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.1);
}

.avatar-container {
  margin-right: 2vw;
}

.avatar {
  width: 15vw;
  height: 15vw;
  border-radius: 50%;
  border: 0.3vw solid #ff3d00;
}

.artist-details {
  flex-grow: 1;
  max-width: 500px;
}

.artist-details h1 {
  font-size: 2.5rem;
  margin: 0;
}

.bio, .bio-short {
  margin-top: 2vh;
  font-size: 1rem;
}

.btn-toggle-bio {
  background-color: #ff3d00;
  color: white;
  padding: 0.5rem 1.2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn {
  background-color: #bf0000;
  padding: 1.5vh 2vw;
  border-radius: 2vw;
  color: white;
}

.btn:hover {
  background-color: #a30000;
}

.genre {
  color: #aaa;
  margin-top: 1vh;
}

.bio, .bio-short {
  margin-top: 2vh;
  font-size: 1rem;
}

.btn-toggle-bio {
  background-color: #ff3d00;
  color: white;
  padding: 0.5rem 1.2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.top-section {
  margin-top: 2vh;
  width: 100%;
  background-color: rgba(31, 31, 31, 0.9);
  padding: 2vh 2vw;
  border-radius: 1vw;
}

.top-columns {
  display: flex;
  gap: 2vw;
}

.top-discography, .top-collaborations {
  flex: 1;
}

.top-discography ul, .top-collaborations ul {
  list-style: none;
  padding: 0;
  margin-top: 0;
}

.logo-link {
  position: fixed;
  top: 1rem;
  left: 1rem;
  z-index: 1000;
  cursor: pointer;
}

li {
  color: #ddd;
  margin-bottom: 0.5rem;
}

.divider {
  width: 2px;
  background-color: #949393;
  margin: 0 1vw;
}

.title-red {
  color: red;
}

.events {
  margin-top: 2vh;
  background-color: rgba(31, 31, 31, 0.9);
  padding: 2vh 2vw;
  border-radius: 1vw;
}

.events-container {
  width: 100%;
  padding: 0;
  margin: 0 auto;
  box-sizing: border-box;
}

/* Media queries para pantallas pequeñas */
@media (max-width: 768px) {
  .perfil-artist {
    padding: 2vh 4vw;
  }

  .perfil-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 2vh 2vw;
  }

  .avatar-container {
    margin: 0 0 2vh;
  }

  .avatar {
    width: 30vw;
    height: 30vw;
    border-width: 0.2vw;
  }

  .artist-details h1 {
    font-size: 1.8rem;
  }

  .bio, .bio-short {
    font-size: 0.9rem;
  }

  .btn-toggle-bio {
    font-size: 0.9rem;
    padding: 0.4rem 1rem;
  }

  .top-section {
    flex-direction: column;
    gap: 2vh;
    padding: 3vh 3vw;
  }

  .top-columns {
    flex-direction: column;
    gap: 2vh;
  }

  .divider {
    display: none;
  }

  .top-discography, .top-collaborations {
    padding: 2vh 2vw;
  }

  .logo {
    width: 12vw;
    max-width: 40px;
  }

  .events {
    padding: 3vh 3vw;
  }

  li {
    font-size: 0.9rem;
  }

  .events-container {
    margin: 0;
    width: 100%;
  }
}

</style>
