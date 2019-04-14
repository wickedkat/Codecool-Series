let episodes = {


    getEpisodesDetails: function getEpisodesDetails(show, seasonId) {
        let episodesRequest = new XMLHttpRequest();
        episodesRequest.open("GET", `/seasons/${show}/episodes`);
        episodesRequest.setRequestHeader("Content-type", "application/json");
        episodesRequest.onloadstart = dom.showLoadingModal();
        episodesRequest.onloadend = function () {
            dom.hideLoadingModal();
            let response = episodesRequest.response;
            let seasons = JSON.parse(response);
            episodes.createTableEpisodesModal(seasons, seasonId)


        };
        episodesRequest.send();
    },

    createTableEpisodesModal: function createTableEpisodesModal(seasons, seasonId) {
        let tableBody = document.getElementById('table-episodes');
        let episodes;
        if (tableBody.hasChildNodes()) {
            dom.deleteRows(tableBody)
        }
        for (let season of seasons) {
            if (season.season_id == seasonId) {
                episodes = season.episodes;
                this.createHeaderEpisodesModal(season);
                for (let episode of episodes) {
                    this.createRowEpisodesModal(episode, tableBody)
                }
            }
        }
        dom.showEpisodesModal()
    },

    createRowEpisodesModal: function createRowEpisodesModal(episode, tableBody) {
        let row = document.createElement('tr');
        row.innerHTML = '<td>' + episode.episode_number + '</td>' +
            '<td>' + episode.episode_title + '</td>' +
            '<td>' + episode.episode_overview + '</td>';
        tableBody.appendChild(row)
    },

    createHeaderEpisodesModal: function createHeaderEpisodesModal(season) {
        header = document.getElementById('episodes-header');
        header.innerHTML= season.title + '   episodes'
    }



};





