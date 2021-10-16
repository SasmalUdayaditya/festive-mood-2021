'''
  hackerrank
  problem name : project euler #4 : Largest Palindrome Product
  problem code : PEULER4
  date : 04.12.2020
  complete : n
'''
def sqrt(n) :
  return int(n ** (1/2))

def iReverse(n) :
  result = 0
  temp = n
  while temp != 0 :
    modulo = temp % 10
    result = (result * 10) + modulo 
    temp = temp // 10
  return result

def icheckPalindrome(n) :
  flag = 0
  reverse = iReverse(n)
#  print("reverse : ", reverse)
  if n == reverse :
    flag = 1
  return flag

def findLPN(n) :
  global val1; global val2

  while n >= (100 ** 2) :
    #print(n)
    flag = icheckPalindrome(n)
    if flag == 1 :
      #print("largest palindrome number : ", n)
      val1 = 100
      while (val1 < 1000) :
        if n % val1 == 0 :
          val2 = n // val1
          #print("val1 : ", val1, "val2 : ", val2, "mul : ", val1 * val2)
          if val2 < 1000 and val2 > 99:
            return n
        val1 += 1
    n -= 1    

#diver function
t = int(input())

while t > 0 and t <= 100:
  n = int(input())
  if n > 101101 and n < 1000000 :
    n = findLPN(n)
    print(n)
  t -= 1
