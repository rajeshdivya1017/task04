
async function registerUser() {

    const username =
        document.getElementById("registerUsername").value;

    const email =
        document.getElementById("registerEmail").value;

    const password =
        document.getElementById("registerPassword").value;

    const response = await fetch('/register', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            username,
            email,
            password
        })
    });

    const data = await response.json();

    if (data.success) {

        window.location.href = "login.html";

    } else {

        document.getElementById("registerError").innerText =
            data.message;
    }
}

async function loginUser() {

    const username =
        document.getElementById("loginUsername").value;

    const password =
        document.getElementById("loginPassword").value;

    const response = await fetch('/login', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            username,
            password
        })
    });

    const data = await response.json();

    if (data.success) {

        window.location.href = "dashboard.html";

    } else {

        document.getElementById("loginError").innerText =
            data.message;
    }
}

async function loadDashboard() {

    const response = await fetch('/dashboard');

    const data = await response.json();

    if (!data.success) {

        window.location.href = "login.html";

        return;
    }

    document.getElementById("welcome").innerText =
        `Welcome, ${data.username}!`;

    document.getElementById("role").innerText =
        `Role: ${data.role}`;

    document.getElementById("createdAt").innerText =
        `Created At: ${data.created_at}`;
}


async function logoutUser() {

    await fetch('/logout');

    window.location.href = "login.html";
}