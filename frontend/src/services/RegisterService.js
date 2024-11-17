import axios from '../http-common'

class RegisterService {
  registerUser (strEmail, strNombre, strApellido, strPassword) {
    return axios.post('/api/v1/users/', {
      email: strEmail,
      is_active: true,
      is_superuser: false,
      first_name: strNombre,
      second_name: strApellido,
      password: strPassword
    })
    .then((res) => {
      return res
    })
    .catch(error => {
      console.error(error)
      throw new Error('Email no disponible')
    })
  }
}

export default new RegisterService()
