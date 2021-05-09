import random
from keyboard import press
from pynput.keyboard import Key, Controller
import time

#Brute force

Keyb = Controller()

clipEmtied = False
password = 0
a = 0
c = ''

# I know I could'ev use \n buut this looks better :)

print("                                              ")
print("                                              ")
print('   @@@@@@@     @@@          @@@     @@@@@@@   ')
print('  !@@          @@!          @@!     @@!  @@@  ')
print('  !@!          !@!          !@!     !@!  @!@  ')
print('  !@!          @!!          !!@     @!@@!@!   ')
print('  !!!          !!!          !!!     !!@!!!    ')
print('  :!!          !!:          !!:     !!:       ')
print('  :!:           :!:         :!:     :!:       ')
print('  ::: :::      :: ::::      ::      ::        ')
print('  :: :: :     : :: : :     :        :         ')
print("                                              ")
print("                                              ")
print('               +-+-+-+-+-+                    ')
print('               |B|r|u|t|e|                    ')
print('               +-+-+-+-+-+                    ')
print('               |F|o|r|c|e|                    ')
print('               +-+-+-+-+-+                    ')
print("                                              ")
print("                                              ")
print("    For all the options type: help            ")
print('                                              ')
ask = input('      What do you want to do? Say it:')

print("                                              ")

speed = input('    How was do you want to emty the clip? (in sec) :')

speed = int(speed)

if ask == 'help':
	print("Ok, so... \n General decimal penetration (using keyboard) is: gp")
	print('Next is... \n Cracking weak passwords with the rockyou.txt list is: lp')

while True:
	def ListForceRockU():
		print('list penetration activated')
		input('Are you ready? (press anything) ')
		time.sleep(0.5)
		print('It will start at 3 seconds...')
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("...")
		with open('rockyou.txt', 'r') as lines:
			for line in lines:
				actual_l = str(line)
				Keyb.type(actual_l + '')
				time.sleep(speed)

	def BruteForceGeneral():
		global password
		global a
		global c
		print('decimal_penetration activated!')
		time.sleep(1.5)
		digits = input('How much digits will this need to guess: ')

		input('Are you ready? (press anything) ')
		print('Will start in 5 seconds')
		digits = int(digits)
		time.sleep(5)

		while True:
			password = int(password)
			password += 1
			password = str(password)

			for i in password:
				a += 1  
			b = digits - a
		    
			if b <= -2:
				break
		  	
			if b != -1:
				for i in range(b):
					c += "0"

				time.sleep(speed)
				Keyb.type(c + password)
				press('enter')
		    
			else:
				time.sleep(speed)
				Keyb.type(password)
				press('enter')
		  

			c = ''
			a = 0
			b = 0

	if clipEmtied == True:
		ask = input("      What else you want to do? Say it: ")


		# activation

	if ask == 'dp':
		BruteForceGeneral()

	if ask == 'lp':
		ListForceRockU()
	
	clipEmtied = True
	print(' ')
	print("      ___clip--empty___")
	print('   ')

