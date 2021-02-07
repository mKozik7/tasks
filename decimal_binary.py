def decimal_to_binary(n_decimal):
    x = n_decimal
    k = []
    while (n_decimal > 0):
        a = int(float(n_decimal % 2))
        k.append(a)
        n_decimal = (n_decimal - a) / 2
    string = ""
    for j in k[::-1]:
        string = string + str(j)
    return print("The binary number for {} is {}".format(x, string))

def binary_to_decimal(n_binary):
    x = n_binary
    result = 0
    for x in range(0, len(n_binary)):
        if n_binary[x] == "1":
            result = result + (2 ** (len(n_binary) - (x + 1)))
        elif n_binary[x] != "0":
            raise ValueError("Undefined symbol")
    print("The decimal number for {} is {}".format(n_binary, result))



while True:
    choose = input("1.Convert from binary to decimal write ----- binary or 1 \n2.Convert from decimal to binary write ----- decimal or 2\n3.exit write ----- exit or 3 ")
    if choose == 'decimal' or choose =='2':
        n_decimal = input("please enter the number in decimal format: ")

        if n_decimal =='':
            print("Invalid input")
            break

        n_decimal=int(n_decimal)
        decimal_to_binary(n_decimal)

    elif choose == 'binary' or choose =='1':
        n_binary = input("please enter the number in binary format(you can only use 0 and 1): ")
        binary_to_decimal(n_binary)
    elif choose == '3' or choose =='exit'  :
        break
    else:
        print("There is no option like this")