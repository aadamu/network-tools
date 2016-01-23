import tornado.ioloop
import tornado.web
import cisco7

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        index_template = "templates\index.html"
        self.render(index_template)

# TODO: Validate strings before processing

class cisco7Handler(tornado.web.RequestHandler):
    def get(self):
        decoded_string = None
        cisco7_template = "templates\cisco7_template.html"
        self.render(cisco7_template, decoded_string=decoded_string)

    def post(self):
        decoded_string = cisco7.crack_cisco7(self.get_body_argument("coded_string"))
        cisco7_template = "templates\cisco7_template.html"
        self.render(cisco7_template, decoded_string=decoded_string)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/cisco7", cisco7Handler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
