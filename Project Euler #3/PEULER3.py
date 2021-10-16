'''
  hackerrank
  problem name : project euler #2 : Largest Prime Factor
  problem code : PEULER3
  date : 01.12.2020
  complete : n
'''
def sqrt(n) :
  return int(n ** (1/2))

def checkPrime(n) :
  sr = sqrt(n)
  i = 2
  while i <= sr :
    if(n % i == 0) :
      return 0
    i += 1
  return 1

def primeFactor(n) :
  sr = sqrt(n)
  i = 1
  while i <= sr :
    if(n % i == 0) :
      #mxlf : maximum largest factor
      #mnlf : minimum lowest factor

      mxlf = n // i
      flag = checkPrime(mxlf)

      if flag == 1 :
        return mxlf
      else :
        flag = checkPrime(i)
        if flag == 1 :
          mnlf = i
    i += 1  
  return mnlf

#driver function
t = int(input())

while t > 0 and t <= 10 :
  n = int(input())
  if n >= 10 :
    mxlf = primeFactor(n)
    print(mxlf)
  t -= 1
