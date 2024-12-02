<template>
  <div class="add-song">
    <router-link to="/home" class="logo-link">
      <img src="../assets/Im_logo.png" alt="Logo" class="logo" />
    </router-link>

    <!-- Opciones de formulario -->
    <div class="form-options">
      <div
        :class="['form-option', { active: !isAlbum }]"
        @click="setOption('single')"
      >
        Subir Single
      </div>
      <div
        :class="['form-option', { active: isAlbum }]"
        @click="setOption('album')"
      >
        Subir Canción en un Álbum
      </div>
    </div>

    <!-- Formulario principal -->
    <form class="add-song-form" @submit.prevent="submitSong">
      <!-- Subir Single -->
      <div v-if="!isAlbum">
        <div class="form-group">
          <label for="songTitle">Título de la canción</label>
          <input
            type="text"
            id="songTitle"
            v-model="song.title"
            placeholder="Ingresa el título de la canción"
            required
          />
        </div>
        <div class="form-group">
          <label for="songArtist">Artista</label>
          <input
            type="text"
            id="songArtist"
            v-model="song.artist"
            placeholder="Ingresa el nombre del artista"
            required
          />
        </div>
        <div class="form-group">
          <label for="songFile">Selecciona la canción</label>
          <input
            type="file"
            id="songFile"
            @change="handleFileChange"
            accept="audio/*"
            required
          />
        </div>
        <div class="form-group">
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
            v-model="song.title"
            placeholder="Ingresa el título de la canción"
            required
          />
        </div>
        <div class="form-group">
          <label for="songArtist">Artista</label>
          <input
            type="text"
            id="songArtist"
            v-model="song.artist"
            placeholder="Ingresa el nombre del artista"
            required
          />
        </div>
        <div class="form-group">
          <label for="songAlbum">Álbum</label>
          <input
            type="text"
            id="songAlbum"
            v-model="song.album"
            placeholder="Ingresa el nombre del álbum"
            required
          />
        </div>
        <div class="form-group">
          <label for="songFile">Selecciona la canción</label>
          <input
            type="file"
            id="songFile"
            @change="handleFileChange"
            accept="audio/*"
            required
          />
        </div>
        <div class="form-group">
          <label for="albumCover">Portada del Álbum (PNG, JPEG)</label>
          <input
            type="file"
            id="albumCover"
            @change="handleAlbumCoverChange"
            accept="image/png, image/jpeg"
            required
          />
        </div>
      </div>

      <!-- Botón de envío -->
      <button type="submit" class="btn-submit">
        {{ isAlbum ? 'Subir Canción' : 'Subir Single' }}
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddSong',
  data () {
    return {
      song: {
        title: '',
        artist: '',
        album: '',
        file: null,
        cover: null
      },
      album: {
        title: '',
        artist: '',
        songCount: 1,
        songs: [{ title: '', file: null }]
      },
      isAlbum: false,
      isAlbumUpload: false
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
        console.log('Subiendo canción en un álbum:', this.song)
      } else {
        console.log('Subiendo single:', this.song)
      }
    }
  }
}
</script>

<style scoped>
/* Estilos mantienen la estética original */
.add-song {
  background-color: #121212;
  color: white;
  padding: 2rem;
  min-height: 100vh;
  overflow-y: auto;
}
body {
  margin: 0;
  padding: 0;
  height: 100vh;
  overflow-y: auto;
}
.form-options {
  display: flex;
  justify-content: center;
  gap: 1rem;
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
.form-option:hover,
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
</style>
