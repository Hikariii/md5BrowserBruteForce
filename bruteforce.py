# your code goes here
import string
import hashlib
import time
import datetime

#define charset
hashChars = string.ascii_lowercase + string.ascii_uppercase

#hash to be found
hashVal = "f92bfc75d481c196c1e4deecf7fac3af"
counter = 0

start_time = time.clock()

#bruteForce for "a-zA-z" strings
def bruteForce(s=''):
  maxLength = 4
  global counter
  counter += 1
  if len(s) > maxLength:
    return None
  elif hashlib.md5(s.encode('utf-8')).hexdigest() == hashVal:
    return s

  #show progress
  if (counter % 1000 == 0):
    print(s)
  
  for c in hashChars:
    res = bruteForce(s+c)
    if (res is not None):
      return res

print(bruteForce())

print("Elapsed (h.mm.ssssssss):" + str(datetime.timedelta(seconds=(time.clock() - start_time))))