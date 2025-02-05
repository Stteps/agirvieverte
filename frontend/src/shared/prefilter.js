import Cookies from "js-cookie";

const csrftoken = Cookies.get("csrftoken");

$.ajaxPrefilter( (settings, original, xhr) => {
    xhr.withCredentials = true;
    if (['post','put','delete'].includes(settings.type.toLowerCase()) && !settings.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});