<template>
  <div class="add-song">
    <router-link to="/home" class="logo-link">
      <img src="../assets/Im_logo.png" alt="Logo" class="logo" />
    </router-link>

    <header class="add-song-header">
      <h1>Subir una Canción o Álbum</h1>
      <p>Selecciona una opción y completa los detalles para subir la canción o el álbum.</p>
    </header>

    <div class="form-options">
      <div
        :class="['form-option', { 'active': !isAlbum && !isAlbumUpload }]"
        @click="setOption('single')"
      >
        Subir Single
      </div>
      <div
        :class="['form-option', { 'active': isAlbum && !isAlbumUpload }]"
        @click="setOption('album')"
      >
        Subir Canción en un Álbum
      </div>
      <div
        :class="['form-option', { 'active': isAlbumUpload }]"
        @click="setOption('uploadAlbum')"
      >
        Subir Álbum Completo
      </div>
    </div>

    <form class="add-song-form" @submit.prevent="submitSong">
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

      <!-- Campos específicos para "Subir Canción en un Álbum" -->
      <div v-if="isAlbum" class="form-group">
        <label for="songAlbum">Álbum</label>
        <input
          type="text"
          id="songAlbum"
          v-model="song.album"
          placeholder="Ingresa el nombre del álbum"
          required
        />
      </div>

      <!-- Campo común para ambos: Archivo de la canción -->
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

      <!-- Campo de portada solo aparece si se selecciona "Subir Single" -->
      <div v-if="!isAlbum && !isAlbumUpload" class="form-group">
        <label for="albumCover">Portada del Single (PNG, JPEG)</label>
        <input
          type="file"
          id="albumCover"
          @change="handleImageChange"
          accept="image/png, image/jpeg"
        />
      </div>

      <div v-if="isAlbumUpload" class="form-group">
        <label for="songCount">Número de Canciones</label>
        <input
          type="number"
          id="songCount"
          v-model="album.songCount"
          min="1"
          placeholder="Número de canciones en el álbum"
          @change="updateSongCount"
          required
        />
      </div>

      <!-- Carrusel de canciones para "Subir Álbum Completo" -->
      <div v-if="isAlbumUpload">
        <div
          v-for="(songItem, index) in album.songs"
          :key="index"
          class="song-entry"
        >
          <div class="form-group">
            <label :for="'songTitle_' + index">Título de la canción {{ index + 1 }}</label>
            <input
              type="text"
              :id="'songTitle_' + index"
              v-model="songItem.title"
              placeholder="Ingresa el título de la canción"
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

          <!-- Botón para eliminar canción -->
          <button type="button" @click="removeSong(index)" class="btn-remove">
            Eliminar Canción
          </button>
        </div>
      </div>
      <button type="submit" class="btn-submit">
        {{ isAlbumUpload ? 'Subir Álbum' : (isAlbum ? 'Subir Canción' : 'Subir Single') }}
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
        songCount: 1,
        songs: [{ title: '', artist: '', file: null }]
      },
      isAlbum: false,
      isAlbumUpload: false
    }
  },
  methods: {
    setOption (option) {
      this.isAlbum = option === 'album'
      this.isAlbumUpload = option === 'uploadAlbum'
      if (this.isAlbumUpload && !this.album.songs.length) {
        this.album.songs = Array.from({ length: this.album.songCount }, () => ({
          title: '',
          artist: '',
          file: null
        }))
      }
    },
    handleFileChange (event) {
      const file = event.target.files[0]
      if (file && file.type.startsWith('audio/')) {
        this.song.file = file
      } else {
        alert('Por favor selecciona un archivo de audio válido.')
        this.song.file = null
      }
    },
    handleFileChangeAlbum (index, event) {
      const file = event.target.files[0]
      if (file && file.type.startsWith('audio/')) {
        this.album.songs[index].file = file
      } else {
        alert('Por favor selecciona un archivo de audio válido.')
        this.album.songs[index].file = null
      }
    },
    updateSongCount () {
      const songCount = this.album.songCount
      if (songCount > this.album.songs.length) {
        for (let i = this.album.songs.length; i < songCount; i++) {
          this.album.songs.push({ title: '', artist: '', file: null })
        }
      } else {
        this.album.songs.splice(songCount)
      }
    },
    removeSong (index) {
      this.album.songs.splice(index, 1)
      this.album.songCount = this.album.songs.length
    },
    handleImageChange (event) {
      const file = event.target.files[0]
      if (file && (file.type === 'image/png' || file.type === 'image/jpeg')) {
        this.song.cover = file
      } else {
        alert('Por favor selecciona una imagen en formato PNG o JPEG.')
        this.song.cover = null
      }
    },
    submitSong () {
      if (this.isAlbumUpload) {
        if (this.album.songs.every(song => song.file)) {
          console.log('Álbum subido:', this.album)
          this.album = { title: '', songCount: 1, songs: [{ title: '', artist: '', file: null }] }
          alert('¡Álbum subido exitosamente!')
        } else {
          alert('Por favor selecciona un archivo para cada canción.')
        }
      } else if (this.song.file) {
        console.log('Canción subida:', this.song)
        this.song = { title: '', artist: '', album: '', file: null, cover: null }
        alert('¡Canción subida exitosamente!')
      } else {
        alert('Por favor selecciona un archivo de canción.')
      }
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
.btn-remove {
  background-color: #e64a19;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 1rem;
}

.btn-remove:hover {
  background-color: #d43f00;
}
</style>
