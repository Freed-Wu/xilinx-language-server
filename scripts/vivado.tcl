#!/usr/bin/env -S vivado -mode batch -source
set name vivado
cd [file dirname [file dirname [file normalize [info script]]]]
source scripts/xilinx.tcl
