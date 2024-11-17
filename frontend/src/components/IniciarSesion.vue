<template>
  <div>
    <div class="background-animation"></div> <!-- Fondo animado -->

    <div class="container">
      <button class="close-btn" @click="cerrarPopup">X</button>

      <img src="../assets/Im_logo.png" alt="Logo"><br>
      <h1>Log in to MeloTunes</h1>

      <form @submit.prevent="handleSubmit">
        <label for="email">Email Address</label><br>
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

        <div v-if="error" class="error">{{ error }}</div>

        <button type="submit" class="submit-btn">Log in</button>
      </form>

      <p><a href="#">Forgot your password?</a></p>
      <p>Don't have an account? <a href="/register">Register for free</a></p>
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
      this.$router.push('/home') // Cambia la ruta de Vue Router
    },
    login () {
      AuthService.login(this.email, this.password)
        .then(response => {
          this.is_authenticated = true
          this.token = response.data.access_token
          this.$router.push({ path: '/home', query: { email: this.email, logged: this.is_authenticated, token: this.token } })
        })
        .catch((error) => {
          console.error(error)
          alert('Username or Password incorrect')
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

.container h1 {
  font-size: 24px;
}

.container input[type="email"],
.container input[type="password"] {
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

.container input[type="email"]:focus,
.container input[type="password"]:focus {
  border-color: #007BFF; /* Borde azul al hacer foco */
  outline: none; /* Elimina el borde predeterminado del navegador */
}

.password-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%; /* Asegura alineación */
  margin: 10px auto; /* Espaciado */
}

.password-container img {
  width: 45px;
  height: 40px;
  margin-left: -45px; /* Superposición del ícono */
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
  color: red;
  font-size: 14px;
}
</style>
