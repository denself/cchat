__author__ = 'D.Ivanets'
import hashlib
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import inspect
from base import Base
from CChat.utils import random_string


class User(Base):
    __tablename__ = "user"
    __table_args__ = {'sqlite_autoincrement': True}
    id = sa.Column('id', sa.NUMERIC(10, 0), primary_key=True)
    email = sa.Column('email', sa.String(64), default='')
    email_conf = sa.Column('email_conf', sa.BOOLEAN, default=False)
    salt = sa.Column('salt', sa.String(32), default='')
    password = sa.Column('password', sa.String(255), default='')
    is_active = sa.Column('is_active', sa.BOOLEAN, default=True)
    dt_registered = sa.Column('dt_registered', sa.DateTime, default=datetime.utcnow)
    dt_last_active = sa.Column('dt_last_active', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return u"<%s(%s:'%s')>" % (self.__class__.__name__, self.id, self.email)

    def __unicode__(self):
        return self.__repr__()

    @property
    def pk(self):
        return int(self.id)

    @property
    def is_active(self):
        return True

    def set_password(self, password):
        self.salt = random_string(32)
        self.password = hashlib.sha512(password + self.salt).hexdigest()

    def is_pass_valid(self, password):
        return self.password == hashlib.sha512(password + self.salt).hexdigest()

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def save(self, *args, **kwargs):
        inspect(self).session.commit()


class AnonymousUser(object):
    id = None
    pk = None
    username = ''
    is_staff = False
    is_active = False
    is_superuser = False

    def __init__(self):
        pass

    def __str__(self):
        return 'AnonymousUser'

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 1  # instances always return the same hash value

    def save(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def set_password(self, raw_password):
        raise NotImplementedError

    def check_password(self, raw_password):
        raise NotImplementedError

    def get_group_permissions(self, obj=None):
        return set()

    def is_anonymous(self):
        return True

    def is_authenticated(self):
        return False