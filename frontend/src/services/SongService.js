import http from '../http-common'

class SongService {
  getAll () {
    return http.get('/api/v1/songs')
      .then((res) => {
        return res
      })
  }
}

export default new SongService()
