# your code goes here
import string
import hashlib

#define charset
hashChars = string.ascii_lowercase + string.ascii_uppercase
hashChars = ['a','b','c'] #for testing

#hash to be found
hashVal = "f92bfc75d481c196c1e4deecf7fac3af"
hashVal = "9df62e693988eb4e1e1444ece0578579" #for testing

#bruteForce for "a-zA-z" strings
def bruteForce(s=''):
  maxLength = 4
  if len(s) >= maxLength:
    return None
  elif hashlib.md5(s).hexdigest() == hashVal:
    return s
  
  for c in hashChars:
    res = bruteForce(s+c)
    if (res is not None):
      return res

print bruteForce()
