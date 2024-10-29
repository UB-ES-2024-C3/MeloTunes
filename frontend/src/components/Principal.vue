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
            <button><img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width: 20px; vertical-align: middle;"> Buscar</button>
        </div>

        <div class="album-grid">
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
            <div class="album">
                <img src="https://via.placeholder.com/150" alt="Portada del álbum">
                <p>Nombre del álbum</p>
                <p>Nombre del artista</p>
            </div>
        </div>

        <div class="artist-section">
            <h2>Artistas Populares</h2>
            <div class="artist-grid">
                <div class="artist">
                    <img src="https://via.placeholder.com/120" alt="Artista">
                    <p>Artista 1</p>
                </div>
                <div class="artist">
                    <img src="https://via.placeholder.com/120" alt="Artista">
                    <p>Artista 2</p>
                </div>
                <div class="artist">
                    <img src="https://via.placeholder.com/120" alt="Artista">
                    <p>Artista 3</p>
                </div>
                <div class="artist">
                    <img src="https://via.placeholder.com/120" alt="Artista">
                    <p>Artista 4</p>
                </div>
                <div class="artist">
                    <img src="https://via.placeholder.com/120" alt="Artista">
                    <p>Artista 5</p>
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
                <a href="#"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Logo de Facebook"></a>
                <a href="#"><img src="https://cdn-icons-png.flaticon.com/512/733/733558.png" alt="Logo de Instagram"></a>
                <a href="#"><img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Logo de Twitter"></a>
            </div>
        </footer>

    </body>
</template>

<script>
export default {
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
      padding-top: 80px; /* Ajusta el valor según la altura de tu header */
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 30px;
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
      padding: 10px 20px;
      border: 1px solid white;
      border-radius: 5px;
      margin-left: 15px;
      transition: background-color 0.3s ease, color 0.3s ease;
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
      margin: 60px 0;
    }

    .hero h1 {
      font-size: 4em;
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

      background-image: url("../assets/notas.png") ;
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-size: cover;
      color: #000;
    }

    .search-bar input[type="text"] {
      width: 40%;
      padding: 15px;
      font-size: 1.1em;
      border: none;
      border-radius: 30px;
      margin-right: 10px;
      outline: none;
      box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }

    .search-bar button {
      padding: 15px 25px;
      font-size: 1em;
      background-color: #e53935;
      color: white;
      border: none;
      border-radius: 30px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .search-bar button:hover {
      background-color: #c62828;
    }

    /* Estilos del carrusel de álbumes */
    .album-carousel {
      position: relative;
      overflow: hidden;
      width: 90%;
      margin: 70px ;
    }

    .album-container {
      display: flex;
      transition: transform 0.5s ease;
      width: 300%; /* Ajustamos el tamaño del contenedor para que se pueda deslizar */
    }

    .mySlides {
      display: flex;
      justify-content: space-between;
      width: 33.33%; /* Cada slide ocupa 1/3 del contenedor */
    }
    .album {
      text-align: center;
      padding: 20px;
      background-color: #1f1f1f;
      border-radius: 20px;
      margin-right: 30px;
      min-width: calc(25% - 30px);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .album-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 23%; /* Cada imagen ocupará el 23% del ancho de la slide */
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

    .prev,
    .next {
      cursor: pointer;
      position: absolute;
      top: 50%;
      width: auto;
      margin-top: -22px;
      padding: 16px;
      color: #fff;
      font-weight: bold;
      font-size: 18px;
      transition: 0.6s ease;
      border-radius: 0 3px 3px 0;
      user-select: none;
      border: solid #fff 2px;
    }

    .next {
      right: 0;
      border-radius: 3px 0 0 3px;
    }

    .prev:hover,
    .next:hover {
      background-color: rgba(0, 0, 0, 0.8);
    }

    .elements {
      text-align: center;
      margin-top: 20px;
    }

    .quadrate {
      cursor: pointer;
      height: 4px;
      width: 50px;
      margin: 0 2px;
      background-color: #717171;
      display: inline-block;
      transition: background-color 0.6s ease;
      border-radius: 2px;
    }

    .active,
    .quadrate:hover {
      background-color: #fff;
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
      font-size: 2.5em;
      text-align: center;

      color: #e53935;
    }

    .artist-grid {
      display: flex;
      justify-content: center;
      gap: 40px;
    }

    .artist {
      text-align: center;
    }

    .artist img {
      width: 180px;
      height: 180px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid #e53935;
      transition: transform 0.3s ease;
    }

    .artist img:hover {
      transform: scale(1.1);
    }

    footer {
      background-color: #1f1f1f;
      padding: 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
    }

    footer .legal, footer .social-icons {
      display: flex;
      align-items: center;
    }

    footer .legal a {
      color: white;
      text-decoration: none;
      margin-right: 20px;
    }

    footer .social-icons img {
      width: 30px;
      margin-left: 15px;
    }
</style>
