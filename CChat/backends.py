# -*- coding: utf-8 -*-
from model import User
from sqlalchemy.orm.exc import NoResultFound
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class EmailBackend(object):
    """
    Class provides user authentication using email as a login
    """
    supports_anonymous_user = True
    supports_inactive_user = True

    def __init__(self):
        self.session = settings.SESSION()

    def authenticate(self, username=None, password=None):
        try:
            validate_email(username)
        except ValidationError:
            return None

        try:
            user = self.session.query(User).filter_by(email=username).one()
        except NoResultFound:
            return None

        if user.is_pass_valid(password) and user.is_active and user.email_conf:
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            user = self.session.query(User).filter_by(id=user_id).one()
        except NoResultFound:
            return None

        return user