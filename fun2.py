
####c1='~'
####c2='!'
####    
def draw_1d(n, char):
    print(char*n)
####draw_1d(12,c1)
####draw_1d(6,c2)
####draw_1d(24,'+')
##
##
####n=5
####m=12
####char=('*')
##def draw_2d(n,m,char1):
##    for num in range(n):
##        draw_1d(m, char1)
##draw_2d(3,23,'*')
##draw_2d(7,3,'x')

#part1 bonus
##def add_numbers(start, end, skip):
##    c=0
##    for number in range(start,end+1,skip):
##        print(number)
##        c=c+number
##    return c
##add_numbers(0,100,2)

#part2 bonus
n=(5)
m=(12)
border=('@')
fill=('x')
def special_draw_2d(n,m,border,fill):
    for numbers in range(n):
        print(numbers)
