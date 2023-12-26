document.addEventListener("DOMContentLoaded", function () {
    var menuItem = document.querySelectorAll('.item-menu');

    function selectLink() {
        // Remover a classe 'ativo' de todos os itens do menu
        menuItem.forEach((item) => item.classList.remove('ativo'));
        
        // Adicionar a classe 'ativo' ao item do menu clicado
        this.classList.add('ativo');

        // Atualizar os dados do menu usando AJAX
        var itemId = this.dataset.itemId; // Assume que você tem um atributo data-item-id em seus elementos do menu
        updateMenuData(itemId);
    }

    // Adicionar o ouvinte de evento de clique a cada item do menu
    menuItem.forEach((item) => item.addEventListener('click', selectLink));

    // Função para atualizar os dados do menu usando AJAX
    function updateMenuData(itemId) {
        // Fazer solicitação AJAX para obter dados do servidor
        fetch("/atualizar-menu?id=" + itemId)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Erro de rede: ${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                // Lógica para atualizar a interface com os novos dados
                console.log(data);
                // Exemplo: Atualizar conteúdo do menu, exibir informações, etc.
            })
            .catch(error => {
                console.error("Erro ao buscar dados do menu:", error);
                // Lógica para lidar com erros, como exibir uma mensagem de erro
            });
    }

    // Restante do seu código...
});
