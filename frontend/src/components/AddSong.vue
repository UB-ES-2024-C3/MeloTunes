<template>
  <div class="add-song">
    <div class="logo-link" @click="goHome">
      <img src="../assets/Im_logo.png" alt="Logo" class="logo" />
    </div>

    <!-- Opciones de formulario -->
    <div class="form-options">
      <div
        :class="['form-option', { active: !isAlbum && !isAlbumUpload }]"
        @click="setOption('single')"
      >
        Subir Single
      </div>
      <div
        :class="['form-option', { active: isAlbum && !isAlbumUpload }]"
        @click="setOption('album')"
      >
        Subir Canción en un Álbum
      </div>
      <div v-if="this.showAlbum"
        :class="['form-option', { active: isAlbumUpload }]"
        @click="setOption('uploadAlbum')"
      >
        Subir Álbum Completo
      </div>
    </div>

    <!-- Formulario principal -->
    <form class="add-song-form" @submit.prevent="submitSong">
      <!-- Subir Single -->
      <div v-if="!isAlbum && !isAlbumUpload">
        <div class="form-group">
          <label for="songTitle">Título de la canción</label>
          <input
            type="text"
            id="songTitle"
            v-model="song_title"
            placeholder="Ingresa el título de la canción"
            required
          />
        </div>
        <div class="form-group" v-if="this.showAlbum">
          <label for="songFile">Selecciona la canción</label>
          <input
            type="file"
            id="songFile"
            @change="handleFileChange"
            accept="audio/*"
            required
          />
        </div>
        <div class="form-group" v-if="this.showAlbum">
          <label for="albumCover">Portada del Single (PNG, JPEG)</label>
          <input
            type="file"
            id="albumCover"
            @change="handleImageChange"
            accept="image/png, image/jpeg"
          />
        </div>
      </div>

      <!-- Subir Canción en un Álbum -->
      <div v-if="isAlbum">
        <div class="form-group">
          <label for="songTitle">Título de la canción</label>
          <input
            type="text"
            id="songTitle"
            v-model="song_title"
            placeholder="Ingresa el título de la canción"
            required
          />
        </div>
        <div class="form-group">
          <label for="songAlbum">Álbum</label>
          <input
            type="text"
            id="songAlbum"
            v-model="song_album"
            placeholder="Ingresa el nombre del álbum"
            required
          />
        </div>
        <div class="form-group" v-if="this.showAlbum">
          <label for="songFile">Selecciona la canción</label>
          <input
            type="file"
            id="songFile"
            @change="handleFileChange"
            accept="audio/*"
            required
          />
        </div>
        <div class="form-group" v-if="this.showAlbum">
          <label for="albumCover">Portada del Single (PNG, JPEG)</label>
          <input
            type="file"
            id="albumCover"
            @change="handleImageChange"
            accept="image/png, image/jpeg"
          />
        </div>
      </div>

      <!-- Subir Álbum Completo -->
      <div v-if="isAlbumUpload">
        <div class="form-group">
          <label for="albumTitle">Título del Álbum</label>
          <input
            type="text"
            id="albumTitle"
            v-model="album.title"
            placeholder="Ingresa el título del álbum"
            required
          />
        </div>
        <div class="form-group">
          <label for="albumArtist">Artista</label>
          <input
            type="text"
            id="albumArtist"
            v-model="album.artist"
            placeholder="Ingresa el nombre del artista"
            required
          />
        </div>

        <div class="form-group">
          <label>Número de Canciones</label>
          <div class="song-counter">
            <button
              type="button"
              class="btn-counter"
              @click="adjustSongCount(-1)"
              :disabled="album.songCount <= 1"
            >
              -
            </button>
            <span class="song-count">{{ album.songCount }}</span>
            <button
              type="button"
              class="btn-counter"
              @click="adjustSongCount(1)"
            >
              +
            </button>
          </div>
        </div>

        <!-- Lista dinámica de canciones -->
        <div
          v-for="(song, index) in album.songs"
          :key="index"
          class="song-entry"
        >
          <div class="form-group">
            <label :for="'songTitle_' + index">Título de la canción {{ index + 1 }}</label>
            <input
              type="text"
              :id="'songTitle_' + index"
              v-model="album.songs[index].title"
              placeholder="Título de la canción"
              required
            />
          </div>
          <div class="form-group">
            <label :for="'songFile_' + index">Archivo de la canción</label>
            <input
              type="file"
              :id="'songFile_' + index"
              @change="handleFileChangeAlbum(index, $event)"
              accept="audio/*"
              required
            />
          </div>
        </div>
      </div>

      <!-- Botón de envío -->
      <button type="submit" class="btn-submit">
        {{ isAlbumUpload ? 'Subir Álbum' : isAlbum ? 'Subir Canción' : 'Subir Single' }}
      </button>
    </form>
  </div>
</template>

<script>
import UserService from '../services/UserService'
import SongService from '../services/SongService'

