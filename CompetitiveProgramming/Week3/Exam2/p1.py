d={}
d["a"]=".-"
d["b"]="-..."
d["c"] ="-.-."
d["d"] ="-.."
d["e"] ="."
d["f"] ="..-."
d["g"]="--."
d["h"] ="...."
d["i"] =".."
d["j"]=".---"
d["k"] ="-.-"
d["l"]=".-.."
d["m"] ="--"	
d["n"]="-."
d["o"] ="---"
d["p"] =".--."
d["q"]="--.-"
d["r"]=".-."
d["s"]="..."
d["t"]="-"
d["u"]="..-"
d["v"]="...-"
d["w"]=".--"
d["x"]="-..-"
d["y"]="-.--"
d["z"]="--.."

s=eval(input())
lis=[]
for i in s:
	str=""
	for j in i:
		str=str+d[j]
	lis.append(str)
dic={}
flag=0
for i in lis:
	if i not in dic:
		dic[i]=1
		flag=flag+1
print(flag)
