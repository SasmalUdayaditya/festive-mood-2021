'''
  hackerrank
  problem name : project euler #1 : Multiples of 3 and 5
  problem code : PEULER1
  date : 29.11.2020
  complete : y

  let N = 30
  Multiple of 3 : 3, 6, 9, 12, 15, 18, 21, 24, 27
  Multiple of 5 : 5, 10, 15, 20, 25

  common : 15(multiple of 15)

  sum = 195
'''
def findSum() :
  sum = 0

  m3 = (N-1) // 3
  m5 = (N-1) // 5
  m15 = (N-1) // 15
  
  sum = (m3 * (3 + (m3 * 3))) // 2
  sum += (m5 * (5 + (m5 * 5))) // 2

  common = (m15 * (15 + (m15 * 15))) // 2

  sum -= common
  return sum

#driver functions
t = int(input())

while t > 0 :
  N = int(input())
  if N >= 1 :

    sum = findSum()
    print(sum)
  t -= 1
