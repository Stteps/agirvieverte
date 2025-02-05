from django.views.generic import TemplateView


class Error500View(TemplateView):
    template_name = "errors/error.html"
    extra_context = {
        "code": 500,
        "code_image": "server_error.png",
        "code_title": "Internal server error",
        "message": "Sorry... An internal server error occured and has been reported. We will try to fix it as soon as \
            possible. Meanwhile, you can go back to <a class='error_message text-decoration-none text-dark' href='/'>\
                Inadgo homepage</a>",
    }


class Error403View(TemplateView):
    template_name = "errors/error.html"
    extra_context = {
        "code": 403,
        "code_image": "permission_denied.png",
        "code_title": "Permission denieds",
        "message": "It seems that you don't have sufficient permissions to access this content, please go back to \
                <a class='error_message text-decoration-none text-dark' href='/'>Inadgo homepage</a>",
    }


class Error404View(TemplateView):
    template_name = "errors/error.html"
    extra_context = {
        "code": 404,
        "code_image": "not_found.png",
        "code_title": "Page not found",
        "message": "Oops... It seems like the page you requested was not found, please check your URL or go back to \
                <a class='error_message text-decoration-none text-dark' href='/'>Inadgo homepage</a>",
    }
