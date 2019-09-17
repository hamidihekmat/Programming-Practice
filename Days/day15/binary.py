



def binary(int):
    binary = ''
    while int!=0:
        int = int / 2
        binary += str(int % 2)
    return binary[::-1]


print(binary(255))
