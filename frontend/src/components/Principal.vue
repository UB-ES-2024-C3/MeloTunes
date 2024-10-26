<template>
    <body>
        <header>
            <div></div> <!-- Espacio para alinear botones a la derecha -->
            <div>
                <a href="#">Iniciar sesión</a>
                <a href="#" @click="register">Registrarse</a>
            </div>
        </header>

        <div class="logo">
            <h1>
                <span class="color-izquierda">¡MELO</span>
                <span class="color-derecha">TUNES!</span>
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
  data () {
  },
  methods: {
    register () {
      this.$router.push('/register')
      this.$router.go()
    }
  }
}
</script>

<style scoped>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: black;
        }

        header {
            display: flex;
            justify-content: space-between;
            padding: 20px;
            background-color: rgb(225, 58, 58);
            /* Degradado en el borde inferior del header */
            box-shadow: 0px 10px 20px -10px rgba(225, 58, 58, 0.5);
        }

        header a {
            text-decoration: none;
            color: #333;
            border: 1px solid #333;
            padding: 10px 20px;
            margin-left: 10px;
            border-radius: 5px;
        }

        .logo {
            text-align: center;
            margin: 40px 0;
        }

        .logo h1 {
            font-size: 2.5em;
            margin: 0;
        }

        .search-bar {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }

        .search-bar input[type="text"] {
            width: 50%;
            padding: 10px;
            font-size: 1.1em;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-right: 10px;
        }

        .search-bar button {
            padding: 10px 20px;
            font-size: 1em;
            background-color: red;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .album-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 40px;
        }

        .album {
            text-align: center;
            border: 1px solid #ddd;
            padding: 10px;
            background-color: white;
            border-radius: 10px;
        }

        .album img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
        }

        .artist-section {
            margin: 40px;
            text-align: center;
        }

        .artist-section h2 {
            margin-bottom: 20px;
        }

        .artist-grid {
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        .artist {
            text-align: center;
        }

        .artist img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #ddd;
        }

        .artist p {
            margin-top: 10px;
        }

        footer {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }

        footer .legal {
            text-align: left;
        }

        footer .legal a {
            color: white;
            text-decoration: none;
            margin-right: 15px;
        }

        footer .social-icons img {
            width: 30px;
            margin-left: 10px;
        }

        /* Estilo para el logo con dos colores */
        .color-izquierda {
            color: red;
        }

        .color-derecha {
            color: white;
        }
</style>
