def isPrimeNumber(number):
    if isinstance(number, int) and number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number.")
                break
        else:
            print(number, "is a prime number")
    else:
        print("Please enter a valid integer greater than 1.")

number = 100
isPrimeNumber(number)
