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
                this.deleteRows()
            }
            this.createTable(shows, 0, 15);
            Start = 0;
            End = 15

        };
        dataRequest.send();
    },

    createTable: function createTable(shows, start, end) {
        for (i = start; i < end; i++) {
            show = shows[i];
            this.createRow(show)
        }
    },


};















