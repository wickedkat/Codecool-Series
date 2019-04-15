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

    showPreviousPage: function showPreviousPage() {
        if (Start === 0) {
            alert('This is the first page');

        } else {
            Start -= 15;
            End -= 15;
            dom.deleteRows(tableBody);
            mainpage.createTable(shows, Start, End)
        }
    },

    showNextPage: function showNextPage() {
        if (End > 1005) {
            alert('This is the last page')
        } else {
            Start += 15;
            End += 15;
            dom.deleteRows(tableBody);
            mainpage.createTable(shows, Start, End)
        }
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
        mainpage.createSeasonsModalUnderButton(show)

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

    createSeasonsModalUnderButton: function createSeasonsModalUnderButton(show ){
        let showSeasons = document.getElementById("button"+show.id).dataset.seasons;
        let showTitle = document.getElementById("button"+show.id).dataset.title;
        document.getElementById("button"+show.id).addEventListener("click", function() {
                let tableBodySeasons = document.getElementById('table-seasons');
                tableBodySeasons.innerHTML='';
                mainpage.createHeaderSeasonsModal(showTitle);
                mainpage.createTableSeasonsModal(showSeasons, tableBodySeasons);
                dom.showSeasonsModal()

            }

        )
    },

    createHeaderSeasonsModal: function createHeaderSeasonsModal (showTitle) {
        let header = document.getElementById('seasons-header');
        header.innerText = showTitle + ' seasons';
    },

    createTableSeasonsModal: function createTableSeasonsModal(showSeasons, tableBodySeasons) {
        let Seasons = showSeasons.split(',');
        for (let season of Seasons) {
            let row = document.createElement('tr');
            row.innerHTML = '<td>' + season + '</td>';
            tableBodySeasons.appendChild(row)
        }

    }

};















