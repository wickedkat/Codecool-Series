sort = {
    sortByNumericOrder: function sortByNumericOrder(direction, condition) {

        switch (direction) {
            case 'asc':
                shows = shows.sort(function (obj1, obj2) {
                    return obj1[condition]  - obj2[condition]
                });
                deleteRows();
                createTable(shows, Start, End);
                break;


            case 'desc':
                shows = shows.sort(function (obj1, obj2) {
                    return obj2[condition] - obj1[condition]
                });
                deleteRows();
                createTable(shows, Start, End);
                break;


        }
    },

    sortByAlphabeticalOrder: function sortByAlphabeticalOrder(direction, condition) {
        debugger;
        switch (direction) {
            case 'asc':
                shows = shows.sort(function (obj1, obj2) {
                    return obj2[condition] < obj1[condition]
                });
                deleteRows();
                createTable(shows, Start, End);
                break;


            case 'desc':
                shows = shows.sort(function (obj1, obj2) {
                    return obj2[condition] > obj1[condition]
                });
                deleteRows();
                createTable(shows, Start, End);



        }
    },
};