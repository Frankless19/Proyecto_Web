// Validación de formulario de Equipo
var formEquipo = document.getElementById('miFormulario');

formEquipo.addEventListener('submit', function(event) {
  var provTelefonoInput = document.getElementById('id_provTelefono');
  var provTelefono = provTelefonoInput.value.trim();
  
  if (!/^[\d]+$/.test(provTelefono)) {
    event.preventDefault();
    alert('El teléfono del proveedor solo puede contener números.');
  }
});

// Validación de formulario de Ticket
var formTicket = document.getElementById('miFormulario');

formTicket.addEventListener('submit', function(event) {
  var empleadoDniInput = document.getElementById('id_empleado-dni');
  var empleadoDni = empleadoDniInput.value.trim();
  
  if (!/^[0-9]{8}[A-Z]$/.test(empleadoDni)) {
    event.preventDefault();
    alert('El DNI del empleado debe contener 8 números seguidos de una letra mayúscula.');
  }
});

// Validación de formulario de Empleado
var formEmpleado = document.getElementById('miFormulario');

formEmpleado.addEventListener('submit', function(event) {
  var emailInput = document.getElementById('id_email');
  var email = emailInput.value.trim();
  
  if (!/@/.test(email)) {
    event.preventDefault();
    alert('El campo de correo electrónico debe contener un símbolo "@"');
  }
});

