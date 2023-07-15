
dash = '-'
dotLine = '.|.'
word = 'WELCOME'

width, height=list(map(int,input().split()))
j=1
for i in range(height):
    if i < height//2:
        print((dotLine*j).center(width,dash))
        j+=2
    elif i == height//2:
        print(word.center(width,dash))
    elif i > height//2:
        j-=2
        print((dotLine*j).center(width,dash))