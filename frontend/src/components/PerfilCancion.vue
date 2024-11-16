<template>
  <body >
  <header>
    <div class="logo">
      <img src="../assets/logo2.png" alt="Logo">
    </div>
    <div class="search-bar">
      <input type="text" placeholder="Busca canciones, artistas">
      <button>
        <img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:100%; vertical-align: middle;">
      </button>
    </div>
  </header>
  <div>
    <div class="perfil">
      <div class="album">
        <img src="../assets/orozco.jpeg" alt="Album Cover">
      </div>
      <div class="song-info">
        <p class="song-title">Que me queda</p>
        <p class="song-author">Antonio Orozco </p>
        <img src="../assets/reo.png">
      </div>
    </div>
    <div class="information">
      <div class="texto">
        <p>Renovatio</p>
        <p>2009</p>
        <p>Pop, Hip-hop/Rap, Tropipop</p>
      </div>
      <div class="favorito">
        <img src="../assets/me-gusta.png" alt="Favorito">
      </div>
    </div>
  </div>
  <div>
    <v-app class="main-container">
      <!-- Drawer en la parte derecha con 'persistent' para que no se cierre cuando haga clic fuera -->
      <v-navigation-drawer v-model="drawer" app right persistent style="background-color: #212121; margin-top: 4vh" height="100vh" width="22vw">
        <v-list>
          <v-list-item style="margin-top: 10vh">
            <v-list-item-content>
              <v-list-item-title
                v-for="(item, index) in items"
                :key="index"
                class="item"
                >
                <img src="../assets/orozco.jpeg" alt="Portada del álbum">
                <div class="item-info">
                  <p>{{ item.name }}</p>
                </div>
              </v-list-item-title>

            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main>
        <v-container>
          <!-- Botón con imagen a la derecha y centrado verticalmente -->
          <v-btn color=transparent  @click="toggleDrawer" class="floating-btn" :class="{'move-left': drawer}">
            <img
              src="../assets/avance-rapido.png"
              alt="Botón Imagen"
              height=40
              width="40"
            />
          </v-btn>
        </v-container>
      </v-main>
    </v-app>
  </div>
  </body>

</template>

<script>
export default {
  data () {
    return {
      drawer: false, // Estado del drawer
      items: [
        { name: 'Llévatelo' },
        { name: 'No hay más' },
        { name: 'Pasó' },
        { name: 'Aire en las espaldas' },
        { name: 'Y no hay manera' },
        { name: 'Es mi momento' },
        { name: 'Un poquito de ti' },
        { name: 'Yo sé de ti' },
        { name: 'Ya lo sabes' },
        { name: 'Un lugar' },
        { name: 'No vale dormir' }
      ]
    }
  },
  methods: {
    toggleDrawer () {
      this.drawer = !this.drawer // Alterna el estado del drawer
    }
  }
}
</script>

<style>
::-webkit-scrollbar {
  display: none;
}

.v-main{
  background-color: black;
  padding-top: 15vh;
}
.main-container {
  height: 100vh;

}
.v-navigation-drawer .v-list-item {
  color: white;
}

.v-toolbar {
  background-color: #ffffff;
}

/* Estilo para el botón flotante */
.floating-btn {
  position: absolute; /* Posiciona el botón de manera absoluta */
  top: -40vh; /* Centra verticalmente */
  right: -1vw; /* Coloca el botón a la derecha */
  transform: translateY(-50%); /* Ajusta el botón para centrarlo verticalmente */
  border: none;
  box-shadow: none;
  cursor: pointer;
  width: 5vw;
  height: 10vh !important;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Estilo para mover el botón hacia la izquierda cuando el drawer está abierto */
.floating-btn.move-left {
  transform: translateY(-50%) translateX(-2%); /* Mueve el botón hacia la izquierda cuando el drawer está abierto */
}
.floating-btn:hover, .floating-btn:focus {
  box-shadow: none;
  outline: none;
  background: none;
}
.floating-btn:active {
  outline: none;
  box-shadow: none;
  background-color: transparent;
  transform: none;
}
body {
  background-color: #000000;
  height: 100vh;
  overflow: hidden;
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

/* Estilos de la barra de búsqueda */
.search-bar {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  height: auto;

}

.search-bar input[type="text"] {
  width: 50%;
  padding: 1%;
  font-size: 2rem;
  border: none;
  border-radius: 20px;
  margin-right: 0.5%;
  outline: none;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
  background-color: white;
}

.search-bar button {
  width: 5vw;
  font-size: 1.5rem;
  background-color: #e53935;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-bar button:hover {
  background-color: #ffffff;
}

.search-bar button img {
  width: 200vw;
  height: 2vh;
  object-fit: contain;
  display: block;
}

/* Estilos de logo */
.logo img {
  width: 50%;
  margin-top: -5%;
  margin-left: 10%;
}
.perfil {
  height: 80vh;
  display: flex;
  padding: 2vw;
  margin-top: 15vh;
}

.album img {
  width: 30vw;
  height: 50vh;
  object-fit: cover;
  border-radius: 10px;
}

.song-info {
  display: flex;
  flex-direction: column;
  margin: 0 3vw;
  width: 70vw;
}

.song-info p {
  margin: 1vw 0;
  color: white;
}

.song-info img {
  margin-top: -2vh;
  justify-content: center;
  width: 40vw;
}

.song-title {
  font-weight: bold;
  font-size: 5rem;
  color: white;
}

.song-author {
  color: #ffffff;
  font-size: 2rem;
}

/* Estilos de la información del álbum */
.information {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: -15vh;
  padding: 0 2vw;
  color: white;
}

.texto {
  font-size: 2rem;
}

.favorito img {
  width: 2.7vw;
  height: 5vh;
  cursor: pointer;
  margin-right: 25vw;
  margin-top: 8vh;
}

.item:hover {
  transform: scale(1.1);
  box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.5);
}

.item img {
  width: 5vw;
  height: 5vw;
  border-radius: 10px;
  margin-right: 0.2vw;
  object-fit: cover;
  margin-left: 0.1vw;
  margin-bottom: 2vh;
}
.item img:hover {
  transform: scale(1.1);

}

.item-info p {
  margin: 0.5vw;
  color: white;
  font-size: 1.7rem;
  text-align: left;
}

.item {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 24vw;
  text-align: center;
  padding: 0.5vh -0.9vw;
  background-color: #1f1f1f;
  border-radius: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;

}

      <button><img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:10%; vertical-align: middle;" ></button>
    </div>

  </header>
</template>
<script setup>
export default {
  name: 'PerfilCancion',
  data () {
  }
}
</script>
<style>
  header {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to bottom, #e53935, #000);
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
    transition: top 0.3s;
    z-index: 1000;
  }
  .search-bar {
    flex-grow: 2; /* Aumenta el espacio en la barra de búsqueda para centrar */
    display: flex;
    justify-content: center;
    height: 10vh;
  }
  .search-bar input[type="text"] {
    width: 60%;
    font-size: 1.2rem;
    border: none;
    border-radius: 30px;
    margin-right: 0.5%;
    outline: none;
    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    height: 5vh;
    margin-top: 2vh;

  }
  .search-bar button {
    padding: 0.5%;
    font-size: 2em;
    background-color: #e53935;
    color: white;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width: 8vw;
    height: 5vh;
    margin-top: 2vh;
  }

  .search-bar button:hover {
    background-color: #c62828;
  }

  .logo img {
    width: 50%;
    margin-top: -5%;
    margin-left: 10%;
  }
</style>
