import turtle as t

size = 40 # Характерный размер нарисованной цифры

def list_for(digit):
    A = []
    with open('digits_for_index.txt') as txt:
        A = [line.rstrip() for line in txt]
        A = A[A.index('<digit_'+str(digit)+'>') + 1 : A.index('<digit_'+str(digit + 1)+'>')]
    list_for_digit = A
    return list_for_digit

list_for_1 = list_for(1)
list_for_4 = list_for(4)
list_for_7 = list_for(7)
list_for_0 = list_for(0)

def draw1():
    A = list_for_1
    i = 0
    while i <= len(A) - 1:
        if A[i] == 'penup':
            t.penup()
            i += 1
        elif A[i] == 'pendown':
            t.pendown()
            i += 1
        elif A[i] == 'forward':
            i += 1
            t.forward(size * float(A[i]))
            i += 1
        elif A[i] == 'left':
            i += 1
            t.left(float(A[i]))
            i += 1
        else:
            print('Something is wrong with digits_for_index.txt')

def draw4():
    A = list_for_4
    i = 0
    while i <= len(A) - 1:
        if A[i] == 'penup':
            t.penup()
            i += 1
        elif A[i] == 'pendown':
            t.pendown()
            i += 1
        elif A[i] == 'forward':
            i += 1
            t.forward(size * float(A[i]))
            i += 1
        elif A[i] == 'left':
            i += 1
            t.left(float(A[i]))
            i += 1
        else:
            print('Something is wrong with digits_for_index.txt')

def draw7():
    A = list_for_7
    i = 0
    while i <= len(A) - 1:
        if A[i] == 'penup':
            t.penup()
            i += 1
        elif A[i] == 'pendown':
            t.pendown()
            i += 1
        elif A[i] == 'forward':
            i += 1
            t.forward(size * float(A[i]))
            i += 1
        elif A[i] == 'left':
            i += 1
            t.left(float(A[i]))
            i += 1
        else:
            print('Something is wrong with digits_for_index.txt')

def draw0():
    A = list_for_0
    i = 0
    while i <= len(A) - 1:
        if A[i] == 'penup':
            t.penup()
            i += 1
        elif A[i] == 'pendown':
            t.pendown()
            i += 1
        elif A[i] == 'forward':
            i += 1
            t.forward(size * float(A[i]))
            i += 1
        elif A[i] == 'left':
            i += 1
            t.left(float(A[i]))
            i += 1
        else:
            print('Something is wrong with digits_for_index.txt')

draw1()
draw4()
draw7()
draw0()
