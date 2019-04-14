let dom = {
    showLoadingModal: function showLoadingModal() {
        document.getElementById('loading-modal').style.display = "flex";
    },
    hideLoadingModal: function hideLoadingModal() {
        document.getElementById('loading-modal').style.display = "none";
    },

    showLoginModal: function showLoginModal() {
        document.getElementById('login-modal').style.display = "flex";
    },
    hideLoginModal: function hideLoginModal() {
        document.getElementById('login-modal').style.display = "none";
    },

    showRegisterModal: function showRegisterModal() {
        document.getElementById('register-modal').style.display = "flex";
    },

    hideRegisterModal: function hideRegisterModal() {
        document.getElementById('register-modal').style.display = "none";
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
    },

    showRolesModal: function showEpisodesModal() {
        document.getElementById('roles-modal').style.display = "flex";
    },

    hideRolesModal: function hideEpisodesModal() {
        document.getElementById('roles-modal').style.display="none";
    },

    showAddActorForm: function showAddActorForm() {
        document.getElementById('add-actor').style.display="block";
    },
    hideAddActorForm: function showAddActorForm() {
        document.getElementById('add-actor').style.display = "none";

    },
    viewAfterUserForm: function viewAfterUserForm(status, username) {
        switch (status) {
            case 1:
                document.getElementById('Login').style.display = "none";
                document.getElementById('Register').style.display = "none";
                let hello = document.getElementById('hello');
                hello.innerText = 'hello ' + username;
                hello.style.display = "inline-block";
                document.getElementById('Logout').innerText = 'Logout';
                document.getElementById('Logout').style.display = "inline-block";
                localStorage.removeItem('username');
                localStorage.setItem( 'username', username);
                break;

            case 2:
                break;


            case 3:
                setTimeout(function () {
                    this.showRegisterModal()
                }, 500);
                break;
        }
    },

};

