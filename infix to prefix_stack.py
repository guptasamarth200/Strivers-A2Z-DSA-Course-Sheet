def infixToPrefix(expression):
    stack = []
    output = ""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Reverse the input expression
    expression = expression[::-1]

    for character in expression:
        if character.isalpha():
            output += character
        elif character == ')':
            stack.append(')')
        elif character == '(':
            while stack and stack[-1] != ')':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != ')' and precedence[character] < precedence[stack[-1]]:
                output += stack.pop()
            stack.append(character)

    while stack:
        output += stack.pop()

    # Reverse the output string to get the prefix notation
    output = output[::-1]

    return output

expression = input('Enter infix expression: ')
print('Infix n  qqqqqotation: ', expression)
print('Prefix notation: ', infixToPrefix(expression))