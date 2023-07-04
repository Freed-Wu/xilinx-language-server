#!/usr/bin/env -S vivado -mode batch -source
set name vivado
cd [file dirname [file dirname [file normalize [info script]]]]
load_features ipintegrator ipservices labtools simulator xhub
source scripts/xilinx.tcl
