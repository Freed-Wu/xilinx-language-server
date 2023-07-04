# Configure

## (Neo)[Vim](https://www.vim.org)

### [coc.nvim](https://github.com/neoclide/coc.nvim)

```json
{
  "languageserver": {
    "xilinx": {
      "command": "xilinx-language-server",
      "filetypes": [
        "xdc",
        "xsct"
      ],
      "initializationOptions": {
        "method": "builtin"
      }
    }
  }
}
```

### [vim-lsp](https://github.com/prabirshrestha/vim-lsp)

```vim
if executable('xilinx-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'xilinx',
          \ 'cmd': {server_info->['xilinx-language-server']},
          \ 'whitelist': ['xdc', 'xsct'],
          \ 'initialization_options': {
          \   'method': 'builtin',
          \ },
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "*.xdc" },
  callback = function()
    vim.lsp.start({
      name = "xilinx",
      cmd = { "xilinx-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

```elisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "xilinx-language-server")))
  :activation-fn (lsp-activate-on "xdc")
  :server-id "xilinx")))
```

## [Sublime](https://www.sublimetext.com)

```json
{
  "clients": {
    "xilinx": {
      "command": [
        "xilinx-language-server"
      ],
      "enabled": true,
      "selector": "source.xilinx"
    }
  }
}
```
