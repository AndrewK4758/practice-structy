def print_formatted(number):

    def octal(num):
        return format(num, 'o')
    
    def hexi(num):
        return format(num, 'X')

    def binary(num):
        return format(num, 'b')
    for i in range(1,number+1):
        width = len(binary(number))
        print(str(i).rjust(width), octal(i).rjust(width), hexi(i).rjust(width), binary(i).rjust(width))
        

print_formatted(2)
