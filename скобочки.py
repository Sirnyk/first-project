def check_string_brackets(input_string):
    flag = True
    open = 0
    close = 0
    for i in range(len(input_string)):
        if input_string[i] == '(':
            open +=1
        else:
            close += 1
        if open < close:
            flag = False
    if open == close and flag == True:
        print('yes')
    else:
        print('no')

check_string_brackets('))((')