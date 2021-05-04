weight = int(input("Enter your weight "))
inputs = input("(L)bs or (K) gm ")
if inputs.upper() == "L":
    converted = weight * 0.45
    print(converted, "kgs")
elif inputs.upper() == "K":
    converted = weight/0.45
    print(converted, "lbs")

else:
    print("ok")
