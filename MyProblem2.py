#MyProblem2.py
#Project Euler problem 6 - Sum Square Difference

from NumberTests import numSquared
from NumberTests import difference

def main():
  total_nums_squared = 0
  for i in range(101):
        squared = numSquared(i)
        total_nums_squared += squared

  #print(total_nums_squared)

  list_nat_num = list(range(101))
  sum_nat_num = sum(list_nat_num)
  #print(sum_nat_num)
  sum_num_squared = numSquared(sum_nat_num)
  #print(sum_num_squared)

  subtract = difference(sum_num_squared,total_nums_squared)
  print(subtract)


if __name__ == '__main__':
  main()