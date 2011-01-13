from teamroom import request

class Handler(request.RequestHandler):
    def get(self):

        path = "templates/index.html"
        template_values = {}

        self.render_template(path, template_values)

