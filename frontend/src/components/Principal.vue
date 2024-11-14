<template>
  <body>
  <header>
    <div class="logo">
      <img src="../assets/logo2.png" alt="Logo">
    </div>
    <div></div> <!-- Espacio para alinear botones a la derecha -->
    <div class="auth-buttons" v-if="!isLogedIn">
      <a href="#" @click="login">Iniciar sesión</a>
      <a href="#" @click="register">Registrarse</a>
    </div>
  </header>
  <div class="hero">
    <h1>
      <span class="melo">¡MELO</span><span class="tunes">TUNES!</span>
    </h1>
  </div>

  <div class="search-bar">
    <input type="text" placeholder="Busca canciones, artistas">
    <button><img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:20%; vertical-align: middle;"> Buscar</button>
  </div>

  <div class="album-grid">
    <div class="album">
      <img src="../assets/albumes/melendi2.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>Curiosa la cara de tu padre</p>
        <p>Melendi</p>
        <p>2008</p>
      </div>
    </div>
    <!-- Repetir elementos de álbum según sea necesario -->
  </div>

  <div class="artist-section">
    <h2>Artistas Populares</h2>
    <div class="artist-grid">
      <div class="artist">
        <img src="../assets/artistas/melendi.jpeg" alt="Artista" style="width: 100%; height: 100%;">
        <p>Melendi</p>
      </div>
      <!-- Repetir elementos de artista según sea necesario -->
    </div>
  </div>

  <footer>
    <div class="legal">
      <a href="#">Legal</a>
      <a href="#">Política de privacidad</a>
      <a href="#">Configuración de cookies</a>
    </div>
    <div class="social-icons">
      <a href="#"><img src="../assets/facebook.png" alt="Logo de Facebook"></a>
      <a href="#"><img src="../assets/instagram.png" alt="Logo de Instagram"></a>
      <a href="#"><img src="../assets/twitter.png" alt="Logo de Twitter"></a>
    </div>
  </footer>
  </body>
</template>

<script>
export default {
  name: 'Home',
  computed: {
    isLogedIn () {
      return this.$route.query.logged === 'true'
    }
  },
  mounted () {
    if (this.isLogedIn) {
      this.user_name = this.$route.query.email
    }
  },
  data () {
    return {
      user_name: null
    }
  },
  methods: {
    register () {
      this.$router.push('/register')
      this.$router.go()
    },
    login () {
      this.$router.push('/login')
      this.$router.go()
    },
    logOut () {
      this.$router.push('/home')
    }
  }
}
</script>

<style scoped>
/* Estilos básicos */
.logo img {
  width: 30%; /* Adaptable */
  margin-top: -2%;
  margin-left: 5%;
}

body {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  padding: 0;
  background-color: black;
  color: white;
  padding-top: 10vh; /* Ajuste para adaptarse a la altura del header */
}

header {

  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 3vh 2vw;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to bottom, #e53935, #000);
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
  transition: top 0.3s;
  z-index: 1000;
}

header .auth-buttons a {
  text-decoration: none;
  color: white;
  padding: 2vh 1.5vw;
  border: 1px solid white;
  border-radius: 25px;
  margin-left: 1vw;
  transition: background-color 0.3s ease, color 0.3s ease;
  font-size: 1.5rem;
}

header .auth-buttons a:hover {
  background-color: white;
  color: #e53935;
}

.hero {
  text-align: center;
  margin-top: 12vh;
}

.hero h1 {
  font-size: 12vw;
  color: white;
  letter-spacing: 0.5vw;
  margin-bottom: 15vh;
}

.hero h1 .melo {
  color: #e53935;
}

.search-bar {
  display: flex;
  justify-content: center;
  margin: 10vh ;
  margin-bottom: 30vh;
}

.search-bar input[type="text"] {
  width: 60vw;
  padding: 1.2vw;
  font-size: 1.5rem;
  border: none;
  border-radius: 30px;
  margin-right: 1vw;
  outline: none;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
}

.search-bar button {
  padding: 1vh;
  font-size: 1.5rem;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 10vw;

}

.search-bar button:hover {
  background-color: #c62828;
}

.album-grid {
  display: flex;
  justify-content: center;
  gap: 2vw;
  margin: 0 5vw 2vh;
}

.album img {
  width: 15vw;
  height: 15vw;
  border-radius: 10px;
}

.album-info p {
  margin: 0;
  color: white;
  font-size: 1.2rem;
  text-align: left;
}

.album {
  display: flex;
  text-align: center;
  padding: 2vh 1vw;
  background-color: #1f1f1f;
  border-radius: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.artist-section h2 {
  font-size: 5vw;
  text-align: center;
  margin: 4vh 0 2vh;
  color: #e53935;
}

.artist-grid {
  display: flex;
  justify-content: center;
  gap: 5vw;
  margin-bottom: 5vh;
}

.artist {
  text-align: center;
  font-size: 1.2rem;
}

.artist img {
  width: 12vw;
  height: 12vw;
  border-radius: 50%;
  border: 3px solid #e53935;
  transition: transform 0.3s ease;
}

.artist img:hover {
  transform: scale(1.1);
}

footer {
  background-color: #1f1f1f;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2vh 5vw;
}

footer .legal {
  display: flex;
  flex-direction: column;
  gap: 1vh;
  width: 50%;
}

footer .social-icons a {
  display: inline-block;
}

footer .social-icons img {
  width: 5vw;
  margin-top: 1vh;
}

footer .legal a {
  color: white;
  text-decoration: none;
  font-size: 1rem;
}

/* Media Queries para mejorar la adaptabilidad */
@media (max-width: 768px) {
  .hero h1 {
    font-size: 12vw;
  }

  .search-bar input[type="text"] {
    width: 70%;
  }

  .search-bar button {
    width: 15vw;
  }

  .album img, .artist img {
    width: 20vw;
    height: 20vw;
  }

  .artist-section h2 {
    font-size: 6vw;
  }

  .footer .legal a {
    font-size: 1.2rem;
  }
}
</style>
