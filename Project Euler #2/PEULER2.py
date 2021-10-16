'''
  hackerrank
  problem name : project euler #2 : Even Fibonacci Numbers
  problem code : PEULER2
  date : 30.11.2020
  complete : n
'''
def palindrome() :
  xold = 1
  x = 2
  xn = x + xold
  sum = 2
  while xn <= n :
#    print(xn, ",\t")
    if xn % 2 == 0 :
      sum += xn
    xold = x
    x = xn
    xn = xold + xn
  return sum

#driver function
t = int(input())

while t > 0 :
  n = int(input())
  sum = palindrome()
  print(sum)
  t -= 1
