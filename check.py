#!/usr/bin/env python3
import string
import sys

class Checker():
	"""
	This is clas is a simple plagiarism checker for case insensitive matching.
	There is no synonym checking.
	"""
	def __init__(self, input_text, master_text, chck_len=6):
		"""
		Feed two strings of text into this class. The second string
		is the text to check against for plagiarism.
		"""
		self.input_text = input_text
		self.master_text = master_text
		self.chck_len = chck_len
		self.prep()
		self.check_width()

	
	def prep(self):
		#remove punctuation
		self.input_list = self.input_text.translate(string.punctuation)

		#put the input text into a list
		self.input_list = self.input_list.split()

		# make a master list
		self.mlist = self.master_text.translate(string.punctuation)
		self.mlist = self.mlist.split()
	
	def check_width(self):
		# take the chck_len width, make a subset and check in master iterate
		print ("[*] Checking...")
		for i,j in enumerate(self.input_list):
			check_str = self.input_list[i:self.chck_len+i]
			result = any(check_str == self.mlist[k:self.chck_len+k] for k in range(len(self.mlist) -1))
			if result:
				print ("[!] Found plagiarism:", check_str)
			

if __name__ == "__main__":
	# This is meant to be used as an imported class so you must provide files and check_length here 
	# FYI, this is just for author testing.. feel free to use this, but no support...

	quick = Checker(open(sys.argv[1], 'r').read(), open(sys.argv[2], 'r').read(), int(sys.argv[3]))
