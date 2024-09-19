function showLogin() {
    document.getElementById('login-form').classList.remove('hidden');
    document.getElementById('signup-form').classList.add('hidden');
}

function showSignup() {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('signup-form').classList.remove('hidden');
}

// Handle login form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    
    // Basic validation
    if (username === '' || password === '') {
        document.getElementById('loginMessage').textContent = 'Please fill in all fields.';
        return;
    }
    
    // Example of login logic (replace with actual authentication logic)
    if (username === 'user' && password === 'pass') {
        document.getElementById('loginMessage').textContent = 'Login successful!';
    } else {
        document.getElementById('loginMessage').textContent = 'Invalid username or password.';
    }
});

// Handle signup form submission
document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('signupUsername').value;
    const password = document.getElementById('signupPassword').value;
    const confirmPassword = document.getElementById('signupConfirmPassword').value;
    
    // Basic validation
    if (username === '' || password === '' || confirmPassword === '') {
        document.getElementById('signupMessage').textContent = 'Please fill in all fields.';
        return;
    }
    
    if (password !== confirmPassword) {
        document.getElementById('signupMessage').textContent = 'Passwords do not match.';
        return;
    }
    
    // Example of signup logic (replace with actual registration logic)
    document.getElementById('signupMessage').textContent = 'Signup successful! You can now log in.';
});

