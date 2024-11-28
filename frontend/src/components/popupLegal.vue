<template>
  <div v-if="visible" class="popup-overlay">
    <div class="popup-content">
      <h2>Términos y Condiciones de uso de Melotunes</h2>
      <div class="info" @wheel="stopScrollPropagation">
        <p class="title">¡BIENVENIDO A MELOTUNES!</p>
        <p>Estos Términos y Condiciones regulan el uso de nuestra aplicación de música.
          Al descargar, instalar o utilizar Melotunes, aceptas los términos establecidos aquí.
          Si no estás de acuerdo, no uses la aplicación.</p>
        <p class="title">1. Uso de la Aplicación</p>
        <p>
          1.1. Melotunes proporciona acceso a contenido musical para uso personal, no comercial.</p>
        <p>1.2. Prohíbese el uso no autorizado, incluyendo:</p>
        <p> · Reproducción, distribución o modificación del contenido protegido por derechos de autor.</p>
        <p> · Uso de la aplicación para actividades ilícitas.</p>
        <p class="title">2. Registro y Cuenta</p>
        <p>
          2.1. Debes registrarte proporcionando información verídica.</p>
        <p>2.2. Eres responsable de la seguridad de tus credenciales de acceso.</p>
        <p>2.3. Nos reservamos el derecho de suspender o eliminar cuentas que violen estos términos.</p>
        <p class="title">3. Tarifas y Pagos</p>
        <p>
          3.1. La versión premium requiere una suscripción paga.</p>
        <p>3.2. Todas las transacciones están sujetas a los términos de nuestro proveedor de pagos.</p>
        <p class="title">4. Propiedad Intelectual</p>
        <p>4.1. Todo el contenido (música, logos, diseño) pertenece a Melotunes o a sus licenciantes.</p>
        <p>4.2. El uso de este contenido está restringido a lo permitido por estos términos.</p>
        <p class="title">5. Limitación de Responsabilidad</p>
        <p>
          Melotunes no se hace responsable de:</p>
        <p>Interrupciones del servicio.</p>
        <p>Daños indirectos o pérdidas de datos.</p>
        <p class="title">6. Modificaciones</p>
        <p>
          Podemos actualizar estos términos en cualquier momento. Notificaremos cambios significativos a través de la aplicación.
          Para más detalles, consulta contacto@melotunes.com.</p>
      </div>
      <button class="close-button" @click="closePopup">Cerrar</button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      visible: false // Controla si el popup es visible
    }
  },
  methods: {
    openPopup () {
      this.visible = true
    },
    closePopup () {
      this.visible = false
    },
    stopScrollPropagation (event) {
      const element = event.currentTarget
      const atTop = element.scrollTop === 0
      const atBottom =
        element.scrollHeight - element.scrollTop === element.clientHeight

      if (atTop && event.deltaY < 0) {
        event.preventDefault() // Evita que suba más cuando está arriba
      }

      if (atBottom && event.deltaY > 0) {
        event.preventDefault() // Evita que baje más cuando está abajo
      }
    }
  }
}
</script>

<style scoped>
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  position: relative;
  background: linear-gradient(to bottom, #000, #e53935);
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  width: 40vw;
}
.close-button {
  cursor: pointer;
  color: #000000;
  transition: color 0.3s ease;
  font-size: 1.5rem;
}

.close-button:hover {
  color: #ff0000;
}
.info {
  border: 2px solid #000000; /* Borde azul */
  padding: 1vw; /* Espaciado interno */
  border-radius: 5px; /* Bordes redondeados */
  background-color: #000000; /* Fondo azul claro */
  margin: 1vw ; /* Separación con otros elementos */
  max-height: 50vh; /* Altura máxima del recuadro */
  overflow-y: auto; /* Activa la scrollbar vertical */
  text-align: justify;

}

.info p {
  color: #ffffff; /* Texto negro para contraste */
  margin: 0;
  font-size: 1.4rem;
  line-height: 2.7rem;
}
.info::-webkit-scrollbar {
  width: 8px; /* Ancho de la scrollbar */
}

.info::-webkit-scrollbar-track {
  background: #212121; /* Fondo del track */
  border-radius: 10px; /* Bordes redondeados */
}

.info::-webkit-scrollbar-thumb {
  background-color: black; /* Color de la scrollbar */
  border-radius: 10px; /* Bordes redondeados */
  border: 2px solid #000000; /* Espaciado interno */
}
.title {
  font-size: 1.3em; /* Aumenta ligeramente el tamaño del texto */
  font-weight: bold; /* Aplica negrita */
  margin-top: 1.1em; /* Espaciado superior para separarlo del texto anterior */
  margin-bottom: 0.5em; /* Espaciado inferior */
  color: #ffffff; /* Asegura que sea negro para buen contraste */
}

</style>
