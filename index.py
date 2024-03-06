# it should always be open and running 
# this acts like an application listening to the http req from clients
import tornado.web
import tornado.ioloop

# basic get request
class basicRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("hello , this is python command from backend")

class listRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

if __name__ =="__main__":
  app = tornado.web.Application([
    (r"/", basicRequestHandler),
    (r"/animal",listRequestHandler)
  ])
  port = 8882
  app.listen(port)
  print(f"Application is ready and listening to {port}")
  # to run python and not stop it just after execution 
  tornado.ioloop.IOLoop.current().start()