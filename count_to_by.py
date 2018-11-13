def helper(number,step,result):
    
    result = ''
    if number <= 0 or step == 0:
        return result
    result = ', ' + str(number)
    number -= step
    result = helper(number,step,result) + result
    
    return result
    

def count_to_by(number,step):
    result = ''
    line = helper(number,step,result)
    print(line[1:])

count_to_by(0,1)