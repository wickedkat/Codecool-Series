let dom = {

    showLoginModal: function showLoginModal() {
        document.getElementById('login-modal').style.display = "flex";
    },
    hideLoginModal: function hideLoginModal() {
        document.getElementById('login-modal').style.display = "none";
    },

    showRegisterModal: function showRegisterModal() {
        document.getElementById('register-modal').style.display = "flex";
    },

    hideRegisterModal: function hideRegisterModal() {
        document.getElementById('register-modal').style.display = "none";
    },

    viewAfterUserForm: function viewAfterUserForm(message) {
        switch (message) {
            case 'Registration successful':
                document.getElementById('Login').style.display = "none";
                document.getElementById('Register').style.display = "none";
                let hello = document.getElementById('hello');
                hello.innerText = 'hello ' + registerUsername;
                hello.style.display = "inline-block";
                document.getElementById('Logout').innerText = 'Logout';
                document.getElementById('Logout').style.display = "inline-block";
                showVoting();
                break;

            case 'Log in successful':
                document.getElementById('Login').style.display = "none";
                document.getElementById('Register').style.display = "none";
                let hellolog = document.getElementById('hello');
                hellolog.innerText = 'hello ' + loginUsername;
                hellolog.style.display = "inline-block";
                document.getElementById('Logout').innerText = 'Logout';
                document.getElementById('Logout').style.display = "inline-block";
                break;

            case 'User already in database':
                break;

            case 'Wrong password. Try again.':
                break;

            case 'User doesn\'t exist. Please register':
                setTimeout(function () {
                    this.showRegisterModal()
                }, 500);
                break;
        }
    }

};

