# http://www.pythonchallenge.com/pc/def/map.html

input_str = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'



def my_make_trans(input_str):
    alphabet = [chr(ascii_num) for ascii_num in range(ord('a'), ord('z') + 1)]
    alphabet = ''.join(alphabet)

    output_str = []
    for input_char in input_str:
        a_index = alphabet.find(input_char)
        if a_index < 0:
            output_str.append(input_char)
        else:
            output_str.append(alphabet[(a_index + 2) % len(alphabet)])
    
    return ''.join(output_str)



print my_make_trans(input_str)
print my_make_trans('map') 
    

