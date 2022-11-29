import re 

f = open("/data/data.txt", 'r') 
line = f.read()

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", line))


f.close()