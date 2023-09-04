augroup xilinx
  autocmd!
  " - vitis:
  "   - platform/platform.spr
  "   - app_system/app_system.sprj
  "   - app/app.prj
  " - vivado:
  "   - project.xpr
  "   - project.hw/project.lpr
  "   - project.gen/sources_1/bd/design_1/design_1.bda
  "   - project.gen/sources_1/bd/design_1/design_1_ooc.xdc
  "   - project.gen/sources_1/bd/design_1/design_1.bxml
  "   - project.gen/sources_1/bd/design_1/sim/design_1.protoinst
  "   - project.srcs/sources_1/bd/design_1/ip/design_1_zynq_ultra_ps_e_0_0/design_1_zynq_ultra_ps_e_0_0.xci
  " - petalinx
  "   - components/yocto/layers/meta-xilinx/meta-xilinx-core/recipes-bsp/u-boot/u-boot-xlnx-scr/boot.cmd.generic.root
  autocmd BufNewFile,BufRead *.tcl call xilinx#shebang()
  autocmd BufNewFile,BufRead *.xdc setfiletype xdc
  autocmd BufNewFile,BufRead *.{xci,protoinst,bda,spr} setfiletype json
  autocmd BufNewFile,BufRead *.{{x,l}pr,bxml,{s,}prj} setfiletype xml
  autocmd BufNewFile,BufRead boot.cmd.* setfiletype sh
augroup END
