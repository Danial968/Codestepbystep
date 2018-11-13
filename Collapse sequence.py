def helper(word,letter,final,number):
    if number == len(word):
        return final
    
    if word[number] != letter or word[number] != word[number - 1]:
        final += word[number]
    number += 1
    
    result = helper(word,letter,final,number)
    return result
    

def collapse_sequences(word,letter):
    final = ''
    number = 0
    if len(word) == 0:
        return final
    final += word[0]
    number += 1
    result = helper(word,letter,final,number)
    return result

print(collapse_sequences("", 't'))