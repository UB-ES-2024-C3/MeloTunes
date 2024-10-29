<template>
  <div>
    <div class="background-animation"></div> <!-- Fondo animado -->

    <div class="container">
      <button class="close-btn" @click="cerrarPopup">X</button>

      <img src="@/assets/Im_logo.png" alt="Logo"><br>
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
            :src="showPassword ? require('@/assets/Im_ojo.png') : require('@/assets/Im_ojo2.png')"
            alt="Show/Hide Password"
            @click="togglePassword"
          >
        </div>

        <div v-if="error" class="error">{{ error }}</div>

        <input type="submit" value="Log In">
      </form>

      <p><a href="#">Forgot your password?</a></p>
      <p>Don't have an account? <a href="/register">Register for free</a></p>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      password: '',
      showPassword: false,
      error: null
    }
  },
  methods: {
    cerrarPopup () {
      this.$router.push('/seleccio_perfils') // Cambia la ruta de Vue Router
    },
    togglePassword () {
      this.showPassword = !this.showPassword
    },
    handleSubmit () {
      if (!this.email || !this.password) {
        this.error = 'Please enter both email and password'
      } else {
        this.error = null
        this.$router.push('/welcome_user') // Cambia la ruta de Vue Router
      }
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
  overflow: hidden; /* Oculta el scroll si el fondo es más grande */
}

/* Fondo animado */
.background-animation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(255, 0, 0, 0.5), rgba(0, 0, 0, 0.8)); /* Gradiente rojo a negro */
  overflow: hidden;
  z-index: 1; /* Asegura que esté detrás del popup */
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
  background-color: #717d7e; /* Fondo del popup */
  padding: 20px;
  margin-top: 5%;
  border-radius: 10px;
  width: 700px;
  position: relative;
  z-index: 10; /* Asegúrate de que esté por encima del fondo */
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

.container input[type="email"],
.container input[type="password"] {
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
  color: red;
  font-size: 14px;
}

.red-text {
  color: red;
}
</style>
