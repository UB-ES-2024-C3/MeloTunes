<template>
  <header>
    <div class="logo">
      <img src="../assets/logo2.png" alt="Logo">
    </div>
    <div class="search-bar">
      <input type="text" placeholder="Busca canciones, artistas">
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
    padding: 1%;
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
    height: 10%;
  }
  .search-bar input[type="text"] {
    width: 60%;
    padding: 3%;
    font-size: 1.2em;
    border: none;
    border-radius: 30px;
    margin-right: 0.5%;
    outline: none;
    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
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
    width: 10%;
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
