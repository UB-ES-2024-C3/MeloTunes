no, simplemente esconde el boton de cambiar cuando se le de y aparezcan los campos nuevos: <template>
  <body>
  <form @submit.prevent="handleSubmit" novalidate>
    <div class="container">
      <h1>Cambia tu contraseña</h1>

      <!-- Email -->
      <label class="email" for="email">Email</label><br>
      <input type="email" v-model="email" placeholder="name@domain.com" required class="form-input" :disabled="isChangingPassword"><br>

      <!-- Mostrar los campos de contraseña solo cuando el usuario haga clic en 'Cambiar' -->
      <div v-if="isChangingPassword">
        <label for="newPassword">Nueva contraseña</label><br>
        <input type="password" v-model="newPassword" placeholder="Nueva contraseña" required class="form-input"><br>

        <!-- Confirmar nueva contraseña -->
        <label for="confirmPassword">Confirmar nueva contraseña</label><br>
        <input type="password" v-model="confirmPassword" placeholder="Confirmar nueva contraseña" required class="form-input"><br>

        <p v-if="newPassword && confirmPassword && newPassword !== confirmPassword" class="error">Las contraseñas no coinciden.</p>
      </div>

      <!-- Botón para cambiar la contraseña -->
      <button type="button" class="submit-btn" @click="togglePasswordFields">Cambiar</button>

      <!-- Botón para actualizar la contraseña -->
      <button v-if="isChangingPassword" type="submit" class="submit-btn">Actualizar contraseña</button>

      <button class="close-btn" @click="cerrarPopup">X</button>
    </div>
  </form>
  </body>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      newPassword: '',
      confirmPassword: '',
      isChangingPassword: false,
      token: null,
      is_authenticated: false,
      error: null
    }
  },
  methods: {
    togglePasswordFields () {
      this.isChangingPassword = !this.isChangingPassword
    },
    handleSubmit () {
      if (this.newPassword !== this.confirmPassword) {
        this.error = 'Las contraseñas no coinciden.'
      }
      this.updatePassword(this.email, this.newPassword)
    },
    updatePassword (email, password) {
      console.log('Actualizando contraseña de usuario:', email)

      // Simular éxito en la actualización:
      alert('Contraseña actualizada con éxito')

      // Cerrar el popup o redirigir al usuario
      this.cerrarPopup()
    },
    cerrarPopup () {
      this.$router.push('/login')
      this.$router.go()
    }
  }
}
</script>

<style scoped>
body, html {
  background: url('../assets/fondo.jpg') no-repeat center center fixed;
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  overflow: hidden;
}

.container {
  color: white;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  justify-content: center;
  background-color: #717d7e;
  padding: 20px;
  border-radius: 15px;
  width: 700px;
  height: auto;
  max-height: 80vh;
  overflow-y: auto;
  z-index: 2;
  box-sizing: border-box;
}

/* Ocultar barra de desplazamiento */
.container::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.container {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
}

.close-btn:hover {
  color: #ff4d4d;
}

.container input[type="email"],
.container .form-input {
  width: 60%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc; /* Borde gris claro */
  border-radius: 5px;
  background-color: white; /* Fondo blanco */
  color: black; /* Texto negro */
  font-size: 16px;
  box-sizing: border-box; /* Asegura que el padding no desborde */
}

.container input:focus {
  border-color: #007BFF; /* Borde azul al hacer foco */
  outline: none; /* Elimina el borde predeterminado del navegador */
}

.submit-btn {
  width: 60%;
  padding: 15px;
  margin-top: 10px;
  border: none;
  border-radius: 5px;
  background-color: red;
  color: white;
  font-size: 18px;
  cursor: pointer;
}

.submit-btn:hover {
  background-color: darkred;
}

.container a {
  color: white;
  text-decoration: none;
}

.container a:hover {
  text-decoration: underline;
}

.error {
  color: yellow;
  font-size: 14px;
  font-weight: bold;
}
</style>
