#MyProblem1.py
#Project Euler problem 16 - Power Digit Sum

from NumberTests import calcExponents
from NumberTests import listDigits

def main():
  exp_ans = calcExponents(2,1000)
  #print(exp_ans)

  digits = listDigits(exp_ans)
  #print(digits)

  digits_summed = sum(digits)
  print("The sum of the digits is:", digits_summed)

if __name__ == '__main__':
  main()
