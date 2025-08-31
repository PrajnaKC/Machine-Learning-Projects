document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const loginResult = document.getElementById('loginResult');
    loginResult.textContent = 'Logging in...';
    try {
        const response = await fetch('http://localhost:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        if (data.success) {
            loginResult.textContent = 'Login successful! Redirecting...';
            setTimeout(() => {
                window.location.href = 'index.html';
            }, 1200);
        } else {
            loginResult.textContent = 'Login failed: ' + (data.error || 'Invalid credentials');
        }
    } catch (error) {
        loginResult.textContent = 'Error connecting to backend.';
    }
});
