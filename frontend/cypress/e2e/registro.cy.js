describe('Página de registro', () => {
  beforeEach(() => {
    cy.visit('/register');
  });

  it('Carga correctamente la página de registro', () => {
    cy.contains('Completa tu Registro'); // Verifica que el texto existe
    cy.get('form').should('exist'); // Verifica que el formulario está presente
    cy.get('input[type="text"]').should('have.length', 3); // Email, Nombre, Apellido
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

  it('Valida las contraseñas correctamente', () => {
    cy.get('#password').type('corta');
    cy.get('input[type="submit"]').click();
    cy.contains('La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula y un número.')
      .should('be.visible');

    cy.get('#password').clear().type('Correcta123');
    cy.get('#confirm_password').type('Incorrecta123');
    cy.get('input[type="submit"]').click();
    cy.contains('Las contraseñas no coinciden.').should('be.visible');
  });

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

});
