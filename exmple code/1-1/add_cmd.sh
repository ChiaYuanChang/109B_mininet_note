#!/bin/bash

echo "table_add phy_forward forward 1 => 2" | simple_switch_CLI --thrift-port 9090  
echo "table_add phy_forward forward 2 => 1" | simple_switch_CLI --thrift-port 9090
simple_switch_CLI --thrift-port 9091 < cmds2.txt

