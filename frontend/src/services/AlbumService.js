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
}

export default new SongService()
