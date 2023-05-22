/* Validación de formulario de Equipo */
var formEquipo = document.getElementById('miFormulario');

formEquipo.addEventListener('submit', function(event) {
  var fechaAdquisicionInput = document.getElementById('id_fechaAdquisicion');
  var fechaPuestaMarchaInput = document.getElementById('id_fechaPuestaMarcha');
  var fechaAdquisicion = new Date(fechaAdquisicionInput.value);
  var fechaPuestaMarcha = new Date(fechaPuestaMarchaInput.value);
  var today = new Date();

  if (fechaAdquisicion > today || fechaPuestaMarcha > today) {
    event.preventDefault();
    alert('Las fechas de adquisición y puesta en marcha no pueden ser futuras.');
  }
});

/* Validación de formulario de Ticket */
var formTicket = document.getElementById('miFormulario');

formTicket.addEventListener('submit', function(event) {
  var fechaAperturaInput = document.getElementById('id_fechaApertura');
  var fechaResolucionInput = document.getElementById('id_fechaResolucion');
  var fechaApertura = new Date(fechaAperturaInput.value);
  var fechaResolucion = new Date(fechaResolucionInput.value);
  var today = new Date();
  var provTelefonoInput = document.getElementById('id_provTelefono');
  var provTelefono = provTelefonoInput.value.trim();

  if (fechaApertura > today || fechaResolucion > today) {
    event.preventDefault();
    alert('Las fechas de apertura y resolución no pueden ser futuras.');
  }

  if (!/^[\d]+$/.test(provTelefono)) {
    event.preventDefault();
    alert('El teléfono del proveedor solo puede contener números.');
  }
});

/* Validación de formulario de Empleado */
var formEmpleado = document.getElementById('miFormulario');

formEmpleado.addEventListener('submit', function(event) {
  var dniInput = document.getElementById('id_dni');
  var dni = dniInput.value.trim();
  var emailInput = document.getElementById('id_email');
  var email = emailInput.value.trim();
  var telefonoInput = document.getElementById('id_telefono');
  var telefono = telefonoInput.value.trim();

  if (!/^[0-9]{8}[A-Z]$/.test(dni)) {
    event.preventDefault();
    alert('El DNI del empleado debe contener 8 números seguidos de una letra mayúscula.');
  }

  if (!/@/.test(email)) {
    event.preventDefault();
    alert('El campo de correo electrónico debe contener un símbolo "@".');
  }

  if (!/^[\d]+$/.test(telefono)) {
    event.preventDefault();
    alert('El teléfono del empleado solo puede contener números.');
  }
});


