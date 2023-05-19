window.addEventListener('load', init, false);
function init() {
    let div = document.querySelector('.ocultar-y-mostrar');
    div.style.display = 'block';
    let mostrar = document.querySelector('.ocultar-mostrar1');
    mostrar.style.display = 'none';
    let ocultar = document.querySelector('.ocultar-mostrar2');
    mostrar.addEventListener('click', function (e) {
        if (div.style.display === 'block') {
            ocultar.style.display = 'block';
            mostrar.style.display = 'none';

        } else {
            div.style.display = 'block';
            mostrar.style.display = 'none';
            ocultar.style.display = 'block';
        }
    }, false);

    ocultar.addEventListener('click', function (e) {
        if (div.style.display === 'none') {
            mostrar.style.display = 'none';
            ocultar.style.display = 'block';
        } else {
            div.style.display = 'none';
            mostrar.style.display = 'block';
            ocultar.style.display = 'none';
        }
    }, false);
}

