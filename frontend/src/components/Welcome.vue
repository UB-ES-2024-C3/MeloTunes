<template>
  <div class="app-container"> <!-- Contenedor raíz único -->
    <div class="background-animation"></div> <!-- Fondo animado -->
    <div id="logo-container">
      <img id="logo" src="../assets/logo1.png" alt="Melotunes Logo">
    </div>
  </div>
</template>

<script>
export default {
  data () {
  },
  created () {
    this.timeout = setTimeout(
      function () {
        this.$router.replace({ path: '/login' })
      }.bind(this),
      3000
    )
  }
}
</script>

<style scoped>
/* Contenedor raíz único */
.app-container {
  position: relative;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
}

/* Fondo animado */
.background-animation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('../assets/fondo.png'); /* Cambia esta ruta según tu archivo de imagen */
  background-size: cover;
  filter: brightness(50%);
  z-index: 0; /* Fondo detrás */
}

body {
  margin: 0;
  height: 100vh;
  font-family: Arial, sans-serif;
  color: white;
  position: relative;
}

/* Contenedor del logo */
#logo-container {
  opacity: 0;
  animation: fadeInOut 3s forwards;
  z-index: 2; /* Asegura que el logo esté encima del fondo */
}

#logo {
  width: 150px;
  height: 150px;
}

h1 {
  margin: 20px 0 0 0;
  font-size: 24px;
  opacity: 0;
  animation: fadeInOutText 3s forwards;
}

@keyframes fadeInOut {
  0% { opacity: 0; }
  50% { opacity: 1; }
  100% { opacity: 0; }
}

@keyframes fadeInOutText {
  0% { opacity: 0; }
  50% { opacity: 1; }
  100% { opacity: 0; }
}
</style>
