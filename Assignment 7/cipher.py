"""
Assignment: Assignment 7

Sutton Cowperthwaite
Maryjane Clark

Description: Cipher Function
Date: 10/10/13

"""

# this imports several strings of characters that are useful
#	for solving these problems
# print them out to see what they contain
from string import ascii_uppercase as letters
from string import punctuation as symbols
from string import digits
from string import whitespace

def caesar_cipher(text, key):
	"""
	Encrypts or Decrypts text using a Caesar cipher with the
	 supplied key value
	Params - text to modify and the key value
	Return - the text modifed by the Caesar cipher
	"""
	code=[]
	woof=[]
	newtext=text.upper()
	linelen=len(newtext)
	for j in range(linelen):
		if ord(newtext[j])<65:
			nope=newtext[j]
		elif ord(newtext[j])>90:
			nope=newtext[j]
		else:	
			code.append(newtext[j])
	w=len(code)
	code1=[]
	for i in range(w):
		if ord(code[i])==code[0:w]:
			nope=code[i]
		else:
			code1.append(code[i])				
	code=str(code1)
	r=len(code1)
	cypher={}
	alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for i in range(26):
		chrn=ord(alpha[i])+key
		if chrn>90:
			chrn=chrn%100
			chrn=64+(chrn-90)
		elif chrn<65:
			chrn=(chrn-64)+90
		cypher[alpha[i]]=chr(chrn)	
			
	for i in cypher:
		code=code.replace(i,cypher[i])
	return code
	
	
	
		
def deranged_cipher(text, keyword, toEncrypt):
	"""
	Encrypts or Decrypts text using a deranged alphabet cipher with the
	 supplied secret keyword/phrase.
	Params - text to modify, the keyword cipher text, and whether to encrypt
	Return - the text modifed by the deranged cipher
	"""
	code=[]
	woof=[]
	newtext=text.upper()
	linelen=len(newtext)
	for j in range(linelen):
		if ord(newtext[j])<65:
			nope=newtext[j]
		elif ord(newtext[j])>90:
			nope=newtext[j]
		else:	
			code.append(newtext[j])	
	w=len(code)
	code1=[]
	for i in range(w):
		if ord(code[i])==code[0:w]:
			nope=code[i]
		else:
			code1.append(code[i])			
	code=str(code1)
	r=len(code1)
	cypher={}
	alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for i in range(26):
		chrn=ord(alpha[i])+key
		if chrn>90:
			chrn=chrn%100
			chrn=64+(chrn-90)
		elif chrn<65:
			chrn=(chrn-64)+90
		cypher[alpha[i]]=chr(chrn)	
			
	for i in cypher:
		code=code.replace(i,cypher[i])
	return code


def print_cipher_codec(code):
	"""
	This prints out the contents in the dictionary. It isn't 
	 actually specific to just printing a codec and could
	 print out any dictionary supplied.
	
	Params - The dictionary cipher codec
	Return - None
	"""
	
	print("\nCipher Codec Contents:")
	
	for c in letters:
		print("key = {} has value = {}".format(c, code[c]))
	
	print()
	
def main():
	# you can use the main function for testing and trying out
	#  various things that were left here
	
	
	
	secret = "..jazz jackrabbit	/?ghijklmnopqrstuvwxyz324"
	msg2 = "The quick brown fox"
	emsg = deranged_cipher(msg2, secret, True)
	print(emsg)
	dmsg = deranged_cipher(emsg, secret, False)
	print(dmsg)
	
	# when the codec creation is working, you can uncomment this
	#  to see the deranged codec values
	#myCodec = create_deranged_codec(secret, True)
	#print_cipher_codec(myCodec)
	
	
	
	ws_tests = ["\t\t   ab c  d b		a", ".", "\t", ""]
	
	symbol_tests = ["-!!~~oo~~!!-", "#", "a", "bab", "\t", ""]
	
	dup_tests = [".A B A C B A.", ".", "a", "cba", "\ta\tb", ""]
	
	for i in range(len(ws_tests)):
		result = remove_whitespace_chars(ws_tests[i])
		print("WS Test {} result: {}".format(i + 1, result))
	print()
	
	for i in range(len(symbol_tests)):
		result = remove_symbol_chars(symbol_tests[i])
		print("Sym Test {} result: {}".format(i + 1, result))
	print()
			
	for i in range(len(dup_tests)):
		result = remove_duplicate_chars(dup_tests[i])
		print("Dup Test {} result: {}".format(i + 1, result))
	print()
	
	codec = create_caesar_codec(2)
	print(codec)
	
	values = codec.values()
	
	for c in letters:
		print("codec[{}] = {}".format(c, codec[c]))
		
	print(len(codec))
	
	rcodec = create_caesar_codec(-2)
	
	for c in letters:
		print("rcodec[{}] = {}".format(c, rcodec[c]))
	
	dcodec = create_deranged_codec("happy joy...to the world", True)
	print(dcodec)
	
	for c in letters:
		print("dcodec[{}] = {}".format(c, dcodec[c]))
		
	rdcodec = create_deranged_codec("happy joy...to the world", False)
		
	for c in letters:
		print("rdcodec[{}] = {}".format(c, rdcodec[c]))
	
	
if __name__ == '__main__':
	main()
