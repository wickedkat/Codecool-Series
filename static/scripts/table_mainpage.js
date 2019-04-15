let shows;
let show;
let tableBody;
let i;
let Start;
let End;

mainpage = {


    getDataMainPage: function getDataMainPage() {
        let dataRequest = new XMLHttpRequest();
        dataRequest.open('GET', '/shows');
        dataRequest.onloadstart = dom.showLoadingModal();
        dataRequest.onloadend = function () {
            dom.hideLoadingModal();
            shows = JSON.parse(dataRequest.response);
            tableBody = document.getElementById("shows_mainpage");
            if (tableBody.hasChildNodes()) {
                dom.deleteRows(tableBody)
            }
            mainpage.createTable(shows, 0, 15);
            Start = 0;
            End = 15

        };
        dataRequest.send();
    },

    createTable: function createTable(shows, start, end) {
        for (i = start; i < end; i++) {
            show = shows[i];
            mainpage.createRow(show)
        }
    },
    createRow: function createRow(show) {
        let row = document.createElement('tr');
        tableBody.appendChild(row);
        row.innerHTML = '<td>' + mainpage.addLinkToShowTitle(show.id, show.title) + '</td>' +
            '<td>' + show.year + '</td>' +
            '<td>' + show.runtime + '</td>' +
            '<td>' + mainpage.limitGenres(show.genre) + '</td>' +
            '<td>' + show.rating + '</td>' +
            '<td>' + mainpage.createTrailerIcon(show.trailer) + '</td>' +
            '<td>' + mainpage.createHomepageIcon(show.homepage) + '</td>' +
            '<td>' + mainpage.seasonsHandler(show.seasons_titles, show) + '</td>' +
            '<td class="action-column"><button type="button" class="icon-button"><i class="fa fa-edit fa-fw"></i></button><button type="button" class="icon-button"><i class="fa fa-trash fa-fw"></i></button></td>'
        /*mainpage.createSeasonsModalUnderButton(show)*/

    },

    deleteRows: function deleteRows() {
        tableBody.innerHTML = '';
        return tableBody
    },

    createTrailerIcon: function createTrailerIcon(trailer) {
        return '<a href="' + trailer + '" target="_blank"><img src="/static/assets/video-player.png" height="14px" width="14px" align="center" ></a>'
    },

    createHomepageIcon: function createHomepageIcon(homepage) {
        return '<a href="' + homepage + '" target="_blank"><img src="/static/assets/house.png" height="14px" width="14px" align="center" ></a>'
    },

    limitGenres: function limitGenres(listgenres) {
        let allGenres = listgenres;
        let genres = [];
        if (allGenres[0] !== null) {
            for (let j = 0; j < 3; j++) {
                if (j < allGenres.length) {
                    genres.push(allGenres[j])
                } else {
                    break
                }
            }
            return genres
        } else {
            return 'Not assigned'
        }
    },

    seasonsHandler: function seasonsHandler(seasons, show) {

        if (seasons.length === 0) {
            return 'No seasons'
        } else {
            return '<button type="button" id="button'+show.id+'" data-seasons ="' + show.seasons_titles + '" data-title="'+show.title+'">' + seasons.length + ' seasons</button>';
        }
    },

    addLinkToShowTitle: function addLinkToShowTitle( id, title) {
        return '<a href="/'+id+'">'+title+' </a>'

    },

};















