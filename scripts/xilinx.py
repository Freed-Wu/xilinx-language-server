#!/usr/bin/env python
r"""Xilinx
==========

Called by ``scripts/xilinx.vim``.
"""
import sys

from xilinx_language_server.server import get_document

doc = " ".join(get_document()[{"xdc": "vivado", "xsct": "vitis"}[sys.argv[1]]])
print(f"syntax keyword {sys.argv[1] + 'Keyword'} {doc}")
