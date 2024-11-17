<template>
  <div>
    <div class="background-animation"></div> <!-- Fondo animado -->

    <div class="container">
      <button class="close-btn" @click="cerrarPopup">X</button>

      <img src="../assets/Im_logo.png" alt="Logo"><br>
      <h1>Register to MeloTunes</h1>

      <form @submit.prevent="handleSubmit">
        <label for="email">Email</label><br>
        <input type="email" v-model="email" placeholder="name@domain.com" required><br>

        <label for="password">Password</label><br>
        <div class="password-container">
          <input
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            placeholder="Password"
            required
          />
          <img
            :src="showPassword ? require('../assets/ojo.png') : require('../assets/ojo2.png')"
            alt="Show/Hide Password"
            @click="togglePassword"
          >
        </div>

        <label for="confirmPassword">Confirm Password</label><br>
        <div class="password-container">
          <input
            :type="showConfirmPassword ? 'text' : 'password'"
            v-model="confirmPassword"
            placeholder="Confirm Password"
            required
          />
          <img
            :src="showConfirmPassword ? require('../assets/ojo.png') : require('../assets/ojo2.png')"
            alt="Show/Hide Confirm Password"
            @click="toggleConfirmPassword"
          >
        </div>

        <label for="name">First Name</label><br>
        <input type="text" v-model="firstName" placeholder="First Name" required><br>

        <label for="surname">Last Name</label><br>
        <input type="text" v-model="lastName" placeholder="Last Name" required><br>

        <label for="dob">Date of Birth</label><br>
        <input type="date" v-model="dob" required><br>

        <button type="submit" class="red-button">Log in</button>

        <!-- Texto para iniciar sesión -->
        <p>¿Ya tienes una cuenta? <a href="/login">Inicia sesión aquí</a>
        </p>
      </form>

      <!-- Popup de errores -->
      <div v-if="error" class="error-popup">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script>

import RegisterService from '../services/RegisterService'

export default {
  name: 'Registrarse',
  data () {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      firstName: '',
      lastName: '',
      dob: '',
      showPassword: false,
      showConfirmPassword: false,
      error: null
    }
  },
  methods: {
    registerUser () {
      RegisterService.registerUser(this.email, this.firstName, this.lastName, this.password)
        .then(response => {
          alert('Se ha registrado correctamente al usuario con email ' + this.email + '.')
          this.$router.push('/login')
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          alert('El usuario con email ' + this.email + ' ya está registrado en el sistema.')
        })
    },

    cerrarPopup () {
      this.$router.push('/home') // Cambia la ruta de Vue Router
    },
    togglePassword () {
      this.showPassword = !this.showPassword
    },
    toggleConfirmPassword () {
      this.showConfirmPassword = !this.showConfirmPassword
    },
    validatePassword (password) {
      const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/ // Regex para validar contraseña
      return regex.test(password)
    },
    validateName (name) {
      const regex = /^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$/ // Solo letras y espacios
      return regex.test(name)
    },
    validateAge (dob) {
      const birthDate = new Date(dob)
      const today = new Date()
      const age = today.getFullYear() - birthDate.getFullYear()
      const monthDifference = today.getMonth() - birthDate.getMonth()
      if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        return age - 1
      }
      return age
    },
    handleSubmit () {
      // Validaciones
      if (!this.email.trim() || !this.password.trim() || !this.confirmPassword.trim() || !this.firstName.trim() || !this.lastName.trim() || !this.dob) {
        this.error = 'Please complete all fields.'
        return
      }

      if (!this.validatePassword(this.password)) {
        this.error = 'Password must be at least 8 characters long, contain a capital letter, a lowercase letter, and a number.'
        return
      }

      if (this.password !== this.confirmPassword) {
        this.error = 'Passwords do not match.'
        return
      }

      if (!this.validateName(this.firstName)) {
        this.error = 'First Name can only contain letters.'
        return
      }

      if (!this.validateName(this.lastName)) {
        this.error = 'Last Name can only contain letters.'
        return
      }

      if (this.validateAge(this.dob) < 16) {
        this.error = 'You must be at least 16 years old to register.'
        return
      }

      // Limpia el error si todas las validaciones pasan
      this.error = null

      // Simular registro o llamar a un servicio
      this.registerUser()
    }
  }
}
</script>

<style scoped>
body, html {
  background-color: black;
  font-family: Arial, sans-serif;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  overflow: hidden;
}

/* Fondo animado */
.background-animation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 150%;
  background: radial-gradient(circle, rgba(255, 0, 0, 0.5), rgba(0, 0, 0, 0.8));
  overflow: hidden;
  z-index: 1;
}

.background-animation::before {
  content: '';
  position: absolute;
  width: 200%;
  height: 200%;
  background-image: linear-gradient(60deg, rgba(255, 0, 0, 0.3) 25%, transparent 25%, transparent 75%, rgba(255, 0, 0, 0.3) 75%);
  background-size: 30px 30px;
  animation: move 4s linear infinite;
}

@keyframes move {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 30px 30px;
  }
}

.container {
  text-align: center;
  justify-content: center;
  background-color: #717d7e;
  padding: 20px;
  margin-top: 5%;
  border-radius: 10px;
  width: 700px;
  position: relative;
  z-index: 10;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: transparent;
  color: white;
  font-size: 20px;
  font-weight: bold;
  border: none;
  cursor: pointer;
}

.container h1 {
  font-size: 24px;
}

.container input {
  width: 37%;
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}

.password-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40%;
  margin: 0 auto;
}

.password-container input {
  flex: 1;
  border: none;
  padding: 10px;
  border-radius: 5px;
  font-size: 16px;
  margin: 10px auto;
}

.password-container img {
  width: 45px;
  height: 40px;
  margin-left: -45px;
  cursor: pointer;
}

.red-button {
  background-color: red;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
}
.container a {
  color: white;
  text-decoration: none;
}

.container a:hover {
  text-decoration: underline;
}

.error-popup {
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #ff4c4c;
  color: white;
  padding: 20px;
  border-radius: 10px;
  font-weight: bold;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  z-index: 1000;
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
