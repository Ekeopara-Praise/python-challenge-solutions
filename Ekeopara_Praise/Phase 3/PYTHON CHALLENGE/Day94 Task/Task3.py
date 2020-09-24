'''3. Write a Python program to add two binary numbers.
Input : ('11', '1')
Output : 100 '''

def add_binary_nums(x,y):
        max_len = max(len(x), len(y))

        x = x.zfill(max_len)
        y = y.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len-1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1       

        if carry !=0 : result = '1' + result

        return result.zfill(max_len)
    
print(add_binary_nums('11', '1'))
print(add_binary_nums('10', '10'))
print(add_binary_nums('111', '111'))
print(add_binary_nums('1111111', '1'))

#Reference: w3resource