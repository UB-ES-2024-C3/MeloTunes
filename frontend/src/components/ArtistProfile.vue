<template>
  <div class="perfil-artist">
    <!-- Encabezado del perfil con fondo -->
    <header class="perfil-header">
      <div class="avatar-container">
        <img :src="getArtistImage(artistStageName)" alt="Avatar del artista" class="avatar" />
      </div>
      <div class="artist-details">
        <h1>{{ artistStageName }}</h1>
        <p class="genre">{{ genre }}</p>
        <p v-if="expandedBio" class="bio">{{ bio }}</p>
        <p v-else class="bio-short">{{ truncatedDescription }}</p>
        <button class="btn-toggle-bio" @click="toggleBio">{{ expandedBio ? 'Ver menos' : 'Ver más' }}</button>
      </div>
    </header>

    <!-- Sección Discografía y Colaboraciones en columnas con línea divisoria -->
    <section class="top-section">
      <div class="top-columns">
        <!-- Discografía Destacada -->
        <div class="top-discography">
          <h2>Discografía Destacada</h2>
          <ul>
            <li v-for="song in artist_songs" :key="song.id">{{ song.title }} - {{ getYear(song.timestamp) }}</li>
          </ul>
        </div>

        <!-- Línea divisoria -->
        <div class="divider"></div>

        <!-- Colaboraciones -->
        <div class="top-collaborations">
          <h2>Colaboraciones</h2>
          <ul>
            <li v-for="collab in collaborations" :key="collab.id">{{ collab.title }} - {{ collab.artist }}</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Próximos Conciertos -->
    <section class="events">
      <h2>Próximos Conciertos</h2>
      <ul>
        <li v-for="event in upcomingEvents" :key="event.id">{{ event.name }} - {{ event.date }} - {{ event.location }}</li>
      </ul>
    </section>
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
        { id: 2, name: 'Gira 2024 - Sevilla', date: '29 de marzo', location: 'Auditorio Rocío Jurado, Sevilla' }
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
      this.$router.push({ path: '/song', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token, song: song.id } })
      this.$router.go()
    },
    getYear (timestamp) {
      const date = new Date(timestamp)
      return date.getFullYear()
    }
  }
}
</script>

<style scoped>
/* Nuevos estilos para el nombre real */
.real-name {
  color: #ccc;
  font-size: 1rem;
  margin-top: 0.5rem;
}

.perfil-artist {
  background-color: #121212;
  color: white;
  padding: 2rem;
  min-height: 100vh;
}

.perfil-header {
  background: #1f1f1f;
  padding: 2rem;
  display: flex;
  align-items: center;
  border-radius: 12px;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  margin-bottom: 2rem;
}

.avatar-container {
  flex-shrink: 0;
  margin-right: 1.5rem;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 3px solid #ff3d00;
  object-fit: cover;
}

.artist-details {
  flex-grow: 1;
  max-width: 500px;
}

.artist-details h1 {
  font-size: 2rem;
  margin: 0;
  font-weight: 700;
}

.genre {
  color: #aaa;
  margin-top: 0.5rem;
}

.bio, .bio-short {
  margin-top: 1rem;
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
  background-color: #1f1f1f;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 2rem;
}

.top-section h2 {
  color: #ff3d00;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.top-columns {
  display: flex;
  align-items: stretch;
  gap: 1rem;
}

.top-discography, .top-collaborations {
  flex: 1;
}

.top-discography ul, .top-collaborations ul {
  list-style: none;
  padding: 0;
  margin-top: 0;
}

li {
  color: #ddd;
  margin-bottom: 0.5rem;
}

.divider {
  width: 1px;
  background-color: #555;
  height: auto;
  align-self: stretch;
}

.events {
  margin-top: 2rem;
  background-color: #1f1f1f;
  padding: 1rem;
  border-radius: 8px;
}

.events h2 {
  color: #ff3d00;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.events ul {
  list-style: none;
  padding: 0;
}

.events li {
  color: #ddd;
  margin-bottom: 0.5rem;
}

</style>
