import http from '../http-common'
import axios from 'axios'

class UserService {
  getAll () {
    return http.get('/api/v1/users')
      .then((res) => {
        return res
      })
  }
  get () {
    const token = localStorage.getItem('accessToken') // Recuperar token
    if (!token) {
      return Promise.reject(new Error('No token found'))
    }
    return axios.get('http://localhost:8000/api/v1/users/me', {
      headers: {
        Authorization: `Bearer ${token}` // Incluir token en la cabecera
      }
    })
      .then((res) => {
        return res
      })
      .catch((error) => {
        console.error(error)
        if (error.response && error.response.status === 401) {
          throw new Error('Unauthorized. Please log in again.')
        }
        throw error
      })
  }
  getMyFavouriteSongs () {
    const token = localStorage.getItem('accessToken') // Recuperar token
    if (!token) {
      return Promise.reject(new Error('No token found')) // Rechazar si no hay token
    }
    return axios.get('http://localhost:8000/api/v1/users/me/my_songs', {
      headers: {
        Authorization: `Bearer ${token}` // Incluir token en la cabecera
      }
    })
      .then((res) => {
        return res.data // Devolver los datos de la respuesta
      })
      .catch((error) => {
        console.error(error) // Mostrar el error en consola
        if (error.response && error.response.status === 401) {
          throw new Error('Unauthorized. Please log in again.') // Error específico para 401
        }
        throw error // Lanzar otros errores
      })
  }
  addToFavoriteSongs (songId) {
    const token = localStorage.getItem('accessToken') // Recuperar token
    if (!token) {
      return Promise.reject(new Error('No token found')) // Rechazar si no hay token
    }
    const parameters = `song_id=${songId}`
    return axios.patch(`http://localhost:8000/api/v1/users/me/${songId}`, parameters, {
      headers: {
        Authorization: `Bearer ${token}` // Incluir token en la cabecera
      }
    })
      .then((res) => {
        console.log(res)
        return res.data // Devolver los datos de la respuesta
      })
      .catch((error) => {
        console.error(error) // Mostrar el error en consola
        if (error.response && error.response.status === 401) {
          throw new Error('Unauthorized. Please log in again.') // Error específico para 401
        }
        throw error // Lanzar otros errores
      })
  }
  deleteOfFavoriteSongs (songId) {
    const token = localStorage.getItem('accessToken') // Recuperar token
    if (!token) {
      return Promise.reject(new Error('No token found')) // Rechazar si no hay token
    }
    const parameters = `song_id=${songId}`
    return axios.patch(`http://localhost:8000/api/v1/users/me/my_songs/${songId}`, parameters, {
      headers: {
        Authorization: `Bearer ${token}` // Incluir token en la cabecera
      }
    })
      .then((res) => {
        console.log(res)
        return res.data // Devolver los datos de la respuesta
      })
      .catch((error) => {
        console.error(error) // Mostrar el error en consola
        if (error.response && error.response.status === 401) {
          throw new Error('Unauthorized. Please log in again.') // Error específico para 401
        }
        throw error // Lanzar otros errores
      })
  }
}

export default new UserService()
