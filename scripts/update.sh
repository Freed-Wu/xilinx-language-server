#!/usr/bin/env bash
cd "$(dirname "$(readlink -f "$0")")/.." || exit 1

scripts/update-vivado-keywords.tcl
scripts/update-xsct-keywords.tcl
scripts/update-vim-plugin.vim
