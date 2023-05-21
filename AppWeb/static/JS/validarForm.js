function validarForm() {
  const numeroserie = document.getElementById('id_nserie').value;

  if (numeroserie === "" || numeroserie === null || numeroserie === "None") {
    alert('El campo numero de serie debe rellenarse');
    return false;
  }

  return true;
}
document.getElementById('miFormulario').addEventListener('submit', validarForm);