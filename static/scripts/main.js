window.onload = mainpage.getDataMainPage(0,15);

function main() {
    if(window.location.pathname === "/"){
        init();
    }

    if(window.location.pathname.startsWith('/show')) {
        initSubpage();
    }


}

function init() {
    authentication.loginHandler();
    authentication.registrationHandler();

}

function initSubpage() {
    let username = localStorage.getItem('username');

}


main();

