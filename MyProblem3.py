#MyProblem3.py
#Project Euler problem 10 - Summation of Primes


from NumberTests import isPrime

def main():
  list_primes = []
  for i in range(2,200000):
        if isPrime(i):
            list_primes.append(i)

  #print(list_primes)

  sum_primes = sum(list_primes)
  print(sum_primes)




    


if __name__ == '__main__':
  main()