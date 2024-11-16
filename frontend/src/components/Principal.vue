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
    <div class="auth-buttons" v-if="isLogedIn">
      <a href="#" @click="profile">Ver perfil</a>
    </div>
  </header>
  <div class="hero">
    <h1>
      <span translate="no" class="melo">¡MELO</span><span translate="no" class="tunes">TUNES!</span>
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
    <div class="album">
      <img src="../assets/albumes/melendi1.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>Lágrimas desordenadas</p>
        <p>Melendi</p>
        <p>2012</p>
      </div>
    </div>
    <div class="album">
      <img src="../assets/albumes/dani1.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>Pequeño</p>
        <p>Dani Martín</p>
        <p>2010</p>
      </div>
    </div>
    <div class="album">
      <img src="../assets/albumes/dani2.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>Grandes éxitos y pequeños desastres</p>
        <p>Dani Martín</p>
        <p>2017</p>
      </div>
    </div>
  </div>
  <div class="album-grid">
    <div class="album">
      <img src="../assets/albumes/fito.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>Antes de que cuente diez</p>
        <p>Fito y Fitipaldis</p>
        <p>2009</p>
      </div>
    </div>
    <div class="album">
      <img src="../assets/albumes/fito2.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>Fitografía</p>
        <p>Fito y Fitipaldis</p>
        <p>2017</p>
      </div>
    </div>
    <div class="album">
      <img src="../assets/albumes/ex1.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>Agila</p>
        <p>Extremoduro</p>
        <p>1996</p>
      </div>
    </div>
    <div class="album">
      <img src="../assets/albumes/sabina1.jpeg" alt="Portada del álbum">
      <div class="album-info">
        <p>19 días y 500 noches</p>
        <p>Sabina</p>
        <p>1999</p>
      </div>
    </div>
  </div>

  <div class="artist-section">
    <h2>Artistas Populares</h2>
    <div class="artist-grid">
      <div class="artist">
        <img src="../assets/artistas/melendi.jpeg" alt="Artista" style="width: 100%; height: 100%;">
        <p>Melendi</p>
      </div>
      <div class="artist">
        <img src="../assets/artistas/danimartin.jpeg" alt="Artista" style="width: 100%; height: 100%;">
        <p>Dani Martín</p>
      </div>
      <div class="artist">
        <img src="../assets/artistas/estopa.jpeg" alt="Artista" style="width: 100%; height: 100%;">
        <p>Estopa</p>
      </div>
      <div class="artist">
        <img src="../assets/artistas/fito.jpeg" alt="Artista" style="width: 100%; height: 100%;">
        <p>Fito y Fitipaldis</p>
      </div>
      <div class="artist">
        <img src="../assets/artistas/sabina.jpeg" alt="Artista" style="width: 100%; height: 100%;">
        <p>Sabina</p>
      </div>
      <div class="artist">
        <img src="../assets/artistas/extremoduro.jpeg" alt="Artista" style="width: 100%; height: 100%;">
        <p>Extremoduro</p>
      </div>
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
    },
    profile () {
      this.$router.push({ path: '/perfil_user', query: { email: this.$route.query.email, logged: this.$route.query.logged, token: this.$route.query.token } })
    }
  }
}
</script>

<style scoped>
/* Estilos básicos */
.logo img {
  width: 3.5vw; /* Adaptable */
  margin-top: -2vh;
  margin-left: -1vw;
}

body {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  padding: 0;
  background-color: black;
  color: white;
  padding-top: 17vh; /* Ajuste para adaptarse a la altura del header */
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
  padding: 1.5vh 1vw;
  border: 1px solid white;
  border-radius: 25px;
  margin-left: 1vw;
  transition: background-color 0.3s ease, color 0.3s ease;
  font-size: 1.2rem;
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
  font-size: 6vw;
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
  margin: 10vh 10vh 30vh;
  color: white;
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
  background-color: white;
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
  flex-wrap: wrap;
  gap: 0.5vw;
  margin: 1vh  0.15vw 1vh;

}
.album:hover {
  transform: scale(1.1);
  box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.5);
}

.album img {
  width: 8vw;
  height: 8vw;
  border-radius: 10px;
  margin-right: 0.3vw;
  object-fit: cover;
}
.album img:hover {
  transform: scale(1.1);

}
.album-info {
  display: flex;
  flex-direction: column;
}

.album-info p {
  margin: 0.2vw;
  color: white;
  font-size: 1.8rem;
  text-align: left;
}

.album {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 24vw;
  text-align: center;
  padding: 0.5vh 0.1vw;
  background-color: #1f1f1f;
  border-radius: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.artist-section h2 {
  font-size: 5vw;
  text-align: center;
  margin: 5vh 0 5vh;
  color: #e53935;
}

.artist-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 2vw;
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
  padding: 2vh 2vw;
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
  width: 3vw;
  margin-top: 1vh;
}

footer .legal a {
  color: white;
  text-decoration: none;
  font-size: 1.5rem;
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
