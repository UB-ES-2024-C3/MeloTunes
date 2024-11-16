import axios from '../http-common'

class RegisterService {
  registerUser (strEmail, strNombre, strApellido, strPassword) {
    window.alert(strEmail)
    axios.post('/api/v1/users/', {
      email: strEmail,
      is_active: true,
      is_superuser: false,
      first_name: strNombre,
      second_name: strApellido,
      password: strPassword
    })
  }
}

export default new RegisterService()
