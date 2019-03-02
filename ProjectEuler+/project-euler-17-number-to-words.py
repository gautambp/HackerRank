# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-17-number-to-words/problem

no2word = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
    '10': 'Ten',
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen',
    '20': 'Twenty',
    '30': 'Thirty',
    '40': 'Forty',
    '50': 'Fifty',
    '60': 'Sixty',
    '70': 'Seventy',
    '80': 'Eighty',
    '90': 'Ninety'
}

def getHundredStr(n):
    result = ''
    if len(n) > 2:
        p = n[-3:-2]
        if int(p) > 0:
            result = no2word[p] + ' Hundred'
    p = int(n[-2:])
    if p >= 10 and p < 20:
        result += ' ' + no2word[str(p)]
    else:
        t = 10*int(p/10)
        if t >= 20:
            result += ' ' + no2word[str(t)]
        u = p - t
        if u > 0:
            result += ' ' + no2word[str(u)]
    return result.strip()
    
def getThousandStr(n):
    if len(n) > 3:
        t = n[-6:-3]
        h = n[-3:]
        if int(t) > 0:
            return getHundredStr(t) + ' Thousand ' + getHundredStr(h)
        else:
            return getHundredStr(h)
    else:
        h = n[-3:]
        return getHundredStr(h)

def getMillionStr(n):
    if len(n) > 6:
        m = n[-9:-6]
        t = n[-6:]
        if int(m) > 0:
            return getHundredStr(m) + ' Million ' + getThousandStr(t)
        else:
            return getThousandStr(t)
    else:
        t = n[-6:]
        return getThousandStr(t)

def getBillionStr(n):
    if len(n) > 9:
        m = n[-12:-9]
        t = n[-9:]
        if int(m) > 0:
            return getHundredStr(m) + ' Billion ' + getMillionStr(t)
        else:
            return getMillionStr(t)
    else:
        t = n[-9:]
        return getMillionStr(t)

def getTrillionStr(n):
    if len(n) > 12:
        m = n[-15:-12]
        t = n[-12:]
        if int(m) > 0:
            return getHundredStr(m) + ' Trillion ' + getBillionStr(t)
        else:
            return getBillionStr(t)
    else:
        t = n[-12:]
        return getBillionStr(t)
    
q = int(input().strip())
for _ in range(q):
    n = input().strip()
    if int(n) == 0:
        print('Zero')
    else:
        print(getTrillionStr(n).strip())
