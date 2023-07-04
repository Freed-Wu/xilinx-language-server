set path src/xilinx_language_server/assets/json
exec mkdir -p $path

package require json

set commands [split [info commands] " "]
foreach command $commands {
  set help ""
  catch {set help [help $command]}
  regsub -all {"} $help ' help
  regsub -all {\\} $help {\\\\} help
  regsub -all "\t" $help {\t} help
  regsub -all "\n" $help {\n} help
  regsub -all "\r" $help {} help
  dict set helps $command [json::string2json $help]
}
set data [json::dict2json $helps]
regsub ",\n}" $data "\n}" data
set fp [open $path/$name.json w]
puts $fp $data
close $fp
