const API_URL = "http://127.0.0.1:8000/apiempleados"

fetch(API_URL)
    .then(response => response.json())
    .then( empleados => {
        tableContainer = document.getElementById("js-empleado-table");
        const thead = document.createElement('thead')
        thead.classList.add('thead-dark')
        const headrow = document.createElement('tr')
        const headkey = Object.keys(empleados[0])
        headkey.forEach(key => {
            const el = document.createElement('th')
            el.innerText=key
            headrow.appendChild(el)
        })
        thead.appendChild(headrow)
        const tbody = document.createElement('tbody')
        empleados.forEach(empleado => {
            const row = document.createElement('tr')
            const rowcontent = `
            <td>${empleado.id}</td>
            <td>${empleado.dni}</td>
            <td>${empleado.nombre}</td>
            <td>${empleado.apellidos}</td>
            <td>${empleado.email}</td>
            <td>${empleado.telefono}</td>
            `
            row.innerHTML=rowcontent
            tbody.appendChild(row)
        })
        tableContainer.appendChild(thead)
        tableContainer.appendChild(tbody)
    });

function addRows(empleados) {
    tbody = document.getElementById("tbody");
    empleados.forEach(element => {
        tbody.appendChild(createEmpleadoRow(element))
    });
}

function createEmpleadoRow(empleados){
    let row = document.createElement("tr")

    let nombre = document.createElement("td")
        nombre.textContent = empleados.nombre;
        row.appendChild(nombre);
        
    return row;
}