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
    }

};


