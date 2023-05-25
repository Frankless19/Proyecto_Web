const API_URL = "http://127.0.0.1:8000/apiequipos"

fetch(API_URL)
    .then(response => response.json())
    .then( equipos => {
        tableContainer = document.getElementById("js-equipo-table");
        const thead = document.createElement('thead')
        thead.classList.add('thead-dark')
        const headrow = document.createElement('tr')
        const headkey = Object.keys(equipos[0])
        headkey.forEach(key => {
            const el = document.createElement('th')
            el.innerText=key
            headrow.appendChild(el)
        })
        thead.appendChild(headrow)
        const tbody = document.createElement('tbody')
        equipos.forEach(equipo => {
            const row = document.createElement('tr')
            const rowcontent = `
            <td>${equipo.id}</td>
            <td>${equipo.nserie}</td>
            <td>${equipo.modelo}</td>
            <td>${equipo.marca}</td>
            <td>${equipo.tipo}</td>
            <td>${equipo.fechaAdquisicion}</td>
            <td>${equipo.fechaPuestaMarcha}</td>
            <td>${equipo.provNombre}</td>
            <td>${equipo.provTelefono}</td>
            <td>${equipo.planta}</td>
            `
            row.innerHTML=rowcontent
            tbody.appendChild(row)
        })
        tableContainer.appendChild(thead)
        tableContainer.appendChild(tbody)
    });

function addRows(equipos) {
    tbody = document.getElementById("tbody");
    equipos.forEach(element => {
        console.log(tbody)
        tbody.appendChild(createEquipoRow(element))
    });
}

function createEmpleadoRow(empleados){
    let row = document.createElement("tr")

    let nombre = document.createElement("td")
        nombre.textContent = equipos.nombre;
        row.appendChild(nombre);
        
    return row;
}