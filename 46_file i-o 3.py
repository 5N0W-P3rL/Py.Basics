# making tables in different files:

for i in range (2,6):
    with open (f"txt files/multiplication of {i}", "w") as f:
        for j in range (1,11):
            print(f"{i} X {j} = {i*j}\n")