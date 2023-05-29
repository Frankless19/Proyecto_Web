/* Validación de formulario de Equipo */
var formEquipo = document.getElementById("miFormulario");

formEquipo.addEventListener("submit", function (event) {
  var fechaAdquisicionInput = document.getElementById("id_fechaAdquisicion");
  var fechaPuestaMarchaInput = document.getElementById("id_fechaPuestaMarcha");
  var fechaAdquisicion = new Date(fechaAdquisicionInput.value);
  var fechaPuestaMarcha = new Date(fechaPuestaMarchaInput.value);
  var today = new Date();

  if (fechaAdquisicion > today || fechaPuestaMarcha > today) {
    event.preventDefault();
    var mensajeError = document.getElementById("mensajeError");
    mensajeError.innerHTML =
      "Las fechas de adquisición y puesta en marcha no pueden ser futuras.";
    fechaAdquisicionInput.classList.add("campo-invalido");
    fechaPuestaMarchaInput.classList.add("campo-invalido");
  }
});

/* Validación de formulario de Ticket */
var formTicket = document.getElementById("miFormulario");

formTicket.addEventListener("submit", function (event) {
  var fechaAperturaInput = document.getElementById("id_fechaApertura");
  var fechaResolucionInput = document.getElementById("id_fechaResolucion");
  var fechaApertura = new Date(fechaAperturaInput.value);
  var fechaResolucion = new Date(fechaResolucionInput.value);
  var today = new Date();
  var provTelefonoInput = document.getElementById("id_provTelefono");
  var provTelefono = provTelefonoInput.value.trim();

  if (fechaApertura > today || fechaResolucion > today) {
    event.preventDefault();
    var mensajeError = document.getElementById("mensajeError");
    mensajeError.innerHTML =
    "Revise los campos en rojo de su formulario, tenga en cuenta que: Solo se admiten numeros en el campo Teléfono y Las fechas de apertura y resolución no pueden ser futuras.";
    fechaAperturaInput.classList.add("campo-invalido");
    fechaResolucionInput.classList.add("campo-invalido");
  }

  if (!/^[\d]+$/.test(provTelefono)) {
    event.preventDefault();
    var mensajeError = document.getElementById("mensajeError");
    mensajeError.innerHTML = "Revise los campos en rojo de su formulario, tenga en cuenta que: Solo se admiten numeros en el campo Teléfono y Las fechas de apertura y resolución no pueden ser futuras.";
    provTelefonoInput.classList.add("campo-invalido");
  }
});

/* Validación de formulario de Empleado */
var formEmpleado = document.getElementById("miFormulario");

formEmpleado.addEventListener("submit", function (event) {
  var dniInput = document.getElementById("id_dni");
  var dni = dniInput.value.trim();
  var emailInput = document.getElementById("id_email");
  var email = emailInput.value.trim();
  var telefonoInput = document.getElementById("id_telefono");
  var telefono = telefonoInput.value.trim();

  if (!/^[0-9]{8}[A-Z]$/.test(dni)) {
    event.preventDefault();
    var mensajeError = document.getElementById("mensajeError");
    mensajeError.innerHTML =
      "Revise los campos en rojo de su formulario, tenga en cuenta que: El DNI del empleado, debe tener 8 numeros y una letra mayúscula al final, el campo del correo debe contener un simbolo @ y El teléfono solo puede contener numeros.";
    dniInput.classList.add("campo-invalido");
  }

  if (!/@/.test(email)) {
    event.preventDefault();
    var mensajeError = document.getElementById("mensajeError");
    mensajeError.innerHTML =
      "Revise los campos en rojo de su formulario, tenga en cuenta que: El DNI del empleado, debe tener 8 numeros y una letra mayúscula al final, el campo del correo debe contener un simbolo @ y El teléfono solo puede contener numeros.";
    emailInput.classList.add("campo-invalido");
  }

  if (!/^[\d]+$/.test(telefono)) {
    event.preventDefault();
    var mensajeError = document.getElementById("mensajeError");
    mensajeError.innerHTML =
      "Revise los campos en rojo de su formulario, tenga en cuenta que: El DNI del empleado, debe tener 8 numeros y una letra mayúscula al final, el campo del correo debe contener un simbolo @ y El teléfono solo puede contener numeros.";
    telefonoInput.classList.add("campo-invalido");
  }
});
