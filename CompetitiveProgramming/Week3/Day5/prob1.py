def BaseConverter(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d
short = 7
short_dic={}
full_dic={}
count=0
b_62=BaseConverter("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
def genShortURL(x):
    if (x in full_dic):
        print("ShortURL already Exists"+full_dic[x])
        return
    global count
    s=""
    k=count
    count+=1
    if (k==0):
        s="0000000"
        if (s not in short_dic):
            short_dic[s]=x
            full_dic[x]=s
            print("short url for "+x+" is https://ca.ke/"+s)
            return
    while(k!=0):
        s=b_62[k%62]+s
        k=k//62
    l=len(s)
    if (l<short):
        for i in range(short-l):
            s="0"+s
    if (s not in short_dic):
        short_dic[s]=x
        full_dic[x]=s
    print("short url for "+x+" is https://ca.ke/"+s)

while (True):
    print("Enter \n\t1) generate ShortURL\n\t2)redirect ShortURL")
    userInput=int(input())
    if (userInput==""):
        x=input("Enter URL to shorten: ")
        genShortURL(x)
    elif (userInput==2):
        shortURL=input("Enter a short url: ")
        if short_dic.get(shortURL,None) is not None:
            print("redirecting to "+short_dic[shortURL])
        else:
            print("Doesn't exist")
    else:
        print("Invalid Input")