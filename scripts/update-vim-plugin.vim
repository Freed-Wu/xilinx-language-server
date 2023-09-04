#!/usr/bin/env -S nvim --headless -u
" Update syntax/xdc.vim and syntax/xsct.vim
for [g:filetype, g:filename] in items({'xdc': 'vivado', 'xsct': 'xsct'})
  let g:filename = expand('<sfile>:p:h:h')
        \ . '/src/xilinx_language_server/assets/json/'. g:filename . '.json'
  let g:xilinx = join(sort(keys(json_decode(join(readfile(g:filename), '')))), ' ')
  execute 'noswapfile edit syntax/' . g:filetype . '.vim'
" vint: -ProhibitCommandRelyOnUser -ProhibitCommandWithUnintendedSideEffect
  %substitute/syntax keyword .*Keyword \zs.*/\=trim(g:xilinx)/
" vint: +ProhibitCommandRelyOnUser +ProhibitCommandWithUnintendedSideEffect
  write
endfor
quit
