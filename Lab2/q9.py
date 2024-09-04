#Convert Decimal number to Binary
def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n < 0:
        return "-" + decimal_to_binary(-n)
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

decimal_number = int(input("Enter any decimal number: "))
binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_representation}")
