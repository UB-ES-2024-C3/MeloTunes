<template>
    <div class="container">
        <button class="close-btn" @click="cerrarPopup">X</button>

        <img src="Im_logo.png" alt="Logo"><br>
        <h1>Log in to MeloTunes</h1>

        <form id="loginForm" action="#" method="post"> <!-- Añadido id="loginForm" -->
            <label for="email">Email Address</label><br>
            <input type="email" id="email" name="email" placeholder="name@domain.com" required><br>

            <label for="password">Password</label><br>
            <div class="password-container">
                <input type="password" id="password" name="password" placeholder="Password" required>
                <img id="togglePassword" src="Im_ojo2.png" alt="Show/Hide Password">
            </div>

            <div class="error"></div>

            <input type="submit" value="Log In">
        </form>

        <p><a href="#">Forgot your password?</a></p>
        <p>Don't have an account? <a @click="register()">Register for free</a></p>
    </div>

</template>

<script>
export default {
  data () {
  },
  methods: {
    cerrarPopup () {
      this.$router.replace({ path: '/home' })
      this.$router.go()
    },
    login () {
      this.$router.push('/login')
      this.$router.go()
    },
    register () {
      this.$router.push('/register')
      this.$router.go()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
        body {
            background-color: black;
            font-family: Arial, sans-serif;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background-color: #717d7e;
            padding: 20px;
            border-radius: 10px;
            width: 700px;
            position: relative; /* Añadido para posicionar el botón de cerrar */
        }
        .close-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: transparent;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        .container h1 {
            font-size: 24px;
        }
        .container input[type="email"], .container input[type="password"] {
            width: 37%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }
        .password-container {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40%;
            margin: 0px auto;
        }
        .password-container input {
            flex: 1;
            border: none;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            margin: 10px auto;
        }
        .password-container img {
            width: 45px;
            height: 40px;
            margin-left: -45px;
            cursor: pointer;
        }
        .container input[type="submit"] {
            width: 40%;
            padding: 10px;
            margin-top: 10px;
            border: none;
            border-radius: 5px;
            background-color: red;
            color: white;
            font-size: 16px;
        }
        .container a {
            color: white;
            text-decoration: none;
        }
        .container a:hover {
            text-decoration: underline;
        }
        .error {
            color: red;
            font-size: 14px;
        }
        .red-text {
            color: red;
        }
</style>
