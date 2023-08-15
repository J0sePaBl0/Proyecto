const botList = document.getElementById('botList');

// Función para cargar los datos de los bots desde el backend
async function cargarBots() {
    const response = await fetch('/obtener_bots');  // Cambia la ruta según tu backend
    const datos = await response.json();

    // Mostrar los datos de los bots en la página
    datos.forEach(bot => {
        const botDiv = document.createElement('div');
        botDiv.classList.add('bot');
        botDiv.innerHTML = `
            <img class="Botimg" src="${bot.imagen_url}" alt="Imagen del bot">
            <h2>${bot.nombre}</h2>
            <p>${bot.descripcion}</p>
            <p>Precio: $${bot.precio}</p>
            <button class="comprar-btn">Comprar</button>
        `;
        botList.appendChild(botDiv);
    });
}

// Cargar los datos de los bots al cargar la página
cargarBots();
