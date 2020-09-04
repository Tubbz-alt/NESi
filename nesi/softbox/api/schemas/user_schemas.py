# This file is part of the NESi software.
#
# Copyright (c) 2020
# Original Software Design by Ilya Etingof <https://github.com/etingof>.
#
# Software adapted by inexio <https://github.com/inexio>.
# - Janis Groß <https://github.com/unkn0wn-user>
# - Philip Konrath <https://github.com/Connyko65>
# - Alexander Dincher <https://github.com/Dinker1996>
#
# License: https://github.com/inexio/NESi/LICENSE.rst

from nesi.softbox.api import ma
from ..models.user_models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('id', 'box', 'credentials_id', 'name', '_links')

    box = ma.Hyperlinks(
        {'_links': {
            'self': ma.URLFor('show_box', id='<box_id>')}})

    _links = ma.Hyperlinks(
        {'self': ma.URLFor('show_user', box_id='<box_id>', id='<id>'),
         'collection': ma.URLFor('show_users', box_id='<box_id>')})


class UsersSchema(ma.ModelSchema):
    class Meta:
        fields = ('members', 'count', '_links')

    class UserSchema(ma.ModelSchema):
        class Meta:
            model = User
            fields = ('id', 'name', '_links')

        _links = ma.Hyperlinks(
            {'self': ma.URLFor(
                'show_user', box_id='<box_id>', id='<id>')})

    members = ma.Nested(UserSchema, many=True)

    _links = ma.Hyperlinks(
        {'self': ma.URLFor('show_users', box_id='<box_id>')})