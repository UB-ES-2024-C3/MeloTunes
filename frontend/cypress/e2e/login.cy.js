describe('Página de inicio de sesión', () => {
  beforeEach(() => {
    cy.visit('/login'); // Asegúrate de que la URL sea correcta
  });

  it('Carga correctamente la página de inicio de sesión', () => {
    cy.contains('Inicia sesión en MeloTunes'); // Verifica que el texto existe
    cy.get('input[type="email"]').should('be.visible'); // Verifica que el campo de email está visible
    cy.get('input[type="password"]').should('be.visible'); // Verifica que el campo de contraseña está visible
  });

  it('Muestra error si los campos están vacíos al enviar', () => {
    cy.get('button[type="submit"]').click();
    cy.contains('Por favor, complete todos los campos').should('be.visible'); // Mensaje de error esperado
  });

  it('Inicia sesión correctamente con credenciales válidas', () => {
    cy.get('input[type="email"]').type('usuario@ejemplo.com');
    cy.get('input[type="password"]').type('contraseñaValida123');
    cy.get('button[type="submit"]').click();

    // Asegúrate de que redirige o muestra contenido tras el inicio de sesión
    cy.url().should('include', '/home'); // Ejemplo de redirección
  });

  it('Muestra error si las credenciales son incorrectas', () => {
    cy.get('input[type="email"]').type('usuario@ejemplo.com');
    cy.get('input[type="password"]').type('contraseñaIncorrecta');
    cy.get('button[type="submit"]').click();

    // Verifica que aparece un mensaje de error
    cy.contains('Correo o contraseña incorrectos').should('be.visible');
  });
});
