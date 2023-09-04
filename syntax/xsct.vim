if exists('b:current_syntax')
  finish
endif
runtime! syntax/tcl.vim
let b:current_syntax = 'xsct'

syntax case match
" generated by scripts/update-vim-plugin.vim
syntax keyword xsctKeyword add_channel after app append apply array auto_execok auto_import auto_load auto_load_index auto_qualify backtrace binary boot bpadd bpdisable bpenable bplist bpremove bpstatus break bsp bt builtin_app builtin_bifgen builtin_boot builtin_bsp builtin_device-tree builtin_domain builtin_driver builtin_isolate builtin_kernel builtin_library builtin_platform builtin_rootfs builtin_scwutil builtin_system builtin_uboot case catch cd chan changebsp checkvalidrmxsa clock close closebsp closehw con concat configapp configbsp configparams connect continue createapp createbsp createdts createhw createlib decode_event_counters delete_channel deleteprojects device device-tree dict dis disconnect dispose_exprs domain dow driver elfverify enable_info_messages encoding eof error eval event_notify exec exit export_to_ds5 expr fblocked fconfigure fcopy file fileevent flush for foreach format fpga gdbremote get_configurable_ip get_context_cache_client get_context_children get_context_data get_context_datatypes get_context_hierarchy get_context_list get_context_pair get_context_properties get_ctx_data get_debug_targets get_debug_targets_cache_client get_design_properties get_jtag_nodes get_jtag_nodes_cache_client get_param_value get_processes get_regs get_slaves get_stacktrace_children getaddrmap getdrivers getlibs getos getperipherals getprocessors getprojects gets getws glob global help history hsi hsiutils huddle if importprojects importsources incr info init_ps interp ishwexpandable isstaticxsa join jtag jtagterminal kernel lappend lassign library lindex linker linsert list llength load loadhw loadipxact locals lrange lrepeat lreplace lreverse lscript lsearch lset lsort mask_poll mask_write mb_drrd mb_drwr mbprofile mbtrace mdm_drrd mdm_drwr memmap mrd mwr namespace notify_newctxs nxt nxti open openbsp openhw osa package pconfig petalinux-boot petalinux-build petalinux-config petalinux-create petalinux-install-path petalinux-package petalinux-util pid pkg_mkIndex platform plm plnx-install-path pmc pread print proc process profile projects puts pwd read readjtaguart redirect_channel regenbsp regexp regsub removelib rename repo return rootfs rrd rst rwr scan sdk sdtgen seek set set_debug_target_id set_jtag_node_id setdriver setlib setosversion setup_hsm_environment setws socket source split stapl state stop stp stpi stpout string subst svf switch sysconfig sysproj system targets tcf tclLog tclPkgSetup tclPkgUnknown tell tfile time toolchain trace u-boot unknown unload unloadhw unset update updatehw updatemss uplevel upvar variable verify version vwait while xsdb xsdbserver yocto

highlight default link xsctKeyword Keyword
" ex: nowrap
