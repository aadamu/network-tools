import tornado.web
import cisco7

# TODO: Validate strings before processing


def cisco7web():
    class Cisco7Handler(tornado.web.RequestHandler):
        def get(self):
            decoded_string = None
            cisco7_template = "html_templates\cisco7_template.html"
            self.render(cisco7_template, decoded_string=decoded_string)

        def post(self):
            decoded_string = cisco7.crack_cisco7(self.get_body_argument("coded_string"))
            cisco7_template = "html_templates\cisco7_template.html"
            self.render(cisco7_template, decoded_string=decoded_string)

    return (Cisco7Handler)