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
import uuid

from nesi.softbox.api import db
from .port_models import Port


class Card(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    box_id = db.Column(db.Integer, db.ForeignKey('box.id'))
    subrack_id = db.Column(db.Integer, db.ForeignKey('subrack.id'))
    ports = db.relationship('Port', backref='Card', lazy='dynamic')
    ppc = db.Column(db.Enum('8', '16', '32', '48', '64'), default='32')
    product = db.Column(db.Enum('xdsl', 'vdsl', 'adsl', 'sdsl', 'ftth-pon', 'ftth', 'mgnt'),
                        nullable=False, default='vdsl')

    # Alcatel specific data
    description = db.Column(db.String(), default='None')
    position = db.Column(db.String())
    entry_vlan_number = db.Column(db.Integer())
    planned_type = db.Column(db.Enum('rdlt-c', 'rant-a', 'nant-a', 'nrnt-a', 'fant-f', 'relt-a', 'nelt-b', 'fglt-b',
                                     'ngfc-f', 'empty'), default='empty')
    dual_tag_mode = db.Column(db.Boolean(), default=False)
    actual_type = db.Column(db.Enum('rdlt-c', 'rant-a', 'nant-a', 'nrnt-a', 'fant-f', 'relt-a', 'nelt-b', 'fglt-b',
                                    'ngfc-f', 'empty'), default='empty')
    admin_state = db.Column(db.Enum('0', '1'), default='0')  # Alcatel: 0 => disabled, 1 => unlock
    operational_state = db.Column(db.Enum('0', '1'), default='0')  # Alcatel: 0 => disabled, 1 => enabled
    err_state = db.Column(db.Enum('no-error', 'error', 'type-mismatch'), default='no-error')
    availability = db.Column(db.Enum('available', 'unavailable', 'not-installed'), default='available')
    alarm_profile = db.Column(db.Enum('none'), default='none')
    capab_profile = db.Column(db.Enum('32port_xDSL', 'fttu_lt', 'not_applicable'), default='32port_xDSL')
    manufacturer = db.Column(db.Enum('ALCL', ''), default='')
    mnemonic = db.Column(db.Enum('RDLT-C', 'FGLT-B', 'FANT-F', 'NGFC-F', 'RANT-A', 'NANT-A', 'NRNT-A', 'RELT-A',
                                 'NELT-B', 'NGFC-F', ''), default='')
    pba_code = db.Column(db.String(), default='')
    fpba_code = db.Column(db.String(), default='')
    fpba_ics = db.Column(db.String(), default='')
    clei_code = db.Column(db.String(), default='')
    serial_no = db.Column(db.String(), default='')
    failed_test = db.Column(db.String(), default='00:00:00:00')
    lt_restart_time = db.Column(db.String(), default='1970-01-01:00:00:00')
    lt_restart_cause = db.Column(db.Enum('poweron', 'poweroff', 'other'), default='poweron')
    lt_restart_num = db.Column(db.Integer(), default=0)
    mgnt_entity_oamipaddr = db.Column(db.String(), default='0.0.0.0')
    mgnt_entity_pairnum = db.Column(db.Integer(), default=0)
    dual_host_ip = db.Column(db.String(), default='0.0.0.0')
    dual_host_loc = db.Column(db.Enum('none'), default='none')
    sensor_id = db.Column(db.Integer(), default=0)
    act_temp = db.Column(db.Integer(), default=0)
    tca_low = db.Column(db.Integer(), default=0)
    tca_high = db.Column(db.Integer(), default=0)
    shut_low = db.Column(db.Integer(), default=0)
    shut_high = db.Column(db.Integer(), default=0)
    restrt_cnt = db.Column(db.Integer(), default=0)
    vce_profile_id = db.Column(db.Integer(), default=None, nullable=True)
    vplt_autodiscover = db.Column(db.Enum('enabled', 'disabled'), default='disabled')
    vect_fallback_spectrum_profile = db.Column(db.Integer(), default=None)
    vect_fallback_fb_vplt_com_fail = db.Column(db.Boolean, default=False)
    vect_fallback_fb_cpe_cap_mism = db.Column(db.Boolean, default=False)
    vect_fallback_fb_conf_not_feas = db.Column(db.Boolean, default=False)

    # Huawei specific data
    board_name = db.Column(db.String(), default='H83BVCMM')
    board_status = db.Column(db.Enum('Normal', 'Failed', 'Active_normal', 'Standby_failed'), default='Normal')
    sub_type_0 = db.Column(db.String(), default='')
    sub_type_1 = db.Column(db.String(), default='')
    power_status = db.Column(db.String(), default='POWER-ON')
    power_off_cause = db.Column(db.String(), default='-')
    power_off_time = db.Column(db.String(), default='-')
    temperature = db.Column(db.String(), default='68C')
