let dom = {
    showLoadingModal: function showLoadingModal() {
        document.getElementById('loading-modal').style.display = "flex";
    },
    hideLoadingModal: function hideLoadingModal() {
        document.getElementById('loading-modal').style.display = "none";
    },

    showSeasonsModal: function showSeasonsModal() {
        document.getElementById('seasons-modal').style.display = "flex";
    },

    hideSeasonsModal: function hideSeasonsModal() {
        document.getElementById('seasons-modal').style.display = "none";
    },

    showEpisodesModal: function showEpisodesModal() {
        document.getElementById('episodes-modal').style.display = "flex";
    },

    hideEpisodesModal: function hideEpisodesModal() {
        document.getElementById('episodes-modal').style.display="none";
    },

    deleteRows: function deleteRows(tableBody){
            tableBody.innerHTML = '';
            return tableBody
    }

};

