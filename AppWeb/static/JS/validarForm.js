const formEquipo = document.getElementById("formEquipo");
const formTicket = document.getElementById("formTicket");
const formEmpleado = document.getElementById("formEmpleado");

formEquipo.addEventListener("submit", function (event) {
  event.preventDefault();

  const nserie = document.getElementById("id_nserie").value;
  const modelo = document.getElementById("id_modelo").value;
  const marca = document.getElementById("id_marca").value;
  const provTelefono = document.getElementById("id_provTelefono").value;

  if (!validarCampo(nserie)) {
    alert("Por favor, ingresa un número de serie válido.");
    return;
  }

  if (!validarCampo(modelo)) {
    alert("Por favor, ingresa un modelo válido.");
    return;
  }

  if (!validarCampo(marca)) {
    alert("Por favor, ingresa una marca válida.");
    return;
  }

  if (!validarTelefono(provTelefono)) {
    alert("Por favor, ingresa un teléfono válido para el proveedor.");
    return;
  }

  formEquipo.submit();
});

formTicket.addEventListener("submit", function (event) {
  event.preventDefault();

  const nref = document.getElementById("id_nref").value;
  const titulo = document.getElementById("id_titulo").value;
  const descripcion = document.getElementById("id_descripcion").value;

  if (!validarCampoNumerico(nref)) {
    alert("Por favor, ingresa una referencia válida.");
    return;
  }

  if (!validarCampo(titulo)) {
    alert("Por favor, ingresa un título válido.");
    return;
  }

  if (!validarCampo(descripcion)) {
    alert("Por favor, ingresa una descripción válida.");
    return;
  }

  formTicket.submit();
});

formEmpleado.addEventListener("submit", function (event) {
  event.preventDefault();

  const dni = document.getElementById("id_dni").value;
  const nombre = document.getElementById("id_nombre").value;
  const apellidos = document.getElementById("id_apellidos").value;
  const email = document.getElementById("id_email").value;
  const telefono = document.getElementById("id_telefono").value;

  if (!validarCampo(dni)) {
    alert("Por favor, ingresa un DNI válido.");
    return;
  }

  if (!validarCampoTexto(nombre)) {
    alert("Por favor, ingresa un nombre válido.");
    return;
  }

  if (!validarCampoTexto(apellidos)) {
    alert("Por favor, ingresa apellidos válidos.");
    return;
  }

  if (!validarEmail(email)) {
    alert("Por favor, ingresa un correo electrónico válido.");
    return;
  }

  if (!validarTelefono(telefono)) {
    alert("Por favor, ingresa un teléfono válido para el empleado.");
    return;
  }

  formEmpleado.submit();
});

function validarCampo(valor) {
  return valor.trim() !== "";
}

function validarEmail(valor) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(valor);
}

function validarTelefono(valor) {
  const regex = /^\d{9}$/;
  return regex.test(valor);
}

function validarCampoNumerico(valor) {
  const regex = /^\d+$/;
  return regex.test(valor);
}

function validarCampoTexto(valor) {
  const regex = /^[A-Za-z\s]+$/;
  return regex.test(valor);
}
