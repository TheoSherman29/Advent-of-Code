input = open('input.txt', 'r').read().strip().split('\n')

sum = 0
for i, data in enumerate(input):
    keys = sorted(data.split(' ')[0:10], key= lambda x: len(x))
    nums = data.split(' ')[11:]
    digits = {'8': {'a', 'b', 'c', 'd', 'e', 'f', 'g'}}
    while (len(digits.keys()) < 10):
        #print('loop')
        for string in keys:
            try:
                # print(string, len(digits.keys()))
                if len(string) == 2:
                    digits['1'] = set(string)
                    #print(digits, 1)
                elif len(string) == 3:
                    digits['7'] = set(string)
                    #print(digits, 7)
                elif len(string) == 4:
                    digits['4'] = set(string)
                    #print(digits, 4)
                elif len(string) == 5:
                    if digits['1'].issubset(set(string)) and digits['7'].issubset(set(string)):
                        digits['3'] = set(string)
                        #print(digits, 3)
                    elif set(string).issubset(digits['6']):
                        digits['5'] = set(string)
                        #print(digits, 5)
                    else:
                        digits['2'] = set(string)
                        #print(digits, 2)
                elif len(string) == 6:
                    if digits['4'].issubset(set(string)) and digits['7'].issubset(set(string)):
                        digits['9'] = set(string)
                        #print(digits, 9)
                    elif digits['7'].issubset(set(string)) and not digits['4'].issubset(set(string)):
                        digits['0'] = set(string)
                    else:
                        digits['6'] = set(string)

            except:
                print('err', string, len(string))
        if string[0] == '|': break
    dec_num = ''
    for num in nums:
        for i in range(10):
            if digits[f'{i}'] == set(num):
                dec_num += (f'{i}')
        print(dec_num)
    sum += int(dec_num)

print(sum)

