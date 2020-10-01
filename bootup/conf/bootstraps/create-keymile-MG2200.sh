#!/bin/bash
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
#
# Example NESi REST API server bootstrapping
#
ENDPOINT=http://localhost:5000/nesi/v1

path="`dirname \"$0\"`"

. $path/functions.sh

# Create a network device (admin operation)
req='{
  "vendor": "KeyMile",
  "model": "MG2200",
  "version": "1",
  "description": "Example Switch",
  "hostname": "KeyMileMG2200",
  "mgmt_address": "10.0.0.12",
  "software_version": "MG2200V800R016C00",
  "network_protocol": "telnet",
  "network_address": "127.0.0.1",
  "network_port": 9023,
  "uuid": "2200"
}'

box_id=$(create_resource "$req" $ENDPOINT/boxen) || exit 1

# Admin credentials
req='{
  "username": "admin",
  "password": "secret"
}'

root_credential_id=$(create_resource "$req" $ENDPOINT/boxen/$box_id/credentials)

### Subrack 0 ###

# Create a physical subrack at the network device (admin operation)
req='{
  "name": "",
  "description": "Pseudo Subrack"
}'

subrack_id=$(create_resource "$req" $ENDPOINT/boxen/$box_id/subracks)

### Unit-1 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "xdsl"
}'

unit_1=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)

### Port-1 ###

# Create a physical port at the network device (admin operation)
req='{
  "card_id": '$unit_1',
  "admin_state": "1",
  "operational_state": "1"
}'

port_1_1=$(create_resource "$req" $ENDPOINT/boxen/$box_id/ports)

### Chan-1 ###

# Create a logical channel at the network device (admin operation)
req='{
  "port_id": '$port_1_1',
  "description": "Channel #1"
}'

chan_1_1_1=$(create_resource "$req" $ENDPOINT/boxen/$box_id/channels)

### Interface-1 ###

# Create a physical port at the network device (admin operation)
req='{
  "chan_id": '$chan_1_1_1'
}'

interface_1_1_1_1=$(create_resource "$req" $ENDPOINT/boxen/$box_id/interfaces)

### Unit-2 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "xdsl"
}'

unit_2=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)

### Port-1 ###

# Create a physical port at the network device (admin operation)
req='{
  "card_id": '$unit_2',
  "admin_state": "1",
  "operational_state": "1"
}'

port_2_1=$(create_resource "$req" $ENDPOINT/boxen/$box_id/ports)

### Port-2 ###

# Create a physical port at the network device (admin operation)
req='{
  "card_id": '$unit_2',
  "admin_state": "1",
  "operational_state": "1"
}'

port_2_2=$(create_resource "$req" $ENDPOINT/boxen/$box_id/ports)

### Unit-3 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "xdsl"
}'

unit_3=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)

### Port-1 ###

# Create a physical port at the network device (admin operation)
req='{
  "card_id": '$unit_3',
  "admin_state": "1",
  "operational_state": "1"
}'

port_3_1=$(create_resource "$req" $ENDPOINT/boxen/$box_id/ports)

### Interface-1 ###

# Create a physical port at the network device (admin operation)
req='{
  "port_id": '$port_3_1'
}'

interface_3_1_1=$(create_resource "$req" $ENDPOINT/boxen/$box_id/interfaces)

### Unit-4 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "xdsl"
}'

unit_4=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)

### Unit-5 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "vdsl"
}'

unit_5=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)

### Unit-6 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "vdsl"
}'

unit_6=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)

### Unit-7 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "vdsl"
}'

unit_7=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)

### Unit-8 ###

# Create a physical card at the network device (admin operation)
req='{
  "subrack_id": '$subrack_id',
  "product": "vdsl"
}'

unit_8=$(create_resource "$req" $ENDPOINT/boxen/$box_id/cards)