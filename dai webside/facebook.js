document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Here you would typically send the data to a server for authentication
    console.log('Email:', email);
    console.log('Password:', password);

    // For demonstration purposes, we'll just show an alert
    alert('Login attempt with email: ' + email);
});