def anagram(s,t):
    s=s.lower()
    t=t.lower()
    l1=[]
    l2=[]
    for i in s:
        if(i!=' '):
            l1.append(i)
    for i in t:
        if(i!=' '):
            l2.append(i)
    l1.sort()
    l2.sort()	
    if(l1==l2):
        print(True)
    else:
        print(False)

anagram("anagram","nagaram")
anagram("rat","car")
anagram("Keep","Peek")
anagram("Mother In Law","Hitler Woman")
anagram("School Master","The Classroom")
anagram("ASTRONOMERS","NO MORE STARS")
anagram("Toss","Shot")
anagram("Debit Card","Bad Credit")
anagram("SiLeNt CAT","LisTen AcT")
anagram("Dormitory","Dirty Room")
