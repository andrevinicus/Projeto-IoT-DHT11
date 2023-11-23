function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    if (username.trim() === "" || password.trim() === "") {
        errorMessage.innerText = "Nome de usuário e senha são obrigatórios.";
        errorMessage.style.display = "block";
        return false;
    }

    return true;
}
