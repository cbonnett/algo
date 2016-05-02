def sum_rec(list_to_sum):
    if len(list_to_sum) == 1:
        return list_to_sum[0]
    else:
        return list_to_sum[0] + sum_rec(list_to_sum[1:])
        
        
def get_base_string(number, base):
    convertString = "0123456789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        return get_base_string(number//base, base) + convertString[number%base]
        
        
def get_fib(number):
    # 1,1,2,3,5,8,13,21
    fib = [1,1]
    if number == 1:
        return fib[0]
    elif number == 2:
        return fib[0] + fib[1]
    else:
        return get_fib(number -1) + get_fib(number -2)      
        
        
