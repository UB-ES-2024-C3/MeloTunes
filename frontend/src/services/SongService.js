import axios from '../http-common'

class SongService {
  getAll () {
    return axios.get('/api/v1/songs/')
      .then((res) => {
        return res
      })
  }
  get (songId) {
    return axios.get(`/api/v1/songs/${songId}`)
      .then((res) => {
        return res
      })
  }
  createSong (title, artist, album) {
    const now = new Date(); // Fecha y hora actual
    const timestamp = now.toISOString(); // Formato ISO 8601
    return axios.post('/api/v1/songs/', {
      title: title,
      artist: artist,
      album: album,
      duration: '00:04:05', // Duración como cadena
      timestamp: timestamp
    })
      .then((res) => {
        return res
      })
      .catch(error => {
        console.error(error)
        throw new Error('The song already exists in the system.')
      })
  }
}

export default new SongService()
