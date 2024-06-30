$(function () {
    $(".toggle").on("click", function () {
        if ($(".item").hasClass("active")) {
            $(".item").removeClass("active");
        } else {
            $(".item").addClass("active");
        }
    });
});
document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    fetch('http://167.71.236.10/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                if (data.role === 'admin') {
                    window.location.href = '/admin-portal';
                } else if (data.role === 'cashier') {
                    window.location.href = '/cashier-portal';
                }
            } else {
                alert('Login failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

document.getElementById('signUpForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const email = document.getElementById('signUpEmail').value;
    const password = document.getElementById('signUpPassword').value;
    const role = document.getElementById('role').value;

    fetch('http://167.71.236.10/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password, role })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Sign up successful! You can now log in.');
            } else {
                alert('Sign up failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});