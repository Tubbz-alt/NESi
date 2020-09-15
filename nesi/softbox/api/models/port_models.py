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
from .ont_models import Ont
from .cpe_models import Cpe


class Port(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    box_id = db.Column(db.Integer, db.ForeignKey('box.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    onts = db.relationship('Ont', backref='Port', lazy='dynamic')
    cpes = db.relationship('Cpe', backref='Port', lazy='dynamic')

    # Alcatel data
    description = db.Column(db.String())
    type = db.Column(db.Enum('pon', 'ethernet-line'), default='pon')
    shutdown = db.Column(db.Boolean(), default=False)
    speed = db.Column(db.Enum('10M', '1G', '10G'), default='1G')
    operational_state = db.Column(db.Enum('0', '1', '2'), default='0')  # Alcatel: 0 => down, 1 => up, 2 => not-appl; Huawei: 0 => deactivated, 1 => activated, 2 => activating
    admin_state = db.Column(db.Enum('0', '1', '2'), default='0')  # Alcatel: 0 => down, 1 => up, 2 => not-appl; Huawei: 0 => deactivated, 1 => activated, 2 => activating
    upstream = db.Column(db.Integer(), default=0)
    downstream = db.Column(db.Integer(), default=0)
    upstream_max = db.Column(db.Integer(), default=100000)
    downstream_max = db.Column(db.Integer(), default=100000)
    cur_init_state = db.Column(db.Enum('up', 'down', 'shutdown'), default='down')
    auto_negotiation = db.Column(db.Boolean(), default=True)
    mtu = db.Column(db.Integer(), default=1500)
    noise_margin_up = db.Column(db.Integer(), default=0)
    noise_margin_down = db.Column(db.Integer(), default=0)
    tgt_noise_margin_up = db.Column(db.Integer(), default=0)
    tgt_noise_margin_down = db.Column(db.Integer(), default=0)
    attenuation_up = db.Column(db.Integer(), default=0)
    attenuation_down = db.Column(db.Integer(), default=0)
    attained_upstream = db.Column(db.Integer(), default=0)
    attained_downstream = db.Column(db.Integer(), default=0)
    threshold_upstream = db.Column(db.Integer(), default=0)
    threshold_downstream = db.Column(db.Integer(), default=0)
    max_delay_upstream = db.Column(db.Integer(), default=0)
    max_delay_downsteam = db.Column(db.Integer(), default=0)
    if_index = db.Column(db.Integer(), default=94502912)
    high_speed = db.Column(db.Integer(), default=0)
    connector_present = db.Column(db.Enum('not-applicable'), default='not-applicable')
    media = db.Column(db.FLOAT, default=0.0)
    largest_pkt_size = db.Column(db.Integer(), default=0)
    curr_bandwith = db.Column(db.Integer(), default=1244000000)
    phy_addr = db.Column(db.String(), default='')
    last_chg_opr_stat = db.Column(db.String(), default='352-02:55:19')
    pkts_unknown_proto = db.Column(db.Integer(), default=0)
    in_octets = db.Column(db.Integer(), default=0)
    out_octets = db.Column(db.Integer(), default=0)
    in_ucast_pkts = db.Column(db.Integer(), default=0)
    out_ucast_pkts = db.Column(db.Integer(), default=0)
    in_mcast_pkts = db.Column(db.Integer(), default=0)
    out_mcast_pkts = db.Column(db.Integer(), default=0)
    in_broadcast_pkts = db.Column(db.Integer(), default=0)
    out_broadcast_pkts = db.Column(db.Integer(), default=0)
    in_discard_pkts = db.Column(db.Integer(), default=0)
    out_discard_pkts = db.Column(db.Integer(), default=0)
    in_err_pkts = db.Column(db.Integer(), default=0)
    out_err_pkts = db.Column(db.Integer(), default=0)
    in_octets_hc = db.Column(db.Integer(), default=0)
    out_octets_hc = db.Column(db.Integer(), default=0)
    in_ucast_pkts_hc = db.Column(db.Integer(), default=0)
    out_ucast_pkts_hc = db.Column(db.Integer(), default=0)
    in_mcast_pkts_hc = db.Column(db.Integer(), default=0)
    out_mcast_pkts_hc = db.Column(db.Integer(), default=0)
    in_broadcast_pkts_hc = db.Column(db.Integer(), default=0)
    out_broadcast_pkts_hc = db.Column(db.Integer(), default=0)
    position = db.Column(db.String())
    diag_avail_status = db.Column(db.Enum('no-error'), default='no-error')
    los = db.Column(db.Enum('not-available'), default='not-available')
    tx_fault = db.Column(db.Enum('no-tx-fault'), default='no-tx-fault')
    tx_power = db.Column(db.String(), default='"3.85 dBm"')
    rx_power = db.Column(db.Enum('not-available'), default='not-available')
    tx_bias_current = db.Column(db.String(), default='"16.17 mA"')
    supply_voltage = db.Column(db.String(), default='"3.23 VDC"')
    temperature = db.Column(db.String(), default='"57.39 degrees Celsius"')
    temperature_tca = db.Column(db.Enum('normal-value'), default='normal-value')
    voltage_tca = db.Column(db.Enum('normal-value'), default='normal-value')
    bias_current_tca = db.Column(db.Enum('normal-value'), default='normal-value')
    tx_power_tca = db.Column(db.Enum('normal-value'), default='normal-value')
    rx_power_tca = db.Column(db.Enum('normal-value'), default='normal-value')
    rssi_profile_id = db.Column(db.Integer, default=65535)
    rssi_state = db.Column(db.Enum('enable'), default='enable')
    inp_up = db.Column(db.Integer(), default=0)
    inp_dn = db.Column(db.Integer(), default=0)
    interl_us = db.Column(db.Integer(), default=0)
    interl_dn = db.Column(db.Integer(), default=0)
    cur_op_mode = db.Column(db.Enum('default'), default='default')
    rinit_1d = db.Column(db.Integer(), default=0)
    actual_tps_tc_mode = db.Column(db.Enum('ptm'), default='ptm')
    rtx_mode_up = db.Column(db.Enum('unknown'), default='unknown')
    rtx_mode_dn = db.Column(db.Enum('unknown'), default='unknown')
    total_reset_attempt = db.Column(db.Integer(), default=0)
    success_reset_attempt = db.Column(db.Integer(), default=0)
    service_profile_id = db.Column(db.Integer(), default=None, nullable=True)
    spectrum_profile_id = db.Column(db.Integer(), default=None, nullable=True)
    vect_profile_id = db.Column(db.Integer(), default=None, nullable=True)
    dpbo_profile_id = db.Column(db.Integer(), default=None, nullable=True)
    qos_profile_id = db.Column(db.Integer(), default=None, nullable=True)
    inventory_status = db.Column(db.Enum('cage-empty', 'no-error'), default='cage-empty')
    alu_part_num = db.Column(db.String(), default='not-available')
    tx_wavelength = db.Column(db.String(), default='not-available')
    fiber_type = db.Column(db.Enum('not-available', 'single-mode'), default='not-available')
    rssi_sfptype = db.Column(db.String(), default='not-available')
    mfg_name = db.Column(db.String(), default='NEOPHOTONICS')
    mfg_oui = db.Column(db.String(), default='000000')
    mfg_date = db.Column(db.String(), default='27/10/2016')
    egress_port = db.Column(db.Boolean(), default=False)

    # Huawei data
    ont_autofind = db.Column(db.Boolean(), default=False)
    loopback = db.Column(db.Enum('enable', 'disable'), default='disable')
    dynamic_profile = db.Column(db.Enum('Bind no dynamic-profile', ''), default='')
    dynamic_profile_index = db.Column(db.String(), default='-')
    dynamic_profile_name = db.Column(db.String(), default='-')
    line_template = db.Column(db.Enum('No.72 SMART_5000_UP_1000_1', ''), default='')
    line_template_num = db.Column(db.Integer(), nullable=True, default=82)
    alarm_template = db.Column(db.String(), default='No.1 DEFVAL')
    alarm_template_num = db.Column(db.Integer(), nullable=False, default=1)
    line_spectrum_profile = db.Column(db.Enum('No.1000 ADSL2plus', 'No.1001 VDSL', ''), default='')
    spectrum_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    upbo_profile = db.Column(db.Enum('No.1 DEFVAL', ''), default='')
    upbo_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    dpbo_profile = db.Column(db.Enum('No.1080 DPBO_80', ''), default='')
    dpbo_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    rfi_profile = db.Column(db.Enum('No.1 DEFVAL', ''), default='')
    rfi_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    noise_margin_profile = db.Column(db.Enum('No.1000 ADSL_6dB', ''), default='')
    noise_margin_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    virtual_noise_profile = db.Column(db.Enum('No.1 DEFVAL', ''), default='')
    virtual_noise_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    inm_profile = db.Column(db.Enum('No.1 DEFVAL', ''), default='')
    inm_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    sos_profile = db.Column(db.Enum('No.1 DEFVAL', ''), default='No.1 DEFVAL')
    sos_profile_num = db.Column(db.Integer(), nullable=True, default=1)
    hardware = db.Column(db.Enum('XTU-C', 'ATU-C'), default='XTU-C')
    last_up_time = db.Column(db.String(), default='2019-09-17 11:46:10+01:00')
    last_down_time = db.Column(db.String(), default='2019-09-17 11:45:24+01:00')
    show_time = db.Column(db.Integer(), nullable=False, default=0)
    nte_power_status = db.Column(db.Enum('on', 'off'), default='off')
    current_operational_mode = db.Column(db.String(), default='No Protocol Selected')
    total_count_of_line_training = db.Column(db.Integer(), nullable=False, default=0)
    result_last_initialization = db.Column(db.Enum('No failure'),
                                           default='No failure')  # TODO: Find corresponding value(s)
    total_bytes_us = db.Column(db.Integer(), default=448203129)
    total_packets_us = db.Column(db.Integer(), default=6386689)
    total_bytes_ds = db.Column(db.Integer(), default=430667320)
    total_packets_ds = db.Column(db.Integer(), default=6493472)
    total_discarded_packets_ds = db.Column(db.Integer(), default=0)
    channel_packets_discarded_ds = db.Column(db.Integer(), default=0)

    channel_ds_data_rate_profile = db.Column(db.Enum('No.1016 TEST_DSL_16000', ''), default='')
    channel_ds_data_rate_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    channel_us_data_rate_profile = db.Column(db.Enum('No.2001 UP_1000', ''), default='')
    channel_us_data_rate_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    channel_inp_delay_profile = db.Column(db.Enum('No.1000 ADSL', ''), default='')
    channel_inp_data_rate_profile_num = db.Column(db.Integer(), nullable=True, default=None)
    channel_ds_rate_adapt_ratio = db.Column(db.Integer(), nullable=True, default=None)
    channel_us_rate_adapt_ratio = db.Column(db.Integer(), nullable=True, default=None)
    standard_port_in_training = db.Column(db.String(), default='G.993.2-Annex B')
    current_power_management_state = db.Column(db.String(), default='Full-on state')
    retransmission_used_us = db.Column(db.String(), default='Unused, retransmission mode is forbidden')
    retransmission_used_ds = db.Column(db.String(), default='Unused, retransmission mode is forbidden')
    signal_attenuation_ds_1 = db.Column(db.FLOAT(), default=3.9)
    signal_attenuation_us_1 = db.Column(db.FLOAT(), default=5.5)
    line_attenuation_ds_1 = db.Column(db.FLOAT(), default=3.9)
    line_attenuation_us_1 = db.Column(db.FLOAT(), default=5.5)
    act_line_rate_ds_1 = db.Column(db.Integer(), default=35584)
    act_line_rate_us_1 = db.Column(db.Integer(), default=4168)
    line_snr_margin_ds_1 = db.Column(db.FLOAT(), default=33.0)
    line_snr_margin_us_1 = db.Column(db.FLOAT(), default=39.2)
    vdsl_2_psd_class_mask = db.Column(db.String(), default='B998M2x')
    act_psd_ds = db.Column(db.String(), default='-')
    act_psd_us = db.Column(db.String(), default='-')
    act_klo_co = db.Column(db.String(), default='24')
    act_klo_cpe = db.Column(db.String(), default='30')
    us_1_band_act_klo_val = db.Column(db.String(), default='24')
    us_2_band_act_klo_val = db.Column(db.String(), default='24')
    us_3_band_act_klo_val = db.Column(db.String(), default='-')
    us_4_band_act_klo_val = db.Column(db.String(), default='-')
    ds_1_band_act_klo_val = db.Column(db.String(), default='-')
    ds_2_band_act_klo_val = db.Column(db.String(), default='-')
    ds_3_band_act_klo_val = db.Column(db.String(), default='-')
    ds_4_band_act_klo_val = db.Column(db.String(), default='-')
    receive_signal_threshhold_ds = db.Column(db.Integer(), default=-30)
    receive_signal_threshhold_us = db.Column(db.Integer(), default=-15)
    total_output_power_ds = db.Column(db.FLOAT(), default=10.8)
    total_output_power_us = db.Column(db.FLOAT(), default=-7.5)
    current_vdsl_2_profile = db.Column(db.String(), default='Profile17a')
    coding_gain_ds = db.Column(db.String(), default='-')
    coding_gain_us = db.Column(db.String(), default='-')
    power_cut_back_ds = db.Column(db.String(), default='-')
    signal_attenuation_ds_2 = db.Column(db.FLOAT(), default=7.1)
    line_attenuation_ds_2 = db.Column(db.FLOAT(), default=7.1)
    line_snr_margin_ds_2 = db.Column(db.FLOAT(), default=32.6)
    signal_attenuation_us_2 = db.Column(db.FLOAT(), default=7.3)
    line_attenuation_us_2 = db.Column(db.FLOAT(), default=79)
    line_snr_margin_us_2 = db.Column(db.FLOAT(), default=37.9)
    signal_attenuation_ds_3 = db.Column(db.FLOAT(), default=11.4)
    line_attenuation_ds_3 = db.Column(db.FLOAT(), default=11.3)
    line_snr_margin_ds_3 = db.Column(db.FLOAT(), default=34.0)
    actual_limit_psd_mask = db.Column(db.String(), default='AnnexB998ADE17-M2x-B(B8-12)')
    actual_transmit_rate_adapt_ds = db.Column(db.String(), default='AdaptAtStartup')
    actual_transmit_rate_adapt_us = db.Column(db.String(), default='AdaptAtStartup')
    actual_inp_of_roc_ds = db.Column(db.String(), default='-')
    actual_inp_of_roc_us = db.Column(db.String(), default='-')
    actual_snr_margin_of_roc_ds = db.Column(db.String(), default='-')
    actual_snr_margin_of_roc_us = db.Column(db.String(), default='-')
    trellis_mode_ds = db.Column(db.Enum('Enable', 'Disable'), default='Enable')
    trellis_mode_us = db.Column(db.Enum('Enable', 'Disable'), default='Enable')
    last_down_cause = db.Column(db.String(), default='LOS')
    port_energy_saving_flag = db.Column(db.Enum('Yes', 'No'), default='No')
    xpon_mac_chipset_state = db.Column(db.String(), default='Normal')
    signal_detect = db.Column(db.String(), default='Normal')
    available_bandwidth = db.Column(db.Integer(), default=1202323)
    illegal_rogue_ont = db.Column(db.String(), default='Inexistent')
    optical_module_status = db.Column(db.Enum('Online', 'Offline'), default='Online')
    laser_state = db.Column(db.String(), default='Normal')
    tx_fault_h = db.Column(db.String(), default='Normal')
    temperature_h = db.Column(db.FLOAT(), default=61)
    temperature_h_exact = db.Column(db.FLOAT(), default=61.505050)
    tx_bias_current_h = db.Column(db.FLOAT(), default=28)
    tx_bias_current_h_exact = db.Column(db.FLOAT(), default=28.000023)
    supply_voltage_h = db.Column(db.FLOAT(), default=3.20)
    supply_voltage_h_exact = db.Column(db.FLOAT(), default=3.200002)
    tx_power_h = db.Column(db.FLOAT(), default=3.67)
    tx_power_h_exact = db.Column(db.FLOAT(), default=3.670001)
    rx_power_h = db.Column(db.FLOAT(), default=-12.6)
    rx_power_h_exact = db.Column(db.FLOAT(), default=-12.680000)
    vendor_name = db.Column(db.String(), default='Hisense')
    vendor_rev = db.Column(db.FLOAT(), default=1.0)
    vendor_oui = db.Column(db.String(), default='Unspecified')
    vendor_pn = db.Column(db.String(), default='LTE3680M-BC+')
    vendor_sn = db.Column(db.String(), default='M5071013838')
    date_code = db.Column(db.String(), default='17-01-12')
    vendor_specific = db.Column(db.String(), default='00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00')
    module_type = db.Column(db.String(), default='GPON')
    module_sub_type = db.Column(db.String(), default='CLASS B+')
    used_type = db.Column(db.String(), default='OLT')
    encapsulation_time = db.Column(db.String(), default='SFP')
    sff_8472_compliance = db.Column(db.String(), default='Includes functionality described in Rev 9.5')
    min_distance = db.Column(db.Integer(), default=0)
    max_distance = db.Column(db.Integer(), default=30)
    max_rate = db.Column(db.Integer(), default=2500000)
    rate_identifier = db.Column(db.String(), default='Unspecified(0x0)')
    wave_length = db.Column(db.Integer(), default=1490)
    fiber_type_h = db.Column(db.String(), default='Single Mode')
    identifier = db.Column(db.String(), default='SFP or SFP Plus')
    ext_identifier = db.Column(db.String(), default='GBIC/SFP function is defined by two-wire interface ID only')
    connector = db.Column(db.String(), default='SC')
    encoding = db.Column(db.String(), default='NRZ')
    length_9_um = db.Column(db.String(), default='40.0')
    length_50_um = db.Column(db.String(), default='-')
    length_62_5_um = db.Column(db.String(), default='-')
    length_copper = db.Column(db.String(), default='-')
    length_50_um_om_3 = db.Column(db.String(), default='-')
    br_max = db.Column(db.String(), default='Unspecified')
    br_min = db.Column(db.String(), default='Unspecified')
    cc_base = db.Column(db.String(), default='0x4d(Correct)')
    cc_exit = db.Column(db.String(), default='0xb3(Correct)')
    rx_power_warning_threshold = db.Column(db.String(), default='[-29.2,-8.0]')
    rx_power_alarm_threshold = db.Column(db.String(), default='[-30.0,-7.0]')
    tx_power_warning_threshold = db.Column(db.String(), default='[1.0,5.0]')
    tx_power_alarm_threshold = db.Column(db.String(), default='[0.6,5.6]')
    tx_bias_warning_threshold = db.Column(db.String(), default='[0.000,70.000]')
    tx_bias_alarm_threshold = db.Column(db.String(), default='[0.000,90.000]')
    supply_voltage_warning_threshold = db.Column(db.String(), default='[3.100,3.500]')
    supply_voltage_alarm_threshold = db.Column(db.String(), default='[3.000,3.600]')
    temperature_warning_threshold = db.Column(db.String(), default='[-8,75]')
    temperature_alarm_threshold = db.Column(db.String(), default='[-13,80]')
    optic_status = db.Column(db.Enum('normal', 'absence'), default='normal')
    native_vlan = db.Column(db.String(), default='-')
    mdi = db.Column(db.String(), default='-')
    speed_h = db.Column(db.Enum('100', '1000', '10000', '100000', 'auto_1000'), default='1000')
    duplex = db.Column(db.Enum('full', 'auto_full', 'auto'), default='full')
    flow_ctrl = db.Column(db.Enum('on', 'off'), default='off')
    active_state = db.Column(db.Enum('active', 'deactive'), default='deactive')
    link = db.Column(db.Enum('offline', 'online', 'failed'), default='offline')
    detecting_time = db.Column(db.String(), default='-')
    tx_state = db.Column(db.Enum('off', 'on'), default='off')
    resume_detect = db.Column(db.String(), default='-')
    detect_interval = db.Column(db.String(), default='-')
    resume_duration = db.Column(db.String(), default='-')
    auto_sensing = db.Column(db.Enum('enable', 'disable'), default='disable')
    alm_prof_15_min = db.Column(db.String(), default='-')
    warn_prof_15_min = db.Column(db.String(), default='-')
    alm_prof_24_hour = db.Column(db.String(), default='-')
    warn_prof_24_hour = db.Column(db.String(), default='-')
    combo_status = db.Column(db.Enum('-', 'optic', 'electric'), default='optic')
    vlan_id = db.Column(db.Integer())
    vectoring_group = db.Column(db.Integer(), default=None)
