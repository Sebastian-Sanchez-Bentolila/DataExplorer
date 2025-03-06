document.addEventListener("DOMContentLoaded", () => {
    const tecnologias = document.querySelectorAll(".card .btn");
    const guiasContainer = document.querySelector("#guias-container");

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

const guiasJSON = [
    {
        "tecnologia": "Python",
        "guias": [
        {
            "titulo": "Introducción a Python",
            "descripcion": "Aprende los fundamentos de lenguaje de programación Python",
            "enlace": "guias/Python/python_basico/python_basico.html"
        },
        {
            "titulo": "Estructura de Datos",
            "descripcion": "Listas, tuplas, conjuntos, diccionarios y colas y pilas.",
            "enlace": "guias/Python/estructura/estructura.html"
        },
        {
            "titulo": "Funciones",
            "descripcion": "Funciones y argumentos. Funciones lambda",
            "enlace": "guias/Python/funciones/funciones.html"
        },
        {
            "titulo": "Módulos",
            "descripcion": "Librerias propias y externas (PIP) y su importación",
            "enlace": "guias/Python/modulos/modulos.html"
        },
        {
            "titulo": "Excepciones",
            "descripcion": "try, finally y raise",
            "enlace": "guias/Python/excepciones/excepciones.html"
        },
        {
            "titulo": "Clases y Objetos",
            "descripcion": "Clases y Objetos",
            "enlace": "guias/Python/clases/clases.html"
        },
        {
            "titulo": "Manejo de archivos",
            "descripcion": "Módulo os",
            "enlace": "guias/Python/archivos/archivos.html"
        },
        {
            "titulo": "Visualizaciones",
            "descripcion": "Matplotlib, Seaborn, plotly, altair",
            "enlace": "guias/Python/visualizacion/visualizacion.html"
        },
        {
            "titulo": "Tkinter",
            "descripcion": "Interfaces Gráficas con el módulo tkinter",
            "enlace": "guias/Python/tkinter/tkinter.html"
        },
        {
            "titulo": "Manejo de base de datos relacionales",
            "descripcion": "SQLite, MySQL y ORM",
            "enlace": "guias/Python/sql/sql.html"
        },
        {
            "titulo": "Expresiones regulares",
            "descripcion": "Módulo regex",
            "enlace": "guias/Python/expresiones_regulares/expresiones_regulares.html"
        },
        {
            "titulo": "Máquinas Virtuales",
            "descripcion": "Maquinas virtuales, frizar version y un poco de Docker",
            "enlace": "guias/Python/maquinas_virtuales/maquinas_virtuales.html"
        },
        {
            "titulo": "Documentación",
            "descripcion": "Documentación en Python y gestores",
            "enlace": "guias/Python/documentacion/documentacion.html"
        },
        {
            "titulo": "Jupyter Notebook",
            "descripcion": "Introducción al entorno de Jupyter Notebook",
            "enlace": "guias/Python/jupyter_notebook/jupyter_notebook.html"
        },
        {
            "titulo": "Google colab",
            "descripcion": "Introducción al entorno de Google Colab",
            "enlace": "guias/Python/google_colab/google_colab.html"
        },
        {
            "titulo": "Metaclases",
            "descripcion": "Metaclases en Python",
            "enlace": "guias/Python/metaclases/metaclases.html"
        }]
    },
    {
        "tecnologia": "R",
        "guias": [
        {
            "titulo": "Introducción a R",
            "descripcion": "Aprende los fundamentos de lenguaje de programación R",
            "enlace": "guias/R/r_basico/r_basico.html"
        }]
    },
    {
        "tecnologia": "SQL",
        "guias": [
        {
            "titulo": "Introducción a SQL",
            "descripcion": "Aprende los fundamentos de las bases de datos relacionales",
            "enlace": "guias/SQL/sql_basico/sql_basico.html"
        },
        {
            "titulo": "Tipo de Datos",
            "descripcion": "Tipos de datos en SQL",
            "enlace": "guias/SQL/tipo_datos/tipo_datos.html"
        },
        {
            "titulo": "Manipulación de Datos",
            "descripcion": "Aprende las diferentes formas para manipular los datos de una base de datos relacionales",
            "enlace": "guias/SQL/manipulacion_datos/manipulacion_datos.html"
        },
        {
            "titulo": "Restricciones",
            "descripcion": "Restricciones de una base de datos relacional",
            "enlace": "guias/SQL/restricciones/restricciones.html"
        },
        {
            "titulo": "Funciones Agregadas",
            "descripcion": "Aprende las diferentes funciones agregadas para operar sobre base de datos relacionales",
            "enlace": "guias/SQL/funciones_agregadas/funciones_agregadas.html"
        },
        {
            "titulo": "JOIN y uniones",
            "descripcion": "Uniones e intersecciones en SQL",
            "enlace": "guias/SQL/join/join.html"
        },
        {
            "titulo": "SubConsultas",
            "descripcion": "Subconsultas en SQL",
            "enlace": "guias/SQL/subconsultas/subconsultas.html"
        },
        {
            "titulo": "Rutinas",
            "descripcion": "Rutinas en SQL",
            "enlace": "guias/SQL/rutinas/rutinas.html"
        },
        {
            "titulo": "Variables",
            "descripcion": "Variables en SQL",
            "enlace": "guias/SQL/variables/variables.html"
        },
        {
            "titulo": "Mejores Prácticas",
            "descripcion": "Optimización y mejores prácticas en SQL",
            "enlace": "guias/SQL/optimizacion/optimizacion.html"
        }]
    },
    {
        "tecnologia": "Matemáticas",
        "guias": [
        {
            "titulo": "Ecuaciones",
            "descripcion": "Ecuaciones Matematicas",
            "enlace": "guias/matematica/ecuaciones/ecuaciones.html"
        },
        {
            "titulo": "Logaritmo",
            "descripcion": "Logaritmo",
            "enlace": "guias/matematica/logaritmo/logaritmo.html"
        },
        {
            "titulo": "Números Complejos",
            "descripcion": "Números Complejos",
            "enlace": "guias/matematica/numero_complejos/numero_complejos.html"
        },
        {
            "titulo": "Límites",
            "descripcion": "Límites matemáticos",
            "enlace": "guias/matematica/limite/limite.html"
        },
        {
            "titulo": "Derivadas",
            "descripcion": "Derivadas",
            "enlace": "guias/matematica/derivadas/derivadas.html"
        }]
    },
    {
        "tecnologia": "Git",
        "guias": [
        {
            "titulo": "Introducción a Git",
            "descripcion": "Aprende los fundamentos de Git",
            "enlace": "guias/Git/git_basico/git_basico.html"
        }]
    },
    {
        "tecnologia": "Investigación",
        "guias": [
        {
            "titulo": "CTyS",
            "descripcion": "Taller de Ciencia, Tecnología y Sociedad",
            "enlace": "guias/Investigacion/cts/cts.html"
        },
        {
            "titulo": "Metodología de la investigación",
            "descripcion": "Aprende los fundamentos de una investigación",
            "enlace": "guias/Investigacion/metodologia_investigacion/metodologia_investigacion.html"
        },
        {
            "titulo": "Administración",
            "descripcion": "Administración a nivel universitario",
            "enlace": "guias/Investigacion/administracion/administracion.html"
        },]
    }
];

async function cargarGuias(tecnologia) {
    const tecnologiaData = guiasJSON.find(item => item.tecnologia === tecnologia);
    return tecnologiaData ? tecnologiaData.guias : [];
}

// Función para mostrar guías dinámicamente
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

    // Desplazar la vista al contenedor
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




