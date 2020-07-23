def C_to_F(celsius):
    return (celsius*9/5) + 32

for i in range(0, 101, 10):
    print(f'{i} degrees Celsius is {C_to_F(i)} degrees Fahrenheit')