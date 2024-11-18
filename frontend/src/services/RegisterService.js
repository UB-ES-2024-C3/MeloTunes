import axios from '../http-common'

class RegisterService {
  registerUser (strEmail, strNombre, strPassword) {
    window.alert(strEmail)
    axios.post('/api/v1/users/', {
      email: strEmail,
      is_active: true,
      is_superuser: false,
      full_name: strNombre,
      password: strPassword
    })
  }
}

export default new RegisterService()
