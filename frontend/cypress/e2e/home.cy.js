describe('Página principal', () => {
  beforeEach(() => {
    cy.visit('/home');  // Asegúrate de usar la URL correcta
  });
it('Debe mostrar el logo correctamente', () => {
    // Verificamos que el logo esté visible
    cy.get('.logo img').should('be.visible');
  });

  it('Debe contener el texto "¡MELOTUNES!" en la cabecera', () => {
    // Verificamos que el texto ¡MELOTUNES! esté presente
    cy.contains('¡MELOTUNES!').should('be.visible');
  });

  it('Debe tener los botones de autenticación cuando no está logueado', () => {
    // Verificamos que los botones de login y registro estén presentes
    cy.get('.auth-buttons a').should('have.length', 2);  // Dos botones: "Iniciar sesión" y "Registrarse"
  });
});
