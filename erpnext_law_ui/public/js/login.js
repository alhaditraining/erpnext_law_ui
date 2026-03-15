window.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".law-login-form");
    if (!form) return;

    const emailField = form.querySelector("#login_email");
    if (emailField && !emailField.value) {
        emailField.focus();
    }
});
