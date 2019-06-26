import os
import time 
from tqdm import tqdm
import random
import sys

# Code By Aditya AXM
# Recode ???
# Silahkan... :)

class Data_Log():

	def __init__(self):
		while True:
			os.system('clear')
			os.system('clear')
			print("\033[1;92m")
			print("\033[1;92m")
			print("\033[1;92m ███▄ ▄███▓ ▄████▄   ▄▄▄       ███▄    █ ")
			print("\033[1;92m▓██▒▀█▀ ██▒▒██▀ ▀█  ▒████▄     ██ ▀█   █ ")
			print("\033[1;92m▓██    ▓██░▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒")
			print("\033[1;92m▒██    ▒██ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒")
			print("\033[1;92m▒██▒   ░██▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░")
			print("\033[1;92m░ ▒░   ░  ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ")
			print("\033[1;92m░  ░      ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░")
			print("\033[1;92m░      ░   ░          ░   ▒      ░   ░ ░ ")
			print("\033[1;92m       ░   ░ ░            ░  ░         ░ ")
			print("\033[1;92m           ░                             ")
			print("\033[1;92m")
			print("\033[1;92m        MOSLEM CYBER ARMY NEWS")
			print("\033[1;92m")
			self.username = input('\033[1;92mYour Name : ')
			self.password = input('\033[1;92mPassword  : ')
			self.log = {'Mujahid212'}
			if self.password in self.log:
				print()
				time.sleep(1)
				print('Wait....')
				time.sleep(1)
				print()
				print('Assalamualaikum',self.username)
				time.sleep(1)
				break
			elif self.password not in self.log:
				print()
				time.sleep(1)
				print('Wait....')
				time.sleep(1)
				print()
				print('Assalamualaikum',self.username)
				print()
				time.sleep(3)
				print()
				print('\033[1;91mYour password is incorrect')
				time.sleep(3)

def bakwan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 00.1)

os.system('clear')
AXM = Data_Log()
time.sleep(1)
os.system('clear')
while True:
	os.system('clear')
	print("\033[1;92m")
	print("\033[1;92m")
	print("\033[1;92m ███▄ ▄███▓ ▄████▄   ▄▄▄       ███▄    █ ")
	print("\033[1;92m▓██▒▀█▀ ██▒▒██▀ ▀█  ▒████▄     ██ ▀█   █ ")
	print("\033[1;92m▓██    ▓██░▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒")
	print("\033[1;92m▒██    ▒██ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒")
	print("\033[1;92m▒██▒   ░██▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░")
	print("\033[1;92m░ ▒░   ░  ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ")
	print("\033[1;92m░  ░      ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░")
	print("\033[1;92m░      ░   ░          ░   ▒      ░   ░ ░ ")
	print("\033[1;92m       ░   ░ ░            ░  ░         ░ ")
	print("\033[1;92m           ░                             ")
	print("\033[1;92m")
	print("\033[1;94m                 MENU")
	print("\033[1;92m")
	print("\033[1;92m[1] Open Source Information Facebook (OSIF)")
	print("\033[1;92m[2] Create Virus APK")
	print("\033[1;92m[3] Hammer")
	print("\033[1;92m[4] Spammer Grab")
	print("\033[1;92m[5] Spam SMS KHUSUS nomor TELKOMSEL")
	print("\033[1;92m[6] Spammer Gmail")
	print("\033[1;92m[7] Daftar Gorengan")
	print("\033[1;92m[8] README !!!")
	print("\033[1;92m[9] EXIT")
	print("")

	data = input('input-> ')
	if data is '1':
		os.system('cd lib/OSIF && python2 osif.py')
		break
	elif data is '2':
		os.system('clear')
		os.system('cd lib/Malicious && python2 malicious.py')
		bakwan('\033[1;92mTuliskan nama apk virus yang sudah di download tdi, untuk di pindah kan ke sdcard secara otomatis')
		print('')
		time.sleep(1)
		namaapk = input('Name Apk ? (Contoh -> Elite.apk) : ')
		print('Sedang di pindahkan...')
		os.system('cd lib/Malicious/Android && mv ' + namaapk + ' /sdcard/Bakwan')
		time.sleep(1)
		print('')
		bakwan('Cek di penyimpanan internal, dan cari folder yang bernama Bakwan')
		time.sleep(3)
		pass
	elif data is '3':
		userin = input(str('Ip Target : '))
		data = ('cd lib/src && python3 hammer.py -s ' + userin + ' -p 80 -t 135')
		os.system(data)
		time.sleep(3)
		pass
	elif data is '4':
		os.system('cd lib/src && python grab.py')
		break
	elif data is '5':
		os.system('cd lib/src && python telsel.py')
		break
	elif data is '6':
		os.system('cd lib/SpamMail && php SpamMail.php')
		break
	elif data is '7':
		bakwan('Daftar Gorengan Enak :v')
		time.sleep(0.1)
		bakwan('Bakwan')
		time.sleep(0.1)
		bakwan('Tahu')
		time.sleep(0.1)
		bakwan('Tempe')
		time.sleep(0.1)
		gor = input('Pilih Gorengannya ?')
		time.sleep(0.1)
		bakwan('GORENGAN ' + gor + ' SIAP MELUNCUR.... WKWKWKWKWK :v')
		time.sleep(1)
		os.system('sl')
		pass
	elif data is '8':
		os.system('clear')
		print("\033[1;92m")
		print("\033[1;92m")
		print("\033[1;92m ███▄ ▄███▓ ▄████▄   ▄▄▄       ███▄    █ ")
		print("\033[1;92m▓██▒▀█▀ ██▒▒██▀ ▀█  ▒████▄     ██ ▀█   █ ")
		print("\033[1;92m▓██    ▓██░▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒")
		print("\033[1;92m▒██    ▒██ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒")
		print("\033[1;92m▒██▒   ░██▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░")
		print("\033[1;92m░ ▒░   ░  ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ")
		print("\033[1;92m░  ░      ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░")
		print("\033[1;92m░      ░   ░          ░   ▒      ░   ░ ░ ")
		print("\033[1;92m       ░   ░ ░            ░  ░         ░ ")
		print("\033[1;92m           ░                             ")
		print("\033[1;92m")
		print("\033[1;92m        MOSLEM CYBER ARMY NEWS")
		print("\033[1;92m")
		bakwan('	We Are Moslem Cyber Army News')
		bakwan('')
		bakwan('Ketika kita semua memiliki akses ke informasi, KITA KUAT. Ketika kita kuat, kita tetap memiliki kekuatan untuk melakukan hal yang mustahil')
		bakwan('')
		bakwan('Kita semua bangkit dan berdiri untuk suatu perubahan.')
		bakwan('	')
		bakwan('Kami tidak Berkelompok, tetapi kami Berkeluarga')
		bakwan('Kami melakukan hal hal yang kami lakukan untuk rakyat, bukan untuk kepentingan kita sendiri seperti sebuah ketenaran')
		bakwan('	')
		bakwan('JANJI JANJI DAN KEBOHONGAN MEREKA, TELAH MEMBAWA KITA KEBAWAH. BUKAN KEDEPAN !!!')
		bakwan('	')
		os.system('mpv lib/Asyghil.mp3')
	elif data is '9':
		print('')
		time.sleep(1)
		print("\033[1;91mWassalamualaikum :)")
		time.sleep(1)
		print('Exit...')
		os.system('exit')
		break
	else:
		time.sleep(1)
		print('Inputkan sesuai nomor urut :)')
		time.sleep(2)
	pass