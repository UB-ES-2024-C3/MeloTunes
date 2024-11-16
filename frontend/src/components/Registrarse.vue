<template>
  <div>
    <div class="background-animation"></div>

    <div class="container">
      <button class="close-btn" @click="cerrarPopup">X</button>
      <img src="../assets/Im_logo.png" alt="Logo"><br>
      <br>
      <h1>Completa tu Registro</h1>

      <form>
        <!-- Campo del correo electrónico -->
        <label for="email">Email</label><br>
        <input type="text" id="email" name="email" placeholder="name@domain.com" class="form-input"><br>

        <!-- Campo de contraseña -->
        <label for="password">Contraseña</label><br>
        <div class="password-container">
          <input :type="showPassword ? 'text' : 'password'" id="password" name="password" placeholder="Introduce tu contraseña" class="form-input">
          <img :src="showPassword ? require('../assets/ojo.png') : require('../assets/ojo2.png')" alt="Mostrar/Ocultar Contraseña" @click="togglePassword">
        </div>

        <!-- Campo de confirmar contraseña -->
        <label for="confirm_password">Confirmar Contraseña</label><br>
        <div class="password-container">
          <input :type="showConfirmPassword ? 'text' : 'password'" id="confirm_password" name="confirm_password" placeholder="Confirma tu contraseña" class="form-input">
          <img :src="showConfirmPassword ? require('../assets/ojo.png') : require('../assets/ojo2.png')" alt="Mostrar/Ocultar Contraseña" @click="toggleConfirmPassword">
        </div>

        <!-- Mostrar error si las contraseñas no coinciden o no se cumplen las condiciones -->
        <div id="error-password" class="error"></div>

        <!-- Campo de nombre -->
        <label for="nombre">Nombre</label><br>
        <input type="text" id="nombre" name="nombre" placeholder="Introduce tu nombre" class="form-input"><br>

        <!-- Campo de apellido -->
        <label for="apellido">Apellido</label><br>
        <input type="text" id="apellido" name="apellido" placeholder="Introduce tu apellido" class="form-input"><br>

        <!-- Campo de fecha de nacimiento -->
        <label for="fecha_nacimiento">Fecha de Nacimiento</label><br>
        <input type="date" id="fecha_nacimiento" name="fecha_nacimiento" class="form-input"><br>

        <!-- Mostrar error si la persona es menor de 16 años -->
        <div id="error-edad" class="error"></div>

        <!-- Botón de enviar -->
        <input type="button" value="Completar Registro" @click="registerUser()" class="submit-btn">

        <!-- Texto para iniciar sesión -->
        <p class="login-text">
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
      showPassword: false, // Controla la visibilidad de la contraseña
      showConfirmPassword: false // Controla la visibilidad de la confirmación de la contraseña
    }
  },
  methods: {
    cerrarPopup () {
      this.$router.replace({ path: '/home' })
    },
    togglePassword () {
      this.showPassword = !this.showPassword // Alterna el estado del primer campo de contraseña
    },
    toggleConfirmPassword () {
      this.showConfirmPassword = !this.showConfirmPassword // Alterna el estado del segundo campo de contraseña
    },
    registerUser () {
      const email = document.getElementById('email').value
      const nombre = document.getElementById('nombre').value
      const apellido = document.getElementById('apellido').value
      const password = document.getElementById('password').value

      RegisterService.registerUser(email, nombre, apellido, password)
        .then(() => {
          this.$router.push('/login')
        })
        .catch((error) => {
          console.error(error)
          alert('Error al registrar el usuario.')
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
  height: auto; /* Altura automática según contenido */
  max-height: 80vh; /* Limitar la altura máxima */
  overflow-y: auto; /* Permitir desplazamiento interno */
  z-index: 2;
  box-sizing: border-box; /* Asegura que el padding no afecte las dimensiones */
}

/* Ocultar barra de desplazamiento en navegadores modernos */
.container::-webkit-scrollbar {
  width: 0; /* Anchura de la barra de desplazamiento */
  height: 0; /* Altura de la barra de desplazamiento horizontal */
}

.container {
  scrollbar-width: none; /* Firefox: Oculta la barra de desplazamiento */
  -ms-overflow-style: none; /* IE 10+ */
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
  border: none;
  border-radius: 5px;
  font-size: 16px;
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
  color: rgb(187, 255, 41);
  font-size: 14px;
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
</style>
