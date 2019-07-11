import os
BAKWAN = ('PS1="\033[1;94m#_MCAN -> \t (\033[1;91m\W\033[1;94m) \d \n| \n\033[1;94m|___>"')
file = open("../../../.bashrc","w")
file.write('clear\n')
file.write('cd Mcan/Mcan/lib/src && python3 logo.py\n')
file.write('cd $HOME')
file.close()

file = open("../../../../usr/etc/bash.bashrc","a")
file.write(BAKWAN)
file.close()
