

t = int(input_data[0])
ket_qua = []    
for i in range(1, t + 1):
    n = int(input_data[i])
    ans_test_case = []
    half_len = (n + 1) // 2
    start = 10**(half_len - 1)
    end = 10**half_len
        
    for num in range(start, end):
        s_half = str(num)
            
        if '4' in s_half:
            continue
            
        if n % 2 == 0:
            s_full = s_half + s_half[::-1]
        else:
            s_full = s_half + s_half[:-1][::-1]
            
        if sum(map(int, s_full)) % 10 == 0:
            ans_test_case.append(s_full)
                
    ket_qua.append(" ".join(ans_test_case))
        
print('\n'.join(ket_qua))