let authentication = {

    loginHandler: function(){
    handleLogin()},
    registrationHandler: function() {
        handleRegistration()
    }
};

/*                            LOGIN FUNCTIONS                                  */

let message;
let registerUsername;
let loginUsername;


function handleLogin() {
    let form = document.getElementById('login-form');
    let username = form.querySelector('input[name="username"]');
    let password = form.querySelector('input[name="password"]');
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        validateLogin(username, password, loginUser);
    });
}

function validateLogin(username, password, callback) {
    let loginErrors = [];
    if (username.value.length === 0) {
        loginErrors.push("Username can't be empty");
        username.classList.add('invalid')
    } else {
        username.classList.remove('invalid')
    }
    if (password.value.length === 0) {
        loginErrors.push("Password can't be empty");
        password.classList.add('invalid')
    } else {
        password.classList.remove('invalid')
    }
    if (loginErrors.length > 0){
        displayLoginErrors(loginErrors);
    }else {
        callback(username, password)}
}


function displayLoginErrors(errors) {
    let errorLine = document.getElementById('login-error');
    errorLine.innerHTML = errors.join("<br>");
    errorLine.classList.add('text-invalid')
}

function loginUser(username, password) {
    let loginRequest = new XMLHttpRequest();
    loginRequest.onreadystatechange = function () {
        if (loginRequest.readyState == 4) {
            if (loginRequest.status == 200) {
                message = JSON.parse(loginRequest.response);
                afterServerResponse(message)
            } else {
                alert('Connection error. Try again later.');
            }
        }

    };
    loginUsername = username.value;
    let loginPassword = password.value;
    let loginData = {'username': loginUsername, 'password': loginPassword};
    loginData = JSON.stringify(loginData);
    loginRequest.open("POST", '/login');
    loginRequest.setRequestHeader('Content-Type', 'application/json');
    loginRequest.send(loginData);
}




/*                          REGISTRATION FUNCTIONS                          */


function handleRegistration() {
    let form = document.getElementById('register-form');
    let username = form.querySelector('input[name="username"]');
    let password = form.querySelector('input[name="password"]');
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        validateRegistration(username, password, registerUser);

    });

}

function validateRegistration(username, password, callback) {
    let registrationErrors = [];
    if (username.value.length === 0) {
        registrationErrors.push("Username can't be empty");
        username.classList.add('invalid')
    } else {
        username.classList.remove('invalid')

    }
    if (password.value.length === 0) {
        registrationErrors.push("Password can't be empty");
        password.classList.add('invalid')
    } else {
        password.classList.remove('invalid')
    }
    if (registrationErrors.length > 0){
        displayRegistrationErrors(registrationErrors);
    } else {
        callback(username, password)}
}



function displayRegistrationErrors(errors) {
    let errorLine = document.getElementById('register-error');
    errorLine.innerHTML = errors.join("<br>");
    errorLine.classList.add('text-invalid')

}

function registerUser(username, password) {
    let registerRequest = new XMLHttpRequest();
    registerRequest.onreadystatechange = function () {
        if (registerRequest.readyState == 4) {
            if (registerRequest.status == 200) {
                message = JSON.parse(registerRequest.response);
                afterServerResponse(message)
            } else {
                alert('Connection error. Try again later.');
            }
        }

    };
    registerUsername = username.value;
    let registerPassword = password.value;
    let registerData = {'username': registerUsername, 'password': registerPassword};
    registerData = JSON.stringify(registerData);
    registerRequest.open("POST", "/register");
    registerRequest.setRequestHeader('Content-Type', 'application/json');
    registerRequest.send(registerData);

}

function afterServerResponse(message) {
    dom.hideRegisterModal();
    dom.hideLoginModal();
    alert(message);
    dom.viewAfterUserForm(message)
}

