const rNombre = document.getElementById('rNombre')
const rCorreo = document.getElementById('rCorreo')
const rContra = document.getElementById('rContra')
const rButton = document.getElementById('rButton')

rButton.addEventListener('click', (e) => {
    e.preventDefault()
    const data = {
        rNombre: rNombre.value,
        rCorreo: rCorreo.value,
        rContra: rContra.value
    }
    
    console.log(data)
})