<template>
    <body>
        <header>
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
            <button><img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:20%; vertical-align: middle;" > Buscar</button>
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
                <img src="../assets/albumes/dani2.jpeg" alt="Portada del álbum">
              <div class="album-info">
                <p>Pequeño</p>
                <p>Dani Martín</p>
                <p>2010</p>
              </div>
            </div>
            <div class="album">
                <img src="../assets/albumes/dani1.jpeg" alt="Portada del álbum">
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
    }
  }
}
</script>

<style scoped>
    /* Estilos básicos */
    body {
      font-family: 'Poppins', sans-serif;
      margin: 0;
      padding: 0;
      background-color: black;
      color: white;
      padding-top: 80px;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 2%;
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
      background-color: transparent;
      padding: 8% 30px;
      border: 1px solid white;
      border-radius: 25px;
      margin-left: 15px;
      transition: background-color 0.3s ease, color 0.3s ease;
      font-size: 25px;
    }

    header .auth-buttons a:hover {
      background-color: white;
      color: #e53935;
    }

    .body{

      margin: 0;
      padding: 0;
      padding-top: 80px; /* Ajusta el valor según la altura de tu header */

      width: 100%;
      height: 75vh; /* Ocupa toda la altura de la ventana */
      background-image: url('../assets/notas.png');

      background-size: 100% 100%; /* Doble tamaño para que ocupe solo la mitad */
      background-position: left, right;

    }

    .hero {

      text-align: center;
      margin-top: 8%;

    }

    .hero h1 {
      font-size: 10em;
      color: white;
      letter-spacing: 5px;
    }

    .hero h1 .melo {
      color: #e53935;
    }

    .hero h1 .tunes {
      color: white;
    }

    .hero p {
      font-size: 1.5em;
      color: #f5f5f5;
      margin-top: 10px;
    }

    .search-bar {
      display: flex;
      justify-content: center;
      margin: 40px 0;
      margin-bottom: 15%;
      height: 20%;
      margin-top: 6%;

    }

    .search-bar input[type="text"] {
      width: 50%;
      padding: 15px;
      font-size: 2.8em;
      border: none;
      border-radius: 30px;
      margin-right: 0.5%;
      outline: none;
      box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }

    .search-bar button {
      padding: 0.5%;
      font-size: 2.5em;
      background-color: #e53935;
      color: white;
      border: none;
      border-radius: 30px;
      cursor: pointer;
      transition: background-color 0.3s ease;
      width: 10%;
    }

    .search-bar button:hover {
      background-color: #c62828;
    }

    .album-grid {
      display: flex;
      justify-content: center;
      gap: 1%;
      margin-left: 5%;
      margin-right: 5%;
      margin-bottom: 0.5%;
    }
    .album-info {
      display: flex;
      flex-direction: column;
      justify-content: center;

    }
    .album img {
      width: 150px;
      height: 150px;
      border-radius: 10px;
      margin-right: 20px; /* Espacio entre la imagen y el texto */
    }
    .album-info p {
      margin: 0;
      color: white;
      text-align: left;
      font-size: 180%;
    }
    .album {
      display: flex;
      text-align: center;
      padding: 20px;
      background-color: #1f1f1f;
      border-radius: 20px;
      margin-right: 30px;
      min-width: calc(25% - 30px);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .album-item img {
      width: 100%;
      border-radius: 10px;
      margin-bottom: 5px;
    }

    .album-item p {
      margin: 0;
      color: white;
      text-align: center;
    }

    @media screen and (max-width: 900px) {
      .container {
        width: 100%;
      }
    }

    @media screen and (max-width: 500px) {
      .prev,
      .next {
        padding: 5px;
      }
    }
    .artist-section h2 {
      font-size: 5em;
      text-align: center;
      margin-top: 4%;
      margin-bottom: 2.5%;
      color: #e53935;
    }

    .artist-grid {
      display: flex;
      justify-content: center;
      gap: 40px;
      margin-bottom: 5%;
    }

    .artist {
      text-align: center;
      font-size: 180%;
    }

    .artist img {
      border-radius: 50%;
      border: 3px solid #e53935;;
      transition: transform 0.3s ease;
      margin-bottom: 15%;
    }

    .artist img:hover {
      transform: scale(1.1);
    }

    footer {

      background-color: #1f1f1f;
      display: flex;
      justify-content: space-between;
      align-items: center;

    }

    footer .legal, footer .social-icons {
      display: flex;
      align-items: center;


    }

    footer .legal a {
      color: white;
      text-decoration: none;
      margin-right: 2%;
    }

    footer .social-icons img {
      width: 15%;
      margin-right: 0%;
    }
</style>
