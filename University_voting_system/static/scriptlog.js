document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('loginForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission for now

        // Perform client-side validation (example)
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (username.trim() === '' || password.trim() === '') {
            alert('Username and password are required.');
            return;
        }

        // If validation passes, submit the form
        form.submit();
    });
});
