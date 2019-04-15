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
        header.innerHTML = actor[0].actor_name + '  roles';
        for (i =0; i<actor.length; i ++) {
            debugger;
            actors.createRowRolesModal(tableBody, actor[i]);
        }
        dom.showRolesModal()
    },

    createRowRolesModal: function createRowRolesModal(tableBody, actor) {
            let row = document.createElement('tr');
            row.innerHTML = '<td>' + actor.character_name + '</td>' +
                '<td><a href="'+actor.id+'">' + actor.title + '</a></td>' +
                '<td class="longtext">' + actor.overview + '</td>';
            tableBody.appendChild(row)
        }

};