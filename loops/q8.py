while True:
    is_prime = True
    input_number = int(input("Enter any Prime number: "))
    if input_number > 1:
        for i in range(2, input_number):
            if(input_number % i == 0):
                print(f"It is a non-prime number:{input_number}")
                print("Please re-enter input")
                is_prime = False
                break
    if is_prime == True:
        print(f"You got it!! {input_number} is Prime number")
        break