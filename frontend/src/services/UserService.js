import http from '../http-common'

class UserService {
  getAll () {
    return http.get('/api/v1/users')
      .then((res) => {
        return res
      })
  }
}

export default new UserService()
