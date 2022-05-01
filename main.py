import os

def pid2ecd(pid : str):
    hashtab = {
        # dst_block, digit_stride, char_stride
        0 : (2, 7, 23),
        1 : (0, 1, 1),
        2 : (3, 2, 2),
        3 : (1, 1, 17),
    }
 
    ecdata = ['' for _ in range(len(hashtab))]
    for i, p in enumerate(pid.split('-')):
        for c in p:
            sum = ord(c) + hashtab[i][1 if c.isdigit() else 2]
            if sum > (57 if c.isdigit() else 90):
                sum -= 10 if c.isdigit() else 26
            ecdata[hashtab[i][0]] += (chr(sum))
    return ''.join(ecdata)
 
def ecd2pid(ecd : str):
    hashtab = {
        # dst_block, digit_stride, char_stride
        0 : (1, 1, 1),
        1 : (3, 1, 17),
        2 : (0, 7, 23),
        3 : (2, 2, 2),
    }
 
    pidkey = ['' for _ in range(len(hashtab))]
    for i, c in enumerate(ecd):
        block_num = i // 5
 
        sub = ord(c) - hashtab[block_num][1 if c.isdigit() else 2]
        if sub < (48 if c.isdigit() else 65):
            sub += 10 if c.isdigit() else 26
        pidkey[hashtab[block_num][0]] += (chr(sub))
    return '-'.join(pidkey)

if __name__ == '__main__':
    input_key = input('Type your PID or ECDATA Key: ')
    if '-' in input_key:
        print('Converted key is :', pid2ecd(input_key))
    else:
        print('Converted key is :', ecd2pid(input_key))
    
    os.system("pause")