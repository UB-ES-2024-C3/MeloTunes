describe('Página de registro', () => {
  beforeEach(() => {
    cy.visit('/register');
  });

  it('Carga correctamente la página de registro', () => {
    cy.contains('Completa tu Registro'); // Verifica que el texto existe
    cy.get('form').should('exist'); // Verifica que el formulario está presente
    cy.get('input[type="email"]').should('have.length', 1); // Email, Nombre, Apellido
    cy.get('input[type="text"]').should('have.length', 2); // Email, Nombre, Apellido
    cy.get('input[type="password"]').should('have.length', 2); // Contraseña y Confirmar Contraseña
    cy.get('input[type="date"]').should('exist'); // Fecha de nacimiento
  });

  it('Muestra error si los campos están vacíos al enviar', () => {
    cy.get('input[type="submit"]').click();

    // Verificar mensajes de error específicos
    cy.contains('El campo de correo electrónico no puede estar vacío.').should('exist');
    cy.contains('La contraseña no puede estar vacía.').should('exist');
    cy.contains('El nombre solo puede contener letras.').should('exist');
    cy.contains('El apellido solo puede contener letras.').should('exist');
    cy.contains('Debes ingresar tu fecha de nacimiento.').should('exist');
  });

  it('Valida el formato del correo electrónico', () => {
    cy.get('#email').type('correo_incorrecto');
    cy.get('input[type="submit"]').click();
    cy.contains('El formato del correo electrónico no es válido.').should('exist');
  });

  /*
  it('Valida las contraseñas correctamente', () => {
    cy.get('#password').type('corta');
    cy.get('input[type="submit"]').click();
    cy.contains('La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula y un número.')
      .should('be.visible');

    cy.get('#password').clear().type('Correcta123');
    cy.get('#confirm_password').type('Incorrecta123');
    cy.get('input[type="submit"]').click();
    cy.contains('Las contraseñas no coinciden.').should('be.visible');
  });*/

  it('Muestra/oculta la contraseña correctamente', () => {
    cy.get('#password').type('MiContraseña123');
    cy.get('.password-container img').first().click(); // Haz clic en el ícono
    cy.get('#password').should('have.attr', 'type', 'text'); // Verifica que se muestra el texto

    cy.get('.password-container img').first().click(); // Haz clic en el ícono de nuevo
    cy.get('#password').should('have.attr', 'type', 'password'); // Verifica que se oculta la contraseña
  });

  it('Valida la fecha de nacimiento', () => {
    cy.get('#fecha_nacimiento').type('2020-01-01'); // Fecha menor a 16 años
    cy.get('input[type="submit"]').click();
    cy.contains('Debes tener al menos 16 años para registrarte.').should('be.visible');
  });

  it('Muestra error si el nombre contiene caracteres no válidos', () => {
    cy.get('#nombre').type('<script>alert("hack")</script>');
    cy.get('input[type="submit"]').click();
    cy.contains('El nombre solo puede contener letras.').should('exist');
  });

  it('Muestra error si el apellido contiene caracteres no válidos', () => {
    cy.get('#apellido').type('<script>alert("hack")</script>');
    cy.get('input[type="submit"]').click();
    cy.contains('El apellido solo puede contener letras.').should('exist');
  });

  it('Muestra un error si el usuario ya está registrado', () => {
    // Datos de un usuario ya registrado
    cy.get('#email').type('registrado@ejemplo.com');
    cy.get('#password').type('Password123');
    cy.get('#confirm_password').type('Password123');
    cy.get('#nombre').type('Usuario');
    cy.get('#apellido').type('Registrado');
    cy.get('#fecha_nacimiento').type('2000-01-01');
    cy.get('input[type="submit"]').click();

    // Verificar que aparece el mensaje de error
    cy.on('window:alert', (text) => {
      expect(text).to.equal(
        'El usuario con email registrado@ejemplo.com ya está registrado en el sistema.'
      );
    });
  });

  /*
  it('Completa el registro exitosamente con datos válidos', () => {
    // Rellenar los campos del formulario con datos válidos
    const uniqueEmail = `testusers${Date.now()}@gmail.com`;
    cy.get('#email').type(uniqueEmail);
    cy.get('#password').type('Valida123');
    cy.get('#confirm_password').type('Valida123');
    cy.get('#nombre').type('Usuario');
    cy.get('#apellido').type('Nuevo');
    cy.get('#fecha_nacimiento').type('2000-01-01');

    // Simular el clic en el botón de registro
    cy.get('input[type="submit"]').click();

    // Capturar el mensaje de alerta y verificarlo
    cy.on('window:alert', (alertText) => {
      expect(alertText).to.contains('Registro exitoso!');
    });
  });*/
  
});
