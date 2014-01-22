import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "static_url_prefix" : "/",
#     "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
#     "login_url": "/login",
#     "xsrf_cookies": True,
}

application = tornado.web.Application([
    (r"/", MainHandler)
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    print "OK"
    tornado.ioloop.IOLoop.instance().start()
