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
from ..models.model_models import Model
from ..schemas.version_schemas import VersionsSchema


class ModelSchema(ma.ModelSchema):
    class Meta:
        model = Model
        fields = ('id', 'name', 'vendor_id', 'versions', '_links')

    versions = ma.Nested(VersionsSchema.VersionSchema, many=True)

    _links = ma.Hyperlinks(
        {'self': ma.URLFor('show_model', id='<id>')})


class ModelsSchema(ma.ModelSchema):
    class Meta:
        fields = ('members', 'count', '_links')

    class ModelSchema(ma.ModelSchema):
        class Meta:
            model = Model
            fields = ('id', 'name', 'versions', '_links')

        versions = ma.Nested(VersionsSchema.VersionSchema, many=True)

        _links = ma.Hyperlinks(
            {'self': ma.URLFor(
                'show_model', id='<id>')})

    members = ma.Nested(ModelSchema, many=True)

    _links = ma.Hyperlinks(
        {'self': ma.URLFor('show_models')})