export default {
  name: 'AddSong',
  mounted () {
    UserService.get().then(response => {
      this.user_logged = response.data
      console.log(response.data)
    })
  },
  data () {
    return {
      song_title: '',
      song_artist: '',
      song_album: '',
      album: {
        title: '',
        artist: '',
        songCount: 1,
        songs: [{ title: '', file: null }]
      },
      isAlbum: false,
      isAlbumUpload: false,
      showAlbum: false
    }
  },
  methods: {
    setOption (option) {
      this.isAlbum = option === 'album'
      this.isAlbumUpload = option === 'uploadAlbum'

      if (this.isAlbumUpload) {
        this.initializeAlbumSongs()
      }
    },
    initializeAlbumSongs () {
      this.album.songs = Array.from({ length: this.album.songCount }, () => ({
        title: '',
        file: null
      }))
    },
    handleFileChange (event) {
      const file = event.target.files[0]
      if (file && file.type.startsWith('audio/')) {
        this.song.file = file
      } else {
        alert('Por favor selecciona un archivo de audio válido.')
      }
    },
    handleFileChangeAlbum (index, event) {
      const file = event.target.files[0]
      if (file && file.type.startsWith('audio/')) {
        this.album.songs[index].file = file
      } else {
        alert('Por favor selecciona un archivo de audio válido.')
      }
    },
    handleImageChange (event) {
      const file = event.target.files[0]
      if (file && (file.type === 'image/jpeg' || file.type === 'image/png')) {
        this.song.cover = file
      } else {
        alert('Por favor selecciona una imagen JPEG o PNG.')
      }
    },
    handleAlbumCoverChange (event) {
      const file = event.target.files[0]
      if (file && (file.type === 'image/jpeg' || file.type === 'image/png')) {
        this.album.cover = file
      } else {
        alert('Por favor selecciona una imagen JPEG o PNG.')
      }
    },
    adjustSongCount (delta) {
      this.album.songCount = Math.max(1, this.album.songCount + delta)
      this.initializeAlbumSongs()
    },
    submitSong () {
      // Aquí iría la lógica para enviar el formulario según el tipo de contenido
      if (this.isAlbumUpload) {
        console.log('Subiendo álbum completo:', this.album)
      } else if (this.isAlbum) {
        console.log('Subiendo canción en un álbum:', this.song_title)
        SongService.createSong(this.song_title, this.user_logged.artist_name, this.song_album)
          .then(() => {
            alert('La canción ' + this.song_title + ' con álbum ' + this.song_album + ' se ha subido con éxito.')
            this.$router.push({ path: '/perfil_user', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token } })
            this.$router.go()
          })
          .catch((error) => {
            console.error(error)
            alert('La canción ' + this.song_title + ' ya existe en el sistema.')
          })
      } else {
        console.log('Subiendo single:', this.song_title)
        SongService.createSong(this.song_title, this.user_logged.artist_name, 'Single')
          .then(() => {
            alert('La canción ' + this.song_title + ' se ha subido con éxito.')
            this.$router.push({ path: '/perfil_user', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token } })
            this.$router.go()
          })
          .catch((error) => {
            console.error(error)
            alert('La canción ' + this.song_title + ' ya existe en el sistema.')
          })
      }
    },
    goHome () {
      this.$router.push({ path: '/home', query: {email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token} })
      this.$router.go()
    }
  }
}
</script>

<style scoped>
.add-song {
  background-color: #121212;
  color: white;
  padding: 2rem;
  min-height: 100vh;
}

.add-song-header {
  background: #1f1f1f;
  color: white;
  padding: 2rem;
  text-align: center;
  border-radius: 12px;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  margin-bottom: 2rem;
}

.add-song-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
}

.add-song-header p {
  font-size: 1rem;
  color: #aaa;
  margin-top: 0.5rem;
}

.form-options {
  display: flex;
  justify-content: center; /* Centra los botones */
  gap: 1rem; /* Agrega un espacio entre los botones */
  margin-bottom: 2rem;
}

.form-option {
  padding: 1rem 2rem;
  background-color: #333;
  color: #bbb;
  font-size: 1.2rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.form-option:hover {
  background-color: #ff3d00;
  color: white;
}

.form-option.active {
  background-color: #ff3d00;
  color: white;
}

.add-song-form {
  background-color: #1f1f1f;
  padding: 2rem;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  font-size: 1rem;
  color: #ff3d00;
  font-weight: bold;
}

input[type='text'],
input[type='file'] {
  width: 100%;
  padding: 0.8rem;
  margin-top: 0.5rem;
  background-color: #333;
  border: none;
  border-radius: 5px;
  color: white;
  font-size: 1rem;
}

input[type='text']::placeholder {
  color: #bbb;
}

.btn-submit {
  background-color: #ff3d00;
  color: white;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  width: 100%;
  margin-top: 1.5rem;
}

.btn-submit:hover {
  background-color: #e64a19;
}

.logo-link {
  display: inline-block;
  margin-bottom: 2rem;
}

.logo {
  width: 60px;
  height: auto;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.1);
}

.song-entry {
  border: 1px solid #444;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  background-color: #2d2d2d;
}

.song-entry .form-group {
  margin-bottom: 1rem;
}
/* Botones "+" y "-" */
.song-counter {
  display: flex;
  align-items: center;
  gap: 10px;
}

.btn-counter {
  background-color: #ff3d00;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.btn-counter:disabled {
  background-color: #555;
  cursor: not-allowed;
}

.song-count {
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
}
</style>
