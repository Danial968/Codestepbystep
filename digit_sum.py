def helper(number,value):
    digit = number % 10
    if number == 0:
        ok = value
        return ok
    value += digit
    number = number//10
    return helper(number,value)

def digit_sum(number):
    negative = False
    
    if number < 0:
        number = number * -1
        negative = True
        
    value = 0
    result = helper(number,value)
    
    if negative == True:
        result = result * -1

    return result

