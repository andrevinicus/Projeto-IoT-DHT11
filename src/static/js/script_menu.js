document.addEventListener("DOMContentLoaded", function () {
    var menuItem = document.querySelectorAll('.item-menu');
    var btnExp = document.querySelector('#id-btn');
    var menuSide = document.querySelector('.menu-lateral');
    var chartContainer = document.querySelector('.chart-container');
    var myChart;

    function selectLink() {
        this.classList.add('ativo');
        menuItem.forEach((item) => {
            if (item !== this) {
                item.classList.remove('ativo');
            }
        });
        localStorage.setItem('selectedMenuItem', this.querySelector('a').getAttribute('href'));
    }

    function toggleMenu() {
        menuSide.classList.toggle('expandir');
        updateChartSize();
    }

    function updateChartSize() {
        if (myChart) {
            // Destrua o gráfico existente
            myChart.destroy();
        }

        // Crie um novo gráfico com base no tamanho atual do contêiner
        myChart = createChart(chartContainer);

        // Inicia a busca de dados
        fetchData();
    }

    menuItem.forEach((item) => item.addEventListener('click', selectLink));
    btnExp.addEventListener('click', toggleMenu);

    menuSide.classList.remove('expandir');

    // Verifica se há uma seleção anterior e aplica a classe 'ativo'
    var selectedMenuItem = localStorage.getItem('selectedMenuItem');
    if (selectedMenuItem) {
        menuItem.forEach((item) => {
            var itemHref = item.querySelector('a').getAttribute('href');
            if (itemHref === selectedMenuItem) {
                item.classList.add('ativo');
            }
        });
    }

    // Cria o gráfico inicial
    updateChartSize();

    // Atualiza o tamanho do gráfico quando a janela é redimensionada
    window.addEventListener('resize', updateChartSize);

    function createChart(container) {
        const ctx = container.querySelector('canvas').getContext('2d');
        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [
                    {
                        label: 'Temperatura',
                        data: [],
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 2,
                    },
                    {
                        label: 'Umidade',
                        data: [],
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 2,
                    },
                ],
            },
            options: {
                responsive: true, // Torna o gráfico responsivo
                maintainAspectRatio: false, // Não mantém a proporção do gráfico
                scales: {
                    x: {
                        type: 'time',
                        time: { unit: 'second' },
                        position: 'bottom',
                    },
                    y: { beginAtZero: true },
                },
            },
        });
    }

    function fetchData() {
        fetch('/data')
            .then((response) => response.json())
            .then((data) => {
                myChart.data.labels = data.timestamps.map((timestamp) => new Date(timestamp));
                myChart.data.datasets[0].data = data.temperature;
                myChart.data.datasets[1].data = data.humidity;
                myChart.update();
            })
            .catch((error) => console.error('Erro ao buscar dados:', error));
    }

    setInterval(fetchData, 5000);
});
