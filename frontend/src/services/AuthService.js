import axios from 'axios'

class AuthService {
  login (username, password) {
    console.log('Datos enviados:', { username, password })
    const parameters = `username=${username}&password=${password}`
    const config = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }
    const path = 'http://localhost:8000/api/v1/login/access-token'
    return axios.post(path, parameters, config)
      .then((res) => {
        const token = res.data.access_token // Asegúrate de que el backend devuelva el token aquí
        if (token) {
          localStorage.setItem('accessToken', token) // Guardar token
        }
        return res
      })
      .catch(error => {
        console.error(error)
        throw new Error('Username or Password incorrect')
      })
  }
}

export default new AuthService()
