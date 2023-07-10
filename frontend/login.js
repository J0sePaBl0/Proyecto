const wrapper = document.querySelector(".wrapper"),
          signupHeader = document.querySelector(".signup header"),
          loginHeader = document.querySelector(".login header");

        loginHeader.addEventListener("click", () => {
          wrapper.classList.add("active");
        });
        signupHeader.addEventListener("click", () => {
          wrapper.classList.remove("active");
        });

const lCorreo = document.getElementById('lCorreo')
const lContra = document.getElementById('lContra')
const lButton = document.getElementById('lButton')

lButton.addEventListener('click', (e) => {
    e.preventDefault()
    const data = {
        lCorreo: lCorreo.value,
        lContra: lContra.value
    }

    console.log(data)
})