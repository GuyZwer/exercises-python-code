N=int(raw_input())

def octal_convert(number):
    return str(oct(number)[1:])

def hexadecimal_convert(number):
    return str(hex(number)[2:])

def binary_convert(number):
    return str(bin(number)[2:])

def string_formatting(num1, num2, num3, num4, N):
    return (num1).rjust(len(bin(N)[2:])) + (num2).rjust(len(bin(N)[1:])) + (num3.upper()).rjust(len(bin(N)[1:])) + (num4).rjust(len(bin(N)[1:]))

for number in range(1, N+1):
    print (string_formatting(str(number), octal_convert(number), hexadecimal_convert(number), binary_convert(number), N))
