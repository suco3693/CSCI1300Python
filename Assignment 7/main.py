"""
Put required comments here

You will be completing the selection portion of the main function and
there are comments indicating what needs to be completed.
"""

from cipher import *

def open_file(filename, mode):
	"""
	Opens a file based on specified mode and returns the file handle
	There is some exception handling to try to keep the program from crashing
	  from file issues
	
	Params - the name of the file and the mode used for opening it
	Return - a file handle for the opened file or None if file could not be opened
	"""
	
	try:
		if(mode == 'w'):
			file = open(filename, mode)
		elif(mode == 'r'):
			file = open(filename, mode)
		
	except FileNotFoundError:
		print("The file could not be found!")
		return
	except IOError:
		print("An Input/Output error has occurred!")
		print("Aborting program!")
		return
	except:
		print("An unknown error has occurred, sorry!")
		return
	else:	
		return file
	
def ask_for_filenames():
	"""
	Prompts user to enter a filename of a file to encode or decode and
	 also prompts user to enter a filename to store results of encoding / decoding
	
	Params - none
	Return - two filenames that the user enters, first the file
	 to read and second the file to write
	"""
	
	print("Enter the filename for encoding/decoding: ")
	reading = input()
	print("\nEnter the filename to write results: ")
	writing = input()
	
	return reading, writing

def get_menu_selection():
	"""
	Prints a menu of choices for the user and asks user to enter their choice
	
	Params - none
	Return - a string containing what the user entered
	"""
	
	print("Welcome to the Amazing Cipher Program!")
	print("1 - Caesar Cipher Encode")
	print("2 - Caesar Cipher Decode")
	print("3 - Deranged Cipher Encode")
	print("4 - Deranged Cipher Decode")
	print("\nEnter your selection: ")
	
	choice = input()
	
	return choice[0]	# returns only the first character entered
	
def main():
	"""
	Runs the cipher program interface, which allows a user to
	 specify a text file, encode or decode the text file using
	 Caesar or Deranged ciphers, and write the results to a 
	 different text file.
	"""
	
	selection = get_menu_selection()
	
	rfile, wfile = ask_for_filenames()
	
	infile = open_file(rfile, 'r')
	
	if infile != None:
		outfile = open_file(wfile, 'w')
		
		if(selection == '1'):
			'''
			General Algorithm:
			ask user for key value
			get a line from input file
			encode it using the caesar ciper with specified key
			write result to output file
			repeat until all lines in file are processed
			'''
			
			pass
			
		elif(selection == '2'):
			'''
			Algorithm is similar to caesar encryption
			Change is how to handle the key value
			'''
			
			pass
			
		elif(selection == '3'):
			'''
			General Algorithm for deranged cipher is similar to Caesar cipher
			Keyword phrase replaces the key and toEncrypt needs to
			 be specified in function call 
			'''
			
			pass
			
		elif(selection == '4'):
			'''
			Similar to deranged encryption
			The toEncrypt actual parameter value for whether to encrypt
			 needs to be set differently to make this work
			'''
			
			pass
			
		else:
			print("\nSelection {} is not a valid, I quit!\n".format(selection))
	
if __name__ == '__main__':
	main()