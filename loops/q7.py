while True:
    input_number = int(input("Enter number between 1-10: "))
    if(input_number >= 1 and input_number <= 10):
        print(f"Number {input_number} stored successfully!!")
        break
    else:
        print(f"Given number is {input_number}!!")
        print("Please re-enter 😊")
        continue
    
