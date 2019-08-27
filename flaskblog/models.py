
from flaskblog import db,login_manager
from datetime import datetime
from flask_login import UserMixin

#decorator to manage sessions

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



##usermixin handles sessions for us
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(10),nullable = False,unique = True)
    email = db.Column(db.String(20),nullable = False,unique = True)
    image_file = db.Column(db.String(20),nullable = False,default = 'default.jpg')
    password = db.Column(db.String(60),nullable = False)

    #posts tells the one to many relationship between user table and Post table.post is foreign key.
    post = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):

        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title= db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime,nullable = False,default =datetime.utcnow)
    content= db.Column(db.Text,nullable = False)

    #user_id foreign key to connect to user table
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"