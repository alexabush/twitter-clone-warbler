from project import db, bcrypt
from flask_login import UserMixin

FollowersFollowee = db.Table('follows',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('followee_id', db.Integer, db.ForeignKey('users.id', ondelete="cascade")),
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id', ondelete="cascade")),
    db.CheckConstraint('follower_id != followee_id', name="no_self_follow"))

UserLikesMessages = db.Table('likes',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id', ondelete="cascade")),
    db.Column('message_id', db.Integer, db.ForeignKey('messages.id', ondelete="cascade")))

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    name = db.Column(db.Text)
    username = db.Column(db.Text, unique=True)
    image_url = db.Column(db.Text)
    header_image_url = db.Column(db.Text)
    bio = db.Column(db.Text)
    location = db.Column(db.Text)
    password = db.Column(db.Text)
    messages = db.relationship('Message', backref='user', lazy='dynamic') #one-to-many
    likes = db.relationship(
        'Message',
        secondary=UserLikesMessages, #one-to-many
        backref=db.backref('liked', lazy='dynamic'),
        lazy='dynamic')
    followers = db.relationship( #many-to-many, making link between two rows in the same table
       "User",
        secondary=FollowersFollowee,
        primaryjoin=(FollowersFollowee.c.follower_id == id),
        secondaryjoin=(FollowersFollowee.c.followee_id == id),
        backref=db.backref('following', lazy='dynamic'),
        lazy='dynamic')

    def __init__(self,
                 email,
                 username,
                 password,
                 name='',
                 location='',
                 bio='',
                 image_url='/static/images/default-pic.png',
                 header_image_url='/static/images/warbler-hero.jpg'):
        self.email = email
        self.username = username
        self.name = name
        self.location = location
        self.bio = bio
        self.image_url = image_url
        self.header_image_url = header_image_url
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8') #hashing is taken care of here

#### instance methods on user class ##########################

    def __repr__(self):
        return f"#{self.id}: email: {self.email} - username: {self.username}"

    def is_followed_by(self, user):
        return bool(self.followers.filter_by(id=user.id).first())

    def is_following(self, user):
        return bool(self.following.filter_by(id=user.id).first())

    def likes_message(self, message_id):
        return bool(self.likes.filter_by(id=message_id).first())

#put this in message model
    def is_liked_by(self, user_id):
        return bool(self.liked.filter_by(id=user_id).first())
##################################################################

    @classmethod
    def authenticate(cls, username, password):
        found_user = cls.query.filter_by(username=username).first()
        if found_user:
            is_authenticated = bcrypt.check_password_hash(
                found_user.password, password)
            if is_authenticated:
                return found_user
        return False
