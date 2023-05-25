const API_URL = "http://127.0.0.1:8000/apitickets"

fetch(API_URL)
    .then(response => response.json())
    .then( tickets => {
        tableContainer = document.getElementById("js-ticket-table");
        const thead = document.createElement('thead')
        thead.classList.add('thead-dark')
        const headrow = document.createElement('tr')
        const headkey = Object.keys(tickets[0])
        headkey.forEach(key => {
            const el = document.createElement('th')
            el.innerText=key
            headrow.appendChild(el)
        })
        thead.appendChild(headrow)
        const tbody = document.createElement('tbody')
        tickets.forEach(ticket => {
            const row = document.createElement('tr')
            const rowcontent = `
            <td>${ticket.id}</td>
            <td>${ticket.nref}</td>
            <td>${ticket.titulo}</td>
            <td>${ticket.descripcion}</td>
            <td>${ticket.fechaApertura}</td>
            <td>${ticket.fechaResolucion}</td>
            <td>${ticket.nivelUrgencia_id}</td>
            <td>${ticket.tipo_id}</td>
            <td>${ticket.estado_id}</td>
            <td>${ticket.empleado_id}</td>
            <td>${ticket.equipo_id}</td>
            <td>${ticket.comentarios}</td>

            `
            row.innerHTML=rowcontent
            tbody.appendChild(row)
        })
        tableContainer.appendChild(thead)
        tableContainer.appendChild(tbody)
    });

function addRows(tickets) {
    tbody = document.getElementById("tbody");
    tickets.forEach(element => {
        console.log(tbody)
        tbody.appendChild(createTicketRow(element))
    });
}

function createTicketRow(tickets){
    let row = document.createElement("tr")

    let nombre = document.createElement("td")
        nombre.textContent = tickets.nombre;
        row.appendChild(nombre);
        
    return row;
}