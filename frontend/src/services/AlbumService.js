import axios from '../http-common'

class SongService {
  getAll () {
    return axios.get('/api/v1/albums/')
      .then((res) => {
        return res
      })
  }
  get (albumId) {
    return axios.get(`/api/v1/albums/${albumId}`)
      .then((res) => {
        return res
      })
  }
  deleteAlbum (albumId, userId) {
    return axios.delete(`/api/v1/albums/albums/${albumId}/${userId}`)
      .then((res) => {
        return res
      })
      .catch(error => {
        console.error(error)
        throw new Error('Album not found')
      })
  }
}

export default new SongService()
