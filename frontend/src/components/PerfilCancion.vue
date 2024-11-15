<template>
  <body>
  <header>
    <div class="logo">
      <img src="../assets/logo2.png" alt="Logo">
    </div>
    <div class="search-bar">
      <input type="text" placeholder="Busca canciones, artistas">
      <button><img src="https://cdn-icons-png.flaticon.com/512/622/622669.png" alt="Buscar" style="width:100%; vertical-align: middle;"></button>
    </div>
  </header>
  <div class="perfil">
    <div class="album">
      <img src="../assets/orozco.jpeg" alt="Album Cover">
    </div>
    <div class="song-info">
      <p class="song-title">Título de la canción</p>
      <p class="song-author">Nombre del autor</p>
      <img src="../assets/reo.png">
    </div>
  </div>
  <div class="information">
    <div class="texto">
      <p>Nombre del álbum</p>
      <p>Año</p>
      <p>Género Musical</p>
    </div>
    <div class="favorito">
      <img src="../assets/me-gusta.png" alt="Favorito">
    </div>
  </div>
  </body>
</template>

<script setup>
export default {
  name: 'PerfilCancion',
  data () {
  }
}
</script>

<style>
/* Estilos del header */
body {
  background-color: #000000;
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
  background-color: #c62828;
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

/* Estilos de perfil */
.perfil {
  height: 80vh;
  display: flex;
  padding: 2vw;
  margin-top: 15vh; /* Ajusta el espacio para que no se sobreponga con el header */
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
}
.song-info img {
  margin-top: -2vh;
  justify-content: center;
  width: 40vw;
}

.song-title {
  font-weight: bold;
  font-size: 5rem;
}

.song-author {
  color: #555;
  font-size: 2rem;
}

/* Estilos de la información del álbum */
.information {
  display: flex;
  align-items: center;
  justify-content: space-between; /* Esto empuja el corazón a la derecha */
  margin-top: -15vh;
  padding: 0 2vw;
}

.texto {
  font-size: 2rem;
}

.favorito img {
  width: 4vw;
  height: 6vh;
  cursor: pointer;
  margin-right: 25vw;
  margin-top: 8vh;
}
</style>
