from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import secrets
import string

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

group_members = db.Table(
    "group_members",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("group.id"), primary_key=True)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(255))
    groups = db.relationship(
        "Group",
        secondary= group_members,
        back_populates="members"
    )
    owned_groups = db.relationship(
      "Group",
      back_populates="owner",
      foreign_keys="Group.owner_id"
)

    def set_password(self, password):
      self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
      return check_password_hash(self.password_hash, password) 

    
    def __repr__(self):
      return "User: {}, {}, {}".format(self.id, self.username, self.email)


class Group( db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), index = True, unique = True)
   code = db.Column(db.String(20), unique=True, nullable=False)
   description = db.Column(db.Text)
   owner_id = db.Column(db.Integer, 
      db.ForeignKey("user.id"), 
      nullable=False
    )
   created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )
   updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
   is_private = db.Column(db.Boolean, default=False, nullable=False)
   max_members = db.Column(db.Integer)
   members = db.relationship(
        "User",
        secondary=group_members,
        back_populates="groups"
    )
   owner = db.relationship(
    "User",
    back_populates="owned_groups",
    foreign_keys=[owner_id]
)
   def generate_group_code(self):
    characters = string.ascii_uppercase + string.digits
    self.code = "".join(
        secrets.choice(characters)
        for _ in range(8)
    )
    


