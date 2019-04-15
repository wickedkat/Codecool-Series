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

};


