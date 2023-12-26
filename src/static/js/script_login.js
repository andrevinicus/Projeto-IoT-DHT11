document.addEventListener("DOMContentLoaded", function() {
    var loginButton = document.getElementById("login-btn");

    if (loginButton) {
        loginButton.addEventListener("click", function() {
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;

            // Enviar dados do formulário via AJAX
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var response = JSON.parse(xhr.responseText);
                    
                    // Lógica para lidar com a resposta do servidor
                    if (response.status === "success") {
                        // Redirecionar para a rota do menu
                        window.location.href = menuRoute;
                    } else {
                        // Exibir mensagem de erro no formulário
                        alert(response.message);
                    }
                }
            };

            var data = "username=" + encodeURIComponent(username) + "&password=" + encodeURIComponent(password);
            xhr.send(data);
        });
    }
});
