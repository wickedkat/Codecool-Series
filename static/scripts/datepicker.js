window.onload = addScriptsToDocument(useDatepicker);

function addScriptsToDocument(callback) {
    let dateField = document.createElement("input");
    dateField.setAttribute("type", "date");
    if (dateField.type != "date") { // if browser doesn't support input type="date", load files for jQuery UI Date Picker
        callback(dateField)
    }
}
function useDatepicker(dateField) {
    if (dateField.type != "date") { // if browser doesn't support input type="date", initialize date picker widget:
        jQuery(function ($) { // on document.ready
            $('#birthday').datepicker();
        })
    }
    if (dateField.type != "date") { // if browser doesn't support input type="date", initialize date picker widget:
        jQuery(function ($) { // on document.ready
            $('#death').datepicker();
        })
    }
}
