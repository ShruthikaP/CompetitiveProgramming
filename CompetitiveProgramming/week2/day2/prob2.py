import unittest
def check(ch1,ch2):
       if (ch1 == '(' and  ch2 == ')'):
         return True
       elif (ch1 == '{' and ch2 == '}'):
         return True
       elif (ch1 == '[' and ch2 == ']'):
         return True
       else:
         return False
         
def func(str):
       t=[]
       for i in range(len(str)):
          if (str[i] == '{' or str[i] == '(' or str[i] == '['):
              t.append(str[i])
          if (str[i] == '}' or str[i] == ')' or str[i] == ']'):
              if not t:
                   return False
              elif (check(t.pop(), str[i]) ==False ):
                  return False
       if not t:
           return True
       else:
           return False