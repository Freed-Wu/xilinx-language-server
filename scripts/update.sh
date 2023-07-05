#!/usr/bin/env bash
cd "$(dirname "$(readlink -f "$0")")/.." || exit 1

scripts/xsct.tcl
scripts/vivado.tcl
