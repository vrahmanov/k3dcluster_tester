import tornado.ioloop
import tornado.web
import socket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        title = "k3d BOMBAMELA",socket.gethostname()
        bgcolor = "dodgerblue"
        self.render("template.html", title=title, bgcolor=bgcolor)
        print(self.request)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8082)
    tornado.ioloop.IOLoop.current().start()

