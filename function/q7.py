def useOfKwarg(**kwarg):
    print("",kwarg)  #prints all taken parameter 
    print(type(kwarg)) #prints type of stored data 
    for key, value in kwarg.items():
        print(f"{key}: {value} ")

useOfKwarg(name = "rehan", age = 12)
print(type(useOfKwarg))