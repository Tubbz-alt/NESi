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


from nesi.softbox.api import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    box_id = db.Column(db.Integer(), db.ForeignKey('box.id'))
    credentials_id = db.Column(db.Integer(), db.ForeignKey('credential.id'))
    name = db.Column(db.String(), default='user')
    level = db.Column(db.Enum('Super', 'Admin', 'Operator', 'User'), default='User')
    status = db.Column(db.Enum('Online', 'Offline'), default='Offline')
    profile = db.Column(db.Enum('root', 'admin', 'operator', 'commonuser'), default='commonuser')
    append_info = db.Column(db.String(), default='-----')
    reenter_num = db.Column(db.Integer(), default=3)
    reenter_num_temp = db.Column(db.Integer(), default=3)
    lock_status = db.Column(db.Enum('Locked', 'Unlocked'), default='Unlocked')