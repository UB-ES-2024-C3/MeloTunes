<template>
  <body>
  <form @submit.prevent="handleSubmit" novalidate>
  <div class="container">
    <h1>Cambia tu contraseña</h1>
    <label class="email" for="email">Email</label><br>
    <input type="email" v-model="email" placeholder="name@domain.com" required class="form-input"><br>
    <button type="submit" class="submit-btn" @click="enviaremail">Recibir email</button>
    <button class="close-btn" @click="cerrarPopup">X</button>
  </div>
  </form>
  </body>
</template>

<script>
import RegisterService from '../services/RegisterService'

export default {
  data () {
    return {
      email: '',
      token: null,
      is_authenticated: false,
      error: null
    }
  },
  methods: {
    cerrarPopup () {
      this.$router.push('/login')
      this.$router.go()
    },

    handleSubmit () {
      // Reinicia errores
      this.errorEmail = ''

      let hasError = false

      // Validaciones
      if (!this.email.trim()) {
        this.errorEmail = 'El campo de correo electrónico no puede estar vacío.'
        hasError = true
      } else if (!this.validateEmail(this.email)) {
        this.errorEmail = 'El formato del correo electrónico no es válido.'
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
    },
    validateEmail (email) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/ // Regex para validar formato de email
      return regex.test(email)
    }
  }
}
</script>

<style scoped>
body, html {
  background: url('../assets/fondo.jpg');
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  overflow: hidden;
}

.container {
  color: white;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  justify-content: center;
  background-color: #717d7e;
  padding: 20px;
  border-radius: 15px;
  width: 700px;
  height: auto;
  max-height: 80vh;
  overflow-y: auto;
  z-index: 2;
  box-sizing: border-box;
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

.close-btn:hover {
  color: #ff4d4d;
}

.container input[type="email"],
.container .form-input {
  width: 60%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc; /* Borde gris claro */
  border-radius: 5px;
  background-color: white; /* Fondo blanco */
  color: black; /* Texto negro */
  font-size: 16px;
  box-sizing: border-box; /* Asegura que el padding no desborde */
}

.container input:focus {
  border-color: #007BFF; /* Borde azul al hacer foco */
  outline: none; /* Elimina el borde predeterminado del navegador */
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

.container a {
  color: white;
  text-decoration: none;
}

.container a:hover {
  text-decoration: underline;
}

.error {
  color: yellow;
  font-size: 14px;
  font-weight: bold;
}
.email{

}
</style>
