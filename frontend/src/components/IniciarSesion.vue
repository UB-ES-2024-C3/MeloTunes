<template>
  <div>
    <div class="background-animation"></div> <!-- Fondo animado -->

    <div class="container">
      <button class="close-btn" @click="cerrarPopup">X</button>

      <img src="../assets/Im_logo.png" alt="Logo"><br>
      <h1>Inicia sesión en MeloTunes</h1>

      <form @submit.prevent="handleSubmit" novalidate>
        <label for="email">Email</label><br>
        <input type="email" v-model="email" placeholder="name@domain.com" required class="form-input"><br>

        <label for="password">Contraseña</label><br>
        <div class="password-container">
          <input
            :type="showPassword ? 'text' : 'password'"
            id="password"
            v-model="password"
            placeholder="Contraseña"
            required
            class="form-input"
          >
          <img
            :src="showPassword ? require('../assets/ojo.png') : require('../assets/ojo2.png')"
            alt="Mostrar/Ocultar Contraseña"
            @click="togglePassword"
          >
        </div>

        <div v-if="error" class="error">{{ error }}</div>

        <button type="submit" class="submit-btn">Inicia sesión</button>
      </form>

      <p><a href="#">¿Has olvidado la contraseña?</a></p>
      <p>¿No tienes una cuenta? <a href="/register">Regístrate gratis</a></p>
    </div>
  </div>
</template>

<script>
import AuthService from '../services/AuthService'
export default {
  data () {
    return {
      email: '',
      password: '',
      showPassword: false,
      token: null,
      is_authenticated: false,
      error: null
    }
  },
  methods: {
    cerrarPopup () {
      this.$router.push('/home')
      this.$router.go()
    },
    login () {
      AuthService.login(this.email, this.password)
        .then(response => {
          this.is_authenticated = true
          this.token = response.data.access_token
          this.$router.push({ path: '/home', query: { email: this.email, logged: this.is_authenticated, token: this.token } })
          this.$router.go()
        })
        .catch((error) => {
          console.error(error)
          this.error = 'Correo o contraseña incorrectos'
        })
    },
    togglePassword () {
      this.showPassword = !this.showPassword
    },
    handleSubmit () {
      if (!this.email.trim() || !this.password.trim()) {
        this.error = 'Por favor, complete todos los campos'
        return
      }
      this.error = null
      this.login()
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
background: url('../assets/fondo.jpg');
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
background-color: rgba(255, 255, 255, 0.8); /* Fondo blanco semi-transparente */
color: black; /* Texto negro para los campos */
font-size: 16px;
box-sizing: border-box; /* Asegura que el padding no desborde */
}

.container input:focus {
border-color: #007BFF; /* Borde azul al hacer foco */
outline: none; /* Elimina el borde predeterminado del navegador */
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

/* Media Query para pantallas pequeñas */
@media (max-width: 768px) {
  .container {
    width: 90%;
    padding: 15px;
  }

  .container input[type="email"],
  .container .form-input,
  .submit-btn {
    width: 80%;
  }

  .close-btn {
    font-size: 20px;
  }

  .password-container img {
    width: 35px;
    height: 30px;
  }

  .container h1 {
    font-size: 20px;
  }

  .error {
    font-size: 12px;
  }
}

</style>
