import tornado.web
import cisco7
import web_template

# TODO: Validate strings before processing


def cisco7web():
    class Cisco7Handler(tornado.web.RequestHandler):
        def get(self):
            decoded_string = None
            html_head = web_template.get_html_head()
            html_bootstrap = web_template.get_bootstrap()
            html_nav = web_template.get_nav()
            cisco7_template = "html_templates\cisco7_template.html"
            self.render(cisco7_template, decoded_string=decoded_string, html_head=html_head, html_bootstrap=html_bootstrap, html_nav=html_nav)

        def post(self):
            html_head = web_template.get_html_head()
            html_bootstrap = web_template.get_bootstrap()
            html_nav = web_template.get_nav()
            decoded_string = cisco7.crack_cisco7(self.get_body_argument("coded_string"))
            cisco7_template = "html_templates\cisco7_template.html"
            self.render(cisco7_template, decoded_string=decoded_string, html_head=html_head, html_bootstrap=html_bootstrap, html_nav=html_nav)

    return (Cisco7Handler)