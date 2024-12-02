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
});
