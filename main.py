for x in '0123456789ABCDEFG':
    if (int('10' + str(x) + '0', 17) + int('f0' + str(x) + 'ff', 17)) % 13 == 0:
        print((int('10' + str(x) + '0', 17) + int('F0' + str(x) + 'FF', 17)) // 13)
