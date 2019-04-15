let dom = {
    deleteRows: function deleteRows(tableBody){
        tableBody.innerHTML = '';
        return tableBody
    },

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
    showRolesModal: function showEpisodesModal() {
        document.getElementById('roles-modal').style.display = "flex";
    },

    hideRolesModal: function hideEpisodesModal() {
        document.getElementById('roles-modal').style.display="none";
    },

};


