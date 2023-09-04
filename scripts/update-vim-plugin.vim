#!/usr/bin/env -S nvim --headless -u
# Update syntax/xdc.vim and syntax/xsct.vim
for g:filetype in ['xdc', 'xsct']
  execute 'py sys.argv = ["python", "' . g:filetype . '"]'
  redir => g:xilinx
  pyfile scripts/xilinx.py
  redir END
  execute 'noswapfile edit syntax/' . g:filetype . '.vim'
" vint: -ProhibitCommandRelyOnUser -ProhibitCommandWithUnintendedSideEffect
  %substitute/syntax keyword .*/\=trim(g:xilinx)/
" vint: +ProhibitCommandRelyOnUser +ProhibitCommandWithUnintendedSideEffect
  write
endfor
quit
