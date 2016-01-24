import tornado.ioloop
import tornado.web
import cisco7_web
import cisco_status_web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        index_template = "html_templates\index.html"
        self.render(index_template)


cisco7Handler = cisco7_web.cisco7web()
ciscoStatusHandler = cisco_status_web.cisco_status_web()


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/cisco7", cisco7Handler),
        (r"/ciscostatus", ciscoStatusHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
