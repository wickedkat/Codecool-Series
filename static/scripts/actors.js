let actors = {
    getActorsDetails: function getActorsDetails(actorId) {
        let actorsRequest = new XMLHttpRequest();
        actorsRequest.open('GET', `/actors/${actorId}`);
        actorsRequest.onloadstart = dom.showLoadingModal();
        actorsRequest.onloadend = function () {
            dom.hideLoadingModal();
            let response = actorsRequest.response;
            let actor = JSON.parse(response);
            actors.createTableRolesModal(actor);
        };
        actorsRequest.send()

    },

    createTableRolesModal: function createTableRolesModal(actor) {
        let tableBody = document.getElementById("table-roles");
        dom.deleteRows(tableBody);
        let header = document.getElementById("roles-header");
        header.innerHTML = actor.name + '  roles';
        for (role in actor) {
            actor.createRowRolesModal(tableBody, role);
        }
        dom.showRolesModal()
    },

    createRowRolesModal: function createRowRolesModal(tableBody, role) {
            let row = document.createElement('tr');
            row.innerHTML = '<td>' + role.character_name + '</td>' +
                '<td>' + role.title + '</td>' +
                '<td class="longtext">' + role.overview + '</td>';
            tableBody.appendChild(row)
        }

};