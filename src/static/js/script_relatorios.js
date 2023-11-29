document.addEventListener('DOMContentLoaded', function () {
    const reportContent = document.getElementById('report-content');
    const dateFilterForm = document.createElement('form');
    const startDateInput = document.createElement('input');
    const endDateInput = document.createElement('input');
    const filterButton = document.createElement('button');
    const table = document.createElement('table');
    const tableBody = document.createElement('tbody');

    startDateInput.type = 'date';
    startDateInput.id = 'startDate';
    startDateInput.name = 'startDate';

    endDateInput.type = 'date';
    endDateInput.id = 'endDate';
    endDateInput.name = 'endDate';

    filterButton.type = 'button';
    filterButton.textContent = 'Filtrar';
    filterButton.addEventListener('click', function () {
        filterTable();
    });

    dateFilterForm.appendChild(document.createTextNode('Data de Início: '));
    dateFilterForm.appendChild(startDateInput);
    dateFilterForm.appendChild(document.createTextNode('Data de Fim: '));
    dateFilterForm.appendChild(endDateInput);
    dateFilterForm.appendChild(filterButton);

    reportContent.appendChild(dateFilterForm);
    reportContent.appendChild(table);
    table.appendChild(tableBody);

    function filterTable() {
        const startDate = startDateInput.value;
        const endDate = endDateInput.value;

        // Simule dados filtrados (substitua esta parte pelo seu próprio código)
        const filteredData = getFilteredData(startDate, endDate);

        renderTable(filteredData);
    }

    function renderTable(data) {
        // Limpa o corpo da tabela
        tableBody.innerHTML = '';

        if (Array.isArray(data) && data.length > 0) {
            data.forEach(({ date, description, value }) => {
                const row = tableBody.insertRow();
                const cell1 = row.insertCell(0);
                const cell2 = row.insertCell(1);
                const cell3 = row.insertCell(2);

                cell1.textContent = date;
                cell2.textContent = description;
                cell3.textContent = value;
            });
        } else {
            // Se não houver dados, exibe uma mensagem na tabela
            const row = tableBody.insertRow();
            const cell = row.insertCell(0);
            cell.textContent = 'Nenhum dado disponível para o período especificado';
        }
    }

    function getFilteredData(startDate, endDate) {
        // Faz uma solicitação AJAX para o servidor
        return fetch(`/get_reports?start_date=${startDate}&end_date=${endDate}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Erro na solicitação: ${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                return data; // Retorna os dados recebidos do servidor
            })
            .catch(error => {
                console.error('Erro ao obter dados do servidor:', error);
                return []; // Retorna uma array vazia em caso de erro
            });
    }

    // Renderiza a tabela inicialmente sem filtragem
    filterTable();
});
