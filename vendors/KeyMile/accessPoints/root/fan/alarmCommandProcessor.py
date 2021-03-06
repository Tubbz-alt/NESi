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

from nesi import exceptions
from vendors.KeyMile.baseCommandProcessor import BaseCommandProcessor


class AlarmCommandProcessor(BaseCommandProcessor):
    __name__ = 'alarm'
    management_functions = ('main', 'cfgm', 'fm')
    access_points = ()

    from .alarmManagementFunctions import main
    from .alarmManagementFunctions import cfgm
    from .alarmManagementFunctions import fm
