#!/usr/bin/env python3
# hextodec by EnigmaCj
class hextodec():
	
	def __init__(self, hex = "0x"):
		self.old_hex = hex
		self.hex = list(hex[2:])       
			
	def toDec(self):
		com = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15 }
		steps = [x for x in range(len(self.hex) - 1, -1, -1)]		
		
		if not self.old_hex.startswith('0x') and not self.old_hex.startswith('0X'):
			print ("Hexadecimal numbers need to start with 0x.")    
			exit(1)
			
		for i in range(len(self.hex)):
			if self.hex[i].isdigit():           
				self.hex[i] = int(self.hex[i])			
				continue
			else:
				self.hex[i] = self.hex[i].lower()
		
		for i in range(len(self.hex)):
			if self.hex[i] in com:              
				self.hex[i] = com[self.hex[i]]
			else:
				if str(self.hex[i]) in '0123456789':
					continue
				else:
					print ("Error. %s does not exist in hexadecimal." % self.hex[i].upper())
					exit(2)  
		
		res = 0
		for n, t in zip(self.hex, steps):     
			res += n * (16 ** t)			 
		return res

while True:
	conv = hextodec(input('>>> '))
	print('%s in hexadecimal equals to %d in decimal.' % 
(conv.old_hex, conv.toDec()))
