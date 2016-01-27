import tornado.ioloop
import tornado.web
import cisco7_web
import cisco_status_web
import os
import web_template


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        html_head = web_template.get_html_head()
        html_bootstrap = web_template.get_bootstrap()
        index_template = "html_templates\index.html"
        self.render(index_template, html_head=html_head, html_bootstrap=html_bootstrap)


cisco7Handler = cisco7_web.cisco7web()
ciscoStatusHandler = cisco_status_web.cisco_status_web()


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/cisco7", cisco7Handler),
        (r"/ciscostatus", ciscoStatusHandler),
        (r"/static", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
