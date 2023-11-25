document.addEventListener("DOMContentLoaded", function () {
    var menuItem = document.querySelectorAll('.item-menu');

    function selectLink() {
        menuItem.forEach((item) => item.classList.remove('ativo'));
        this.classList.add('ativo');
        
        // Adicione a lógica para redirecionar para a página do gráfico quando o item "Dashboard" é clicado
        if (this.id === 'dashboard-item') {
            window.location.href = "/index"; // Substitua pelo caminho real
        }
    }

    menuItem.forEach((item) => item.addEventListener('click', selectLink));

    // Expandir o menu
    var btnExp = document.querySelector('#id-btn');
    var menuSide = document.querySelector('.menu-lateral');

    btnExp.addEventListener('click', function () {
        menuSide.classList.toggle('expandir');
    });
});
