<template>
    <div class="container">
        <h1>Complete Your Registration</h1>

        <form>
            <!-- Mostrar el correo del paso anterior que no se puede modificar -->
            <label for="email">Email</label><br>
            <input type="text" id="email" name="email" placeholder="name@domain.com"><br>

            <!-- Campo de contraseña -->
            <label for="password">Password</label><br>
            <div class="password-container">
                <input type="password" id="password" name="password" placeholder="Enter your password">
                <img id="togglePassword" src="Im_ojo2.png" alt="Show/Hide Password">
            </div>

            <!-- Campo de confirmar contraseña -->
            <label for="confirm_password">Confirm Password</label><br>
            <div class="password-container">
                <input type="password" id="confirm_password" name="confirm_password" placeholder="Confirm your password">
                <img id="toggleConfirmPassword" src="Im_ojo2.png" alt="Show/Hide Password">
            </div>

            <!-- Mostrar error si las contraseñas no coinciden o no se cumplen las condiciones -->
            <div id="error-password" class="error"></div>

            <!-- Campo de nombre -->
            <label for="nombre">First Name</label><br>
            <input type="text" id="nombre" name="nombre" placeholder="Enter your first name"><br>

            <!-- Campo de nombre de usuario -->
            <label for="usuario">Username</label><br>
            <input type="text" id="usuario" name="usuario" placeholder="Username"><br>

            <!-- Campo de fecha de nacimiento -->
            <label for="fecha_nacimiento">Date of Birth</label><br>
            <input type="date" id="fecha_nacimiento" name="fecha_nacimiento"><br>

            <!-- Mostrar error si la persona es menor de 16 años -->
            <div id="error-edad" class="error"></div>

            <!-- Botón de enviar -->
            <input type="button" value="Complete Registration" @click=registerUser()>

            <button class="close-btn" @click="cerrarPopup()">X</button>
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
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
        body {
            background-color: black;
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
            pointer-events: none; /* El correo no será editable */
        }
        .password-container {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40%;
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
</style>
