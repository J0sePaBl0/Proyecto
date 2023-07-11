
const signupForm = document.getElementById('signupForm');
const rButton = document.getElementById('rButton');

rButton.addEventListener('click', (e) => {
  e.preventDefault(); 


  const nombre = document.getElementById('rNombre').value;
  const correo = document.getElementById('rCorreo').value;
  const contraseña = document.getElementById('rContra').value;

  
  const formData = {
    nombre: nombre,
    correo: correo,
    contraseña: contraseña
  };

 
  fetch('/registro', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
  })
    .then(response => response.json())
    .then(data => {
      
      console.log(data);
      alert('Valores de los campos: ' + nombre + ', ' + correo + ', ' + contraseña);
      alert('¡Registro exitoso!'); 
    })
    .catch(error => {
      console.error('Error:', error);
     
    });
});
