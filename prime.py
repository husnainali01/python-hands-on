def findPrimeNumber(num):
    isprime = True
    if num == 0 or num == 1:
        print(num, 'is a prime number')
    else:
        if num > 1:
            for i in range(2, int(num / 2)):
                if (num % i) == 0:
                    isprime = False
                    break
                else:
                    isprime = True
        else:
            print('You are enter the negative number ... please ..  Enter the Positive Number:')
    if isprime == True:
        print(num, 'is a prime number')
    else:
        print(num, 'is not prime number')


if __name__ == "__main__":
    num = input("Enter the Number:")
    num = int(num)
    findPrimeNumber(num)
