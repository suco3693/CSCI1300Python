
def create_caesar_codec():
	text=str(['T', 'H', 'E', 'T', 'Y', 'G', 'E', 'R'])
	key=2
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
		text=text.replace(i,cypher[i])
		print(text)
		
create_caesar_codec()
