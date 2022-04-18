# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-89-roman-numerals/problem
def rtod_converter(roman):
    roman_arr = [c for c in roman]
    for i,el in enumerate(roman_arr):
        if el == 'I':
            roman_arr[i]=1
        elif el == 'V':
            roman_arr[i]=5
        elif el == 'X':
            roman_arr[i]=10
        elif el == 'L':
            roman_arr[i]=50
        elif el == 'C':
            roman_arr[i]=100
        elif el == 'D':
            roman_arr[i]=500
        elif el == 'M':
            roman_arr[i]=1000
        else :
            roman_arr[i]=0
    anchor = max(roman_arr)
    flip = -1
    value = 0
    for i,el in enumerate(roman_arr):
        if el == anchor:
            flip = 1
        value += (flip) * el
    return value

def dtor_converter(num):
    num_arr = [i for i in str(num)]
    num_arr = num_arr[::-1]
    roman_arr = []
    m_arr = num_arr[3:]
    m_count = ''.join(m_arr[::-1])
    m_app = ''
    if m_count:
        m_count = int(m_count)
        m_app = 'M'*m_count
    for i,el in enumerate(num_arr):
        unit = ''
        penta= ''
        deca = ''
        if i == 0:
            unit = 'I'
            penta = 'V'
            deca = 'X'
        elif i == 1:
            unit = 'X'
            penta = 'L'
            deca = 'C'
        elif i == 2:
            unit = 'C'
            penta = 'D'
            deca = 'M'
        if el == '1':
            roman_arr.append(unit)
        elif el == '2':
            roman_arr.append(unit*2)
        elif el == '3':
            roman_arr.append(unit*3)
        elif el == '4':
            roman_arr.append(penta+unit)
        elif el == '5':
            roman_arr.append(penta)
        elif el == '6':
            roman_arr.append(unit+penta)
        elif el == '7':
            roman_arr.append((unit*2)+penta)
        elif el == '8':
            roman_arr.append((unit*3)+penta)
        elif el == '9':
            roman_arr.append(deca+unit)
    roman_arr.append(m_app)
    roman = ''.join(roman_arr)
    return(roman[::-1])

times = int(input())
while times:
    s=str(input())
    value = rtod_converter(s)
    result = dtor_converter(value)
    print(result)
    times -= 1
