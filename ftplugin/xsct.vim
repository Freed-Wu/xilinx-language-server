if exists('b:did_ftplugin')
  finish
endif
runtime! ftplugin/tcl.vim
let b:did_ftplugin = 1

let s:save_cpoptions = &cpoptions
set cpoptions&vim

let b:undo_ftplugin = substitute(get(b:, 'undo_ftplugin', 'setlocal'), 'setlocal', '& isk', '')
set iskeyword+=-

let &cpoptions = s:save_cpoptions
unlet s:save_cpoptions
