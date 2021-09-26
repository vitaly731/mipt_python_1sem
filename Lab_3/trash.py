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
    for line in A:
        if line == 'penup':
            t.penup()
            A.pop(0)
        elif line == 'pendown':
            t.pendown()
            A.pop(0)
        elif line == 'forward':
            A.pop(0)
            t.forward(size * float(A[0]))
            A.pop(0)
        elif line == 'left':
            A.pop(0)
            t.left(float(A[0]))
            A.pop(0)
        else:
            A.pop(0)

draw1()
    


