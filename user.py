from google.appengine.ext import db

class User(db.Model):
	username = db.StringProperty()

	@classmethod
	def create(cls,uname):
		u = cls(username=uname)
		u.put()
		

	@classmethod
	def create_user(cls,uname):
		q = db.GqlQuery("SELECT * from User where username = :1",uname)
		u = cls(username=uname)
		for r in q.run():
  			return r.username

	@classmethod
	def listofusers(cls):
		for p in User.all():
			print p.username


	@classmethod
	def deleteuser(cls,uname):
		persontodelete = db.GqlQuery("SELECT * from User where username = :1",uname)
		person = persontodelete[0];
		person.delete()
		return person




	