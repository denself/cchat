# -*- coding: utf-8 -*-
import datetime
import uuid
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from base import Base

__author__ = 'D.Ivanets'


class EmailConfirmation(Base):
    __tablename__ = 'email_confirmation'
    __table_args__ = {}
    hash = sa.Column('hash', sa.String(32), primary_key=True)
    user_id = sa.Column('user_id', sa.Numeric(10, 0), sa.ForeignKey('user.id'))
    dt_create = sa.Column('dt_create', sa.DateTime, default=datetime.datetime.utcnow)
    dt_use = sa.Column('dt_use', sa.DateTime)

    user = relationship('User')

    def __init__(self, user):
        self.user = user
        self.hash = uuid.uuid1().get_hex()

    def use(self):
        self.dt_use = datetime.datetime.utcnow()
        self.user.email_conf = True

    def __repr__(self):
        return u"<%s(%s)>" % (self.__class__.__name__, self.hash,)

    def __unicode__(self):
        return self.__repr__()
