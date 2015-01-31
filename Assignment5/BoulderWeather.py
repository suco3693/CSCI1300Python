fo=open("BoulderWeatherData.csv","r+")
print("Name of this file is: ",fo.name)
for chara in fo:
	line=fo.readline()
	print(line)
	

