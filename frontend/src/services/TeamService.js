import http from '../http-common'

class TeamService {
  getAll () {
    return http.get('/api/v1/songs/')
      .then((res) => {
        return res.data
      })
  }
}

export default new TeamService()
