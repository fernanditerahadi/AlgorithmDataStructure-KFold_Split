print('''\n       ***K-FOLD TESTING-TRAINING SET GENERATOR***\n''')

def solution(indices,k):
    length = len(indices)
    dp = int(length)//int(k) #length of data points
    kfold, l, m, n = [], k*[dp], 1, k
    length = len(indices)

    while sum(l) != length:
        l[-m] += 1
        m += 1

    if length % int(k) == 0:
        for i in range(0, length, dp):
            test = indices[i:i+dp]
            if i < 1 : train = indices[i+dp:]
            if i > 0 : train = indices[0:i] + indices[i+dp:]
            kfold.append([test, train])
    else:
        for a in l:
            for i in range(k-n, k-n+1, a):
                test = indices[i:i+a]
                if i < 1 : train = indices[i+a:]
                if i > 0 : train = indices[0:i] + indices[i+a:]
                kfold.append([test, train])
                n -= a

    return kfold

if __name__ == "__main__":
    numbers = input('INSERT NUMBERs, e.g., 1 2 3 : ')
    z, x, y = 0, 0, 1
    while z < 1:
        try: indices = list(map(int, numbers.split())) ; z += 1
        except: print('Please enter only numeric number(s)\n') ; continue
    while x < 1:
        try:
            k = int(input('INSERT NUMBER OF FOLDs, e.g., 2 : '))
            if k < 2: print('Please enter a numeric number equal or greater than 2\n') ; continue
            if k > len(indices): print('Number of folds cannot be greater than', len(indices),'\n') ; continue
            x += 1
        except: print('Please enter a numeric number ') ; continue

    print('\n[FOLD] * [TESTING SET] * [TRAINING SET]')
    for a, b in solution(indices,k): print(y,'*',a,'*', b) ; y += 1

    input()

#Vinsensius Fernandi, February 2018
