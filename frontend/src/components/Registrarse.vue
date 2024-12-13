<template>
  <div>
    <div class="background-animation"></div> <!-- Fondo animado -->

    <div class="container">
      <button class="close-btn" @click="cerrarPopup">X</button>
      <img src="../assets/Im_logo.png" alt="Logo"><br>
      <br>
      <h1>Completa tu Registro</h1>

      <form @submit.prevent="handleSubmit" novalidate>
        <!-- Campo del correo electrónico -->
        <label for="email">Email</label><br>
        <input
          type="email"
          id="email"
          v-model="email"
          placeholder="name@domain.com"
          class="form-input"
        ><br>
        <div class="error" v-if="errorEmail">{{ errorEmail }}</div>

        <!-- Campo de contraseña -->
        <label for="password">Contraseña</label><br>
        <div class="password-container">
          <input
            :type="showPassword ? 'text' : 'password'"
            id="password"
            v-model="password"
            placeholder="Introduce tu contraseña"
            class="form-input"
          >
          <img
            :src="showPassword ? require('../assets/ojo.png') : require('../assets/ojo2.png')"
            alt="Mostrar/Ocultar Contraseña"
            @click="togglePassword"
          >
        </div>
        <div class="error" v-if="errorPassword">{{ errorPassword }}</div>

        <!-- Campo de confirmar contraseña -->
        <label for="confirm_password">Confirmar Contraseña</label><br>
        <div class="password-container">
          <input
            :type="showConfirmPassword ? 'text' : 'password'"
            id="confirm_password"
            v-model="confirmPassword"
            placeholder="Confirma tu contraseña"
            class="form-input"
          >
          <img
            :src="showConfirmPassword ? require('../assets/ojo.png') : require('../assets/ojo2.png')"
            alt="Mostrar/Ocultar Contraseña"
            @click="toggleConfirmPassword"
          >
        </div>
        <div class="error" v-if="errorConfirmPassword">{{ errorConfirmPassword }}</div>

        <!-- Campo de nombre -->
        <label for="nombre">Nombre</label><br>
        <input
          type="text"
          id="nombre"
          v-model="firstName"
          placeholder="Introduce tu nombre"
          class="form-input"
        ><br>
        <div class="error" v-if="errorFirstName">{{ errorFirstName }}</div>

        <!-- Campo de apellido -->
        <label for="apellido">Apellido</label><br>
        <input
          type="text"
          id="apellido"
          v-model="lastName"
          placeholder="Introduce tu apellido"
          class="form-input"
        ><br>
        <div class="error" v-if="errorLastName">{{ errorLastName }}</div>

        <!-- Campo de fecha de nacimiento -->
        <label for="fecha_nacimiento">Fecha de Nacimiento</label><br>
        <input
          type="date"
          id="fecha_nacimiento"
          v-model="dob"
          class="form-input"
        ><br>
        <div class="error" v-if="errorDob">{{ errorDob }}</div>

        <!-- Botón de enviar -->
        <input
          type="submit"
          value="Completar Registro"
          class="submit-btn"
        >

        <!-- Texto para iniciar sesión -->
        <p>
          ¿Ya tienes una cuenta? <a href="/login">Inicia sesión aquí</a>
        </p>
      </form>
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
      errorEmail: '',
      errorPassword: '',
      errorConfirmPassword: '',
      errorFirstName: '',
      errorLastName: '',
      errorDob: ''
    }
  },
  methods: {
    cerrarPopup () {
      this.$router.replace({ path: '/home' })
    },
    togglePassword () {
      this.showPassword = !this.showPassword
    },
    toggleConfirmPassword () {
      this.showConfirmPassword = !this.showConfirmPassword
    },
    validateEmail (email) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/ // Regex para validar formato de email
      return regex.test(email)
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
      // Reinicia errores
      this.errorEmail = ''
      this.errorPassword = ''
      this.errorConfirmPassword = ''
      this.errorFirstName = ''
      this.errorLastName = ''
      this.errorDob = ''

      let hasError = false

      // Validaciones
      if (!this.email.trim()) {
        this.errorEmail = 'El campo de correo electrónico no puede estar vacío.'
        hasError = true
      } else if (!this.validateEmail(this.email)) {
        this.errorEmail = 'El formato del correo electrónico no es válido.'
        hasError = true
      }
      if (!this.password.trim()) {
        this.errorPassword = 'La contraseña no puede estar vacía.'
        hasError = true
      } else if (!this.validatePassword(this.password)) {
        this.errorPassword = 'La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula y un número.'
        hasError = true
      }
      if (this.password !== this.confirmPassword) {
        this.errorConfirmPassword = 'Las contraseñas no coinciden.'
        hasError = true
      }
      if (!this.validateName(this.firstName)) {
        this.errorFirstName = 'El nombre solo puede contener letras.'
        hasError = true
      }
      if (!this.validateName(this.lastName)) {
        this.errorLastName = 'El apellido solo puede contener letras.'
        hasError = true
      }
      if (!this.dob.trim()) {
        this.errorDob = 'Debes ingresar tu fecha de nacimiento.'
        hasError = true
      } else if (this.validateAge(this.dob) < 16) {
        this.errorDob = 'Debes tener al menos 16 años para registrarte.'
        hasError = true
      }

      if (hasError) return

      // Si todo está correcto
      RegisterService.registerUser(this.email, this.firstName, this.lastName, this.password)
        .then(() => {
          alert('Registro exitoso!')
          this.$router.push('/login')
          this.$router.go()
        })
        .catch((error) => {
          console.error(error)
          alert('El usuario con email ' + this.email + ' ya está registrado en el sistema.')
        })
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
  height: 100%;
  background: url('../assets/fondo.jpg'); /* Asegúrate de usar una textura sutil */
  background-size: cover;
  filter: brightness(50%);
  z-index: 1;
}

.container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  justify-content: center;
  padding: 20px;
  border-radius: 15px;
  width: 700px;
  height: auto;
  max-height: 80vh;
  overflow-y: auto;
  z-index: 2;
  box-sizing: border-box;
  background-color: rgba(0, 0, 0, 0.5); /* Fondo negro semitransparente */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5); /* Sombra suave */
  color: white; /* Todas las letras blancas */
}

/* Ocultar barra de desplazamiento */
.container::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.container {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.password-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin: 0px auto;
}

.password-container img {
  width: 45px;
  height: 40px;
  margin-left: -45px;
  cursor: pointer;
}

.form-input {
  width: 60%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc; /* Borde gris claro */
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.8); /* Fondo blanco semi-transparente */
  color: black; /* Texto negro para los campos */
  font-size: 16px;
  box-sizing: border-box;
}

.form-input:focus {
  border-color: #007BFF;
  outline: none;
}

.submit-btn {
  width: 60%;
  padding: 15px;
  margin-top: 10px;
  border: none;
  border-radius: 5px;
  background-color: red;
  color: white;
  font-size: 18px;
  cursor: pointer;
}

.submit-btn:hover {
  background-color: darkred;
}

.error {
  color: yellow;
  font-size: 14px;
  font-weight: bold;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
}

.container a {
  color: white;
  text-decoration: none;
}

.container a:hover {
  text-decoration: underline;
}

.close-btn:hover {
  color: #ff4d4d;
}
</style>
