document.addEventListener("DOMContentLoaded", () => {
    const tecnologias = document.querySelectorAll(".card .btn");
    const guiasContainer = document.createElement("section");
    guiasContainer.id = "guias-container";
    document.body.appendChild(guiasContainer);

    tecnologias.forEach(btn => {
        btn.addEventListener("click", async (event) => {
            event.preventDefault();
            const tecnologia = btn.parentElement.querySelector("h3").textContent;

            // Cargar guías desde el archivo JSON
            const guias = await cargarGuias(tecnologia);

            // Mostrar guías en el contenedor
            mostrarGuias(tecnologia, guias);
        });
    });
});

// Función para cargar guías desde el archivo JSON
async function cargarGuias(tecnologia) {
    try {
        const response = await fetch("guias.json");
        const data = await response.json();
        const tecnologiaData = data.find(item => item.tecnologia === tecnologia);
        return tecnologiaData ? tecnologiaData.guias : [];
    } catch (error) {
        console.error("Error al cargar las guías:", error);
        return [];
    }
}

function mostrarGuias(tecnologia, guias) {
    const guiasContainer = document.querySelector("#guias-container");
    guiasContainer.innerHTML = `
        <h2 data-aos="fade-up">Guías de ${tecnologia}</h2>
        <div class="guias-grid">
            ${guias.map(guia => `
                <div class="guia-card" data-aos="zoom-in">
                    <h3>${guia.titulo}</h3>
                    <p>${guia.descripcion}</p>
                    <a href="${guia.enlace}" class="btn" target="_blank">Leer más</a>
                </div>
            `).join('')}
        </div>
    `;
    
    // Reinicializar AOS para las nuevas guías
    AOS.refresh();

    // Desplazarse al contenedor
    guiasContainer.scrollIntoView({ behavior: "smooth" });
}


AOS.init({
    duration: 1200,   // Duración de las animaciones (en ms)
    once: true,       // La animación ocurre solo una vez
    easing: 'ease-in-out', // Tipo de movimiento
    offset: 200,      // Distancia desde el viewport para activar la animación
});

let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll(".carousel .slide");
    slides.forEach((slide, i) => {
        slide.style.transform = `translateX(${(i - index) * 100}%)`;
    });
}

document.querySelector(".proyectos").addEventListener("click", () => {
    currentSlide = (currentSlide + 1) % document.querySelectorAll(".slide").length;
    showSlide(currentSlide);
});

showSlide(currentSlide);



