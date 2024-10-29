<template>
    <body>
      <div id="logo-container">
          <img id="logo" src="~@/assets/Im_logo.png" alt="Melotunes Logo">
      </div>
    </body>
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
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-color: rgb(77, 63, 63);
            font-family: Arial, sans-serif;
            color: white;
        }

        #logo-container {
            opacity: 0;
            animation: fadeInOut 3s forwards;
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
