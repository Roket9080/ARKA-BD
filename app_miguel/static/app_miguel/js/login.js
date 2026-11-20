document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const btnSubmit = document.querySelector('.btn-submit');

  if (loginForm) {
    loginForm.addEventListener('submit', () => {
      // Feedback visual al enviar el formulario
      btnSubmit.style.opacity = '0.7';
      btnSubmit.textContent = 'Ingresando...';
    });
  }
});