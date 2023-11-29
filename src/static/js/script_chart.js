document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('myChart').getContext('2d');
    let myChart = createChart(ctx);
    let intervalId; // Variável para armazenar o ID do intervalo

    function createChart(ctx) {
        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Temperatura',
                    data: [],
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2
                }, {
                    label: 'Umidade',
                    data: [],
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                scales: {
                    x: {
                        type: 'time',
                        time: { unit: 'second' },
                        position: 'bottom'
                    },
                    y: { beginAtZero: true }
                }
            }
        });
    }

    function fetchData() {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                myChart.data.labels = data.timestamps.map(timestamp => new Date(timestamp));
                myChart.data.datasets[0].data = data.temperature;
                myChart.data.datasets[1].data = data.humidity;
                myChart.update();
            })
            .catch(error => console.error('Erro ao buscar dados:', error));
    }

    function updateChart() {
        fetchData();
    }

    // Atualiza o tamanho do gráfico quando a janela é redimensionada
    window.addEventListener('resize', function () {
        updateChartSize();
    });

    // Expandir o menu
    var btnExp = document.querySelector('#id-btn');
    var menuSide = document.querySelector('.menu-lateral');

    btnExp.addEventListener('click', function () {
        menuSide.classList.toggle('expandir');
        updateChartSize();
    });

    // Atualiza o tamanho do gráfico quando o menu é expandido ou retraído
    function updateChartSize() {
        // Parar o intervalo antes de ajustar o tamanho do gráfico
        clearInterval(intervalId);

        // Destrói o gráfico existente antes de criar um novo
        myChart.destroy();
        myChart = createChart(ctx);

        // Reinicia o intervalo após a criação do novo gráfico
        intervalId = setInterval(updateChart, 5000);
    }

    // Iniciar o intervalo e armazenar o ID
    intervalId = setInterval(updateChart, 5000);
});
