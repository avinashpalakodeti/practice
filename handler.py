import webapp2
from models.user import User
from handlers import BaseHandler
import logging as log

class MainHandler(BaseHandler):
    def get(self):
        users = ["user"+str(i) for i in range(10)]
        self.render_response("user.html",users=users)

class Data(BaseHandler):    
    def post(self):
        b=self.request.get("name")
        self.response.write(b)

        d=self.request.get("uname")
        print d

        f = self.request.get("upname")
        print f

        a=User.create_user(b)
        self.response.write(a)

        if b == a:
            self.response.write("already exists")

        else:
            self.response.write("created")
            User.create(b)
        
        c=User.listofusers()

        if d == a:
            e=User.deleteuser(d)
            print "deleted user"
        else:
            print "username didnt exist"

        if b == a:
            g=User.update(f)
            print "updated"

    

