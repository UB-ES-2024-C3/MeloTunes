<template>
  <div v-if="visible" class="popup-overlay">
    <div class="popup-content">
      <h2>Cookies de Melotunes</h2>
      <div class="info" @wheel="stopScrollPropagation">
        <p class="title">¡BIENVENIDO A MELOTUNES!</p>
        <p>En Melotunes, utilizamos cookies y tecnologías similares para mejorar tu experiencia y personalizar el contenido que ofrecemos. Esta política describe qué son las cookies, cómo las usamos y cómo puedes gestionarlas.</p>
        <p class="title">1. Tipos de cookies que usamos</p>
        <p>1.1 Cookies esenciales</p>
        <p>Estas cookies son necesarias para el funcionamiento básico de la aplicación.</p>
        <p>1.2 Cookies de rendimiento</p>
        <p> · Recopilan datos sobre cómo utilizas Melotunes, como las páginas o secciones visitadas y errores encontrados.</p>
        <p> · Nos ayudan a mejorar la funcionalidad y rendimiento de la aplicación.</p>
        <p>1.3 Cookies de personalización</p>
        <p>Guardan tus preferencias (como idioma o género musical favorito) para ofrecerte una experiencia personalizada.</p>
        <p>1.4 Cookies publicitarias</p>
        <p>Usadas para mostrar anuncios relevantes (aplican solo a usuarios de cuentas gratuitas).</p>
        <p>Trabajamos con socios publicitarios para adaptar los anuncios a tus intereses.</p>
        <p>1.5 Cookies de terceros</p>
        <p>Algunos de nuestros socios, como servicios analíticos o publicitarios, también pueden establecer cookies en tu dispositivo. Estas cookies están sujetas a sus propias políticas de privacidad.</p>

        <p class="title">2. Por qué usamos cookies</p>
        <p>Utilizamos cookies para:</p>
        <p> · Facilitar la navegación y garantizar el funcionamiento básico de Melotunes.</p>
        <p> · Mejorar la experiencia de usuario mediante la personalización del contenido.</p>
        <p> · Analizar el uso de la aplicación para optimizar su rendimiento.</p>
        <p> · Mostrarte anuncios relevantes según tus intereses (en cuentas gratuitas).</p>

        <p class="title">3. Cómo gestionar tus cookies</p>
        <p>3.1 Configuración dentro de la aplicación</p>
        <p>Puedes ajustar tus preferencias de cookies desde la sección Configuración de Cookies en el menú principal de Melotunes. Allí puedes:</p>
        <p>Activar o desactivar ciertos tipos de cookies (excepto las esenciales).</p>
        <p>Revocar tu consentimiento para el uso de cookies opcionales.</p>
        <p>3.2 Configuración en tu navegador o dispositivo</p>
        <p>La mayoría de los navegadores y dispositivos móviles te permiten bloquear o eliminar cookies. Consulta la documentación de tu navegador o dispositivo para obtener instrucciones.</p>
        <p>Ten en cuenta: Deshabilitar ciertas cookies puede afectar la funcionalidad de la aplicación.</p>

        <p class="title">4. Cookies de terceros</p>
        <p>Usamos servicios de terceros, como Google Analytics, para analizar el rendimiento de nuestra aplicación y mostrar anuncios personalizados. Estos servicios pueden establecer cookies en tu dispositivo.</p>
        <p>Para saber más sobre cómo estos terceros gestionan las cookies, consulta sus políticas de privacidad.</p>
        <p>Puedes deshabilitar estas cookies desde la configuración de tu dispositivo o en la sección de cookies de nuestra app.</p>

        <p class="title">5. Cambios en esta política</p>
        <p>Podemos actualizar esta política ocasionalmente para reflejar cambios en el uso de cookies o nuevas normativas legales. La fecha de la última actualización se indica al inicio del documento.</p>

        <p class="title">6. Contacto</p>
        <p>Si tienes preguntas o inquietudes sobre el uso de cookies en Melotunes, contáctanos en:</p>
        <p> · Correo electrónico: contacto@melotunes.com</p>
        <p> · Dirección postal: Dirección de la empresa</p>
        <p> · Teléfono: +34 123456789</p>

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
  background: url('../assets/fondo.png') no-repeat center center fixed; /* Fondo de la imagen */
  background-size: cover; /* Hace que la imagen cubra todo el área del popup */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  position: relative;
  background: rgba(0, 0, 0, 0.7); /* Fondo oscuro semitransparente para hacer que el contenido sea legible sobre la imagen */
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  width: 40vw;
}

.close-button {
  cursor: pointer;
  color: #ff1e1e;
  transition: color 0.3s ease;
  font-size: 1.5rem;
}

.close-button:hover {
  color: #ff0000;
}

.info {
  border: 2px solid #000000; /* Borde oscuro */
  padding: 1vw; /* Espaciado interno */
  border-radius: 5px; /* Bordes redondeados */
  background-color: rgba(0, 0, 0, 0.8); /* Fondo oscuro para que el texto sea legible */
  margin: 1vw; /* Separación con otros elementos */
  max-height: 50vh; /* Altura máxima del recuadro */
  overflow-y: auto; /* Activa la scrollbar vertical */
  text-align: justify;
}

.info p {
  color: #ffffff; /* Texto blanco para contraste */
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
  color: #ffffff; /* Texto blanco para mejor contraste */
}
</style>
