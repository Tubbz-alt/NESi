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

from nesi.softbox.api.schemas.service_port_schemas import *


class AlcatelServicePortSchema(ServicePortSchema):
    class Meta:
        model = ServicePort
        fields = ServicePortSchema.Meta.fields + ('max_unicast_mac', 'qos_profile_id', 'pvid', 'pvc')
