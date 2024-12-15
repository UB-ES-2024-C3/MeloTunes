import axios from '../http-common'

class UserService {
  getAll () {
    return axios.get('/api/v1/users/')
      .then((res) => {
        return res
      })
  }
  get () {
    const token = localStorage.getItem('accessToken') // Recuperar token
    if (!token) {
      return Promise.reject(new Error('No token found'))
    }
    return axios.get('/api/v1/users/me', {
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
  getMyFavouriteSongs (userId) {
    return axios.get(`/api/v1/users/me/fav_songs/${userId}`, {
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
  addToFavoriteSongs (songId, userId) {
    return axios.patch(`/api/v1/users/me/favs/${songId}/${userId}`)
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
  deleteOfFavoriteSongs (songId, userId) {
    return axios.patch(`/api/v1/users/me/fav_songs/${songId}/${userId}`)
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
  updateUser (userId, strNombre, strApellido, strBiografia) {
    return axios.patch(`/api/v1/users/${userId}`, {
      first_name: strNombre,
      second_name: strApellido,
      description: strBiografia
    })
      .then((res) => {
        return res
      })
      .catch(error => {
        console.error(error)
        throw new Error('No disponible')
      })
  }
  getbyArtist (artistName) {
    return axios.get(`/api/v1/users/artist/${artistName}`)
      .then((res) => {
        return res
      })
  }
}

export default new UserService()
