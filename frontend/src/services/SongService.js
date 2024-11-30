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
}

export default new SongService()
