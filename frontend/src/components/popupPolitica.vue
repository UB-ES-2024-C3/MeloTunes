<template>
  <div v-if="visible" class="popup-overlay">
    <div class="popup-content">
      <h2>Política de Privacidad de Melotunes</h2>
      <div class="info" @wheel="stopScrollPropagation">
        <p class="title">¡BIENVENIDO A MELOTUNES!</p>

        <p>En Melotunes, nos comprometemos a proteger tu privacidad y garantizar
        la seguridad de tus datos personales. Esta Política de Privacidad explica cómo recopilamos,
        usamos, compartimos y protegemos tu información cuando utilizas nuestra aplicación.</p>
        <p class="title">1. Información que Recopilamos</p>
        <p>1.1 Información proporcionada por el usuario</p>
        <p> · Nombre y apellidos.</p>
        <p> · Dirección de correo electrónico.</p>
        <p> · Fecha de nacimiento.</p>
        <p>Datos opcionales como género, preferencias musicales, y tu foto de perfil.</p>

          <p class="title">1.2 Información recopilada automáticamente</p>

        <p> · Datos de uso: canciones escuchadas, playlists creadas, tiempo de reproducción.</p>
        <p> · Información del dispositivo: dirección IP, tipo de dispositivo, sistema operativo, e identificadores únicos.</p>
        <p> · Datos de ubicación aproximada basados en tu IP.</p>
        <p> · Cookies y tecnologías similares.</p>

            <p class="title">1.3 Información de terceros</p>

        <p>Si vinculas tu cuenta de Melotunes con redes sociales o plataformas de terceros, como Google, Facebook
          o Apple, podemos recibir información adicional como:</p>

        <p>Nombre, foto de perfil y correo electrónico asociado a dichas plataformas.</p>

        <p>Amigos o contactos en dichas redes (si das tu consentimiento).</p>

              <p class="title">2. Cómo Usamos tu Información</p>

        <p>Utilizamos tus datos personales para:</p>
        <p> · Prestar y personalizar el servicio: Recomendaciones musicales, creación automática de playlists y
          sugerencias basadas en tus gustos.</p>
        <p> · Gestión de la cuenta: Proporcionarte acceso seguro y mantener tus preferencias almacenadas. </p>
        <p> · Mejorar la experiencia del usuario: Analizar patrones de uso para optimizar el rendimiento de la
          aplicación y solucionar problemas técnicos. </p>
        <p> · Marketing y promociones: Enviar notificaciones o correos electrónicos sobre nuevos lanzamientos, ofertas
        o promociones (si has aceptado recibirlos).</p>

        <p> · Cumplir con obligaciones legales: Usar y compartir datos según sea necesario para cumplir con leyes y
          regulaciones aplicables.</p>

                <p class="title">3. Cómo Compartimos tu Información </p>

        <p>No vendemos tus datos personales. Sin embargo, podemos compartir información en los siguientes casos:</p>

        <p>3.1 Con proveedores de servicios</p>

        <p>Colaboramos con terceros que nos ayudan a operar nuestra aplicación, como servicios de alojamiento, análisis
        de datos, procesadores de pagos y notificaciones push. Estos proveedores solo tienen acceso a los datos necesarios
        para realizar sus funciones y están sujetos a acuerdos de confidencialidad.</p>

        <p>3.2 Con socios publicitarios</p>
        <p>Para usuarios de cuentas gratuitas, podemos compartir datos anonimizados o agregados con socios publicitarios
          para ofrecer anuncios relevantes.</p>

        <p>3.3 Por motivos legales</p>
        <p>Podemos divulgar tu información si es requerido por ley o para proteger nuestros derechos legales, prevenir
          fraudes o cumplir con procesos judiciales.</p>

                  <p class="title"> 4. Tus Derechos</p>

        <p>Dependiendo de tu ubicación, puedes ejercer los siguientes derechos sobre tus datos personales:</p>
        <p> · Acceso: Solicitar información sobre los datos personales que tenemos sobre ti.</p>
        <p> · Corrección: Solicitar que corrijamos información incorrecta o incompleta.</p>
        <p> · Eliminación: Pedir la eliminación de tus datos personales, salvo que debamos conservarlos por motivos
          legales o legítimos.</p>
        <p> · Portabilidad: Recibir una copia de tus datos en un formato estructurado y comúnmente utilizado.</p>
        <p> · Retiro de consentimiento: Revocar tu consentimiento para el uso de tus datos (por ejemplo, en marketing).</p>
        <p>Puedes ejercer estos derechos contactándonos en contacto@melotunes.com.</p>

                    <p class="title"> 5. Seguridad de los Datos</p>

        <p>Adoptamos medidas de seguridad técnicas y organizativas para proteger tus datos personales frente a accesos
          no autorizados, pérdida o alteración. Sin embargo, ningún sistema es completamente seguro. Por lo tanto, no
          podemos garantizar una seguridad absoluta.</p>

                      <p class="title"> 6. Retención de Datos</p>

        <p>Conservamos tus datos personales mientras tengas una cuenta activa con Melotunes. Si decides eliminar tu
          cuenta, eliminaremos tus datos salvo que debamos conservarlos para cumplir con obligaciones legales o
          proteger nuestros intereses legítimos.</p>

                        <p class="title">7. Uso de Cookies</p>
        <p>Utilizamos cookies y tecnologías similares para:</p>

        <p> · Recordar tus preferencias.</p>
        <p> · Analizar el rendimiento de nuestra aplicación.</p>
        <p> · Mostrar anuncios relevantes (para cuentas gratuitas).</p>
        <p>Puedes gestionar tus preferencias de cookies desde la configuración de tu dispositivo o navegador.
          Para más detalles, consulta nuestra Política de Cookies.</p>

                          <p class="title"> 8. Privacidad de Menores</p>

        <p>Melotunes no está destinada a personas menores de 13 años. No recopilamos intencionadamente datos personales
          de menores. Si descubrimos que hemos recopilado datos de un menor, los eliminaremos de inmediato.</p>

                            <p class="title">9. Cambios en esta Política</p>

          <p>Podemos actualizar esta Política de Privacidad ocasionalmente. Notificaremos cualquier cambio significativo
          a través de la aplicación o por correo electrónico. La fecha de la última actualización se encuentra al inicio
          de este documento.</p>

                              <p class="title"> 10. Contacto</p>

          <p>Si tienes preguntas, inquietudes o deseas ejercer tus derechos, puedes contactarnos en:</p>
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
