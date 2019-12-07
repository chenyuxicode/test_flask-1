from application import db

# User table
class Users(db.Model):
    # Define the name of the table
    __tablename__ = 'yuhu_users'

    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    # username
    username = db.Column(db.String(128), nullable=False)
    # password
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return self.username