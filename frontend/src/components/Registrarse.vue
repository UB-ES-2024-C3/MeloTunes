<template>
    <div class="container">
      <button class="close-btn" @click="cerrarPopup">X</button>
      <img src="@/assets/Im_logo.png" alt="Logo"><br>
      <br>
      <h1>Completa tu Registro</h1>

        <form>
            <!-- Campo del correo electrónico -->
            <label for="email">Email</label><br>
            <input type="text" id="email" name="email" placeholder="name@domain.com"><br>

            <!-- Campo de contraseña -->
            <label for="password">Contraseña</label><br>
            <div class="password-container">
                <input type="password" id="password" name="password" placeholder="Introduce tu contraseña">
                <img id="togglePassword" src="Im_ojo2.png" alt="Mostrar/Ocultar Contraseña" @click="togglePassword('password')">
            </div>

            <!-- Campo de confirmar contraseña -->
            <label for="confirm_password">Confirmar Contraseña</label><br>
            <div class="password-container">
                <input type="password" id="confirm_password" name="confirm_password" placeholder="Confirma tu contraseña">
                <img id="toggleConfirmPassword" src="Im_ojo2.png" alt="Mostrar/Ocultar Contraseña" @click="togglePassword('confirm_password')">
            </div>

            <!-- Mostrar error si las contraseñas no coinciden o no se cumplen las condiciones -->
            <div id="error-password" class="error"></div>

            <!-- Campo de nombre -->
            <label for="nombre">Nombre</label><br>
            <input type="text" id="nombre" name="nombre" placeholder="Introduce tu nombre"><br>

            <!-- Campo de nombre de usuario -->
            <label for="usuario">Nombre de Usuario</label><br>
            <input type="text" id="usuario" name="usuario" placeholder="Nombre de usuario"><br>

            <!-- Campo de fecha de nacimiento -->
            <label for="fecha_nacimiento">Fecha de Nacimiento</label><br>
            <input type="date" id="fecha_nacimiento" name="fecha_nacimiento"><br>

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
</template>

<script>

import RegisterService from '../services/RegisterService'

export default {
  name: 'Registrarse',
  data () {
  },
  methods: {
    validateEmail () {
      // eslint-disable-next-line
      if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email)) {
        this.msg['email'] = 'Please enter a valid email address'
      } else {
        this.msg['email'] = ''
      }
    },
    registerUser () {
      RegisterService.registerUser(document.getElementById('email').value, document.getElementById('nombre').value, document.getElementById('password').value)
      this.$router.push('/login')
    },
    cerrarPopup () {
      this.$router.replace({ path: '/home' })
    },
    togglePassword (fieldId) {
      const field = document.getElementById(fieldId)
      field.type = field.type === 'password' ? 'text' : 'password'
    }
  }
}
</script>

<!-- Estilos para el componente -->
<style>
        body {
            background: linear-gradient(to bottom, red, black) !important; /* Fondo degradado de rojo a negro */
            font-family: Arial, sans-serif;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden; /* Evitar el desplazamiento en toda la página */
        }
        .container {
            position: relative;
            text-align: center;
            background-color: #717d7e;
            padding: 20px;
            border-radius: 10px;
            width: 700px;
            max-height: 80vh; /* Limitar la altura para evitar que sea demasiado alta */
            overflow-y: auto; /* Hacer que el contenido sea desplazable solo dentro del recuadro */
        }
        .container h1 {
            font-size: 24px;
        }
        .container input[type="text"],
        .container input[type="date"],
        .container input[type="tel"],
        .container input[type="password"] {
            width: 37%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
        }
        .container input[type="email"] {
            width: 37%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            background-color: #ccc;
            color: #666;
        }
        .password-container {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 37%;
            margin: 0px auto;
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
        .submit-btn {
          width: 37%;
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
        .login-text {
          margin-top: 20px;
          font-size: 15px;
          color: white;
        }
        .login-text a {
          color: #00f;
          text-decoration: underline;
        }
        .login-text a:hover {
          color: yellow;
        }
        .logo {
          width: 100px;
          margin-bottom: 20px;
        }
        .container input[type="submit"] {
            width: 40%;
            padding: 10px;
            margin-top: 10px;
            border: none;
            border-radius: 5px;
            background-color: red;
            color: white;
            font-size: 16px;
        }
        .container a {
            color: white;
            text-decoration: none;
        }
        .container a:hover {
            text-decoration: underline;
        }
        .error {
            color: rgb(187, 255, 41);
            font-size: 14px;
        }
        .error-box {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .close-btn{
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
