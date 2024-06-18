document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registerForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission for now

        // Perform client-side validation (example)
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirm_password = document.getElementById('confirm_password').value;

        if (username.trim() === '' || email.trim() === '' || password.trim() === '' || confirm_password.trim() === '') {
            alert('All fields are required.');
            return;
        }

        if (password !== confirm_password) {
            alert('Passwords do not match.');
            return;
        }

        // If validation passes, submit the form
        form.submit();
    });
});
