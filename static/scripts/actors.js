let actors = {
    getActorsDetails: function getActorsDetails(actorId) {
        let actorsRequest = new XMLHttpRequest();
        actorsRequest.open('GET', "/actors/details");
        actorsRequest.onloadstart = dom.showLoadingModal();
        actorsRequest.onloadend = function () {
            dom.hideLoadingModal();
            let response = actorsRequest.response;
            let actors = JSON.parse(response);
            createTableRolesModal(actorId, actors);
        };
        actorsRequest.send()

    },

    addNewActor: function addNewActor() {
        let form = document.getElementById("add-actor-form");
        let name = form.querySelector('input[name="name"]');
        let birthday = form.querySelector('input[name="birthday"]');
        let death = form.querySelector('input[name="death"]');
        let biography = form.querySelector('input[name="biography"]');
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            debugger;
            validateActorForm(name, birthday, death, biography, sendActorToServer)
    })
    }
};

function createTableRolesModal(actorId, actors) {
    for (let actor of actors) {
        if (actor.id == actorId) {
            let tableBody = document.getElementById("table-roles");
            dom.deleteRows(tableBody);
            let header = document.getElementById("roles-header");
            header.innerHTML = actor.name + '  roles';
            let roles = actor.roles;
            createRowRolesModal(tableBody, roles);
            break
        }
    }
    dom.showRolesModal()
}

function createRowRolesModal(tableBody, roles) {
    for (let role of roles) {
        let row = document.createElement('tr');
        row.innerHTML = '<td>' + role.character_name + '</td>' +
            '<td>' + role.title + '</td>' +
            '<td class="longtext">' + role.overview + '</td>';
        tableBody.appendChild(row)
    }
}

function validateActorForm(name, birthday, death, biography, callback){
    let formErrors = [];
    if (name.value.length === 0) {
        formErrors.push("Name can't be empty");
        name.classList.add('invalid')
    } else {
        name.classList.remove('invalid')
    }
    if (birthday.value.length === 0) {
        formErrors.push("Birthday can't be empty");
        birthday.classList.add('invalid')
    } else {
        birthday.classList.remove('invalid')
    }
    if (formErrors.length > 0) {
        displayFormErrors(formErrors);
    } else {
        callback(name, birthday, death, biography)
    }


}


function displayFormErrors(errors) {
    let errorLine = document.getElementById('add-actor-error');
    errorLine.innerHTML = errors.join("<br>");
    errorLine.classList.add('text-invalid')
}

function sendActorToServer(name, birthday, death, biography) {
    let addActorRequest = new XMLHttpRequest();
    addActorRequest.onreadystatechange = function () {
        if (addActorRequest.readyState == 4) {
            if (addActorRequest.status == 200) {
                let response = JSON.parse(addActorRequest.response);
                message = response['message'];
                afterServerResponse(message)
            } else {
                alert('Connection error. Try again later.');
            }
        }

    };
    let actorName = name.value;
    let actorBirthday = birthday.value;
    let actorDeath = death.value;
    let actorBiography = biography.value;
    let actorData = {'name': actorName, 'birthday': actorBirthday,
                    'death': actorBirthday, 'biography':actorBiography};
    actorData = JSON.stringify(actorData);
    addActorRequest.open("POST", "/actors/add");
    addActorRequest.setRequestHeader('Content-Type', 'application/json');
    addActorRequest.send(actorData);

}

function afterServerResponse(message) {
    dom.hideAddActorForm();
    clearInputAddActor();
    alert(message)
}


function clearInputAddActor() {
    let form = document.getElementById("add-actor-form");
    let name = form.querySelector('input[name="name"]');
    name.value = '';
    let birthday = form.querySelector('input[name="birthday"]');
    birthday.value='';
    let death = form.querySelector('input[name="death"]');
    death.value ='';
    let biography = form.querySelector('input[name="biography"]');
    biography.value = '';
}

