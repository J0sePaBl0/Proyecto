const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");


nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if(input.value != ""){
            form.classList.add('secActive');
        }else{
            form.classList.remove('secActive');
        }
    })
})

backBtn.addEventListener("click", () => form.classList.remove('secActive'));



nextBtn.addEventListener('click', (e) => {
  e.preventDefault(); 


  const nombre = document.getElementById('rNombre').value;
  const descripcion = document.getElementById('rDescripcion').value;
  const precio = document.getElementById('rPrecio').value;

  
  const formData = {
    nombre: nombre,
    descripcion: descripcion,
    precio: precio
  };

 
  fetch('/registroBots', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
  })
    .then(response => response.json())
    .then(data => {
      
      console.log(data);
      alert('Valores de los campos: ' + nombre + ', ' + descripcion + ', ' + precio);
      alert('¡Registro exitoso!'); 
    })
    .catch(error => {
      console.error('Error:', error);
     
    });
});
