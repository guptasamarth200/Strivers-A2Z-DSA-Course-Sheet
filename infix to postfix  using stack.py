def infixToPostfix(expression):
    stack = []
    output = ""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for character in expression:
        if character.isalpha():
            output += character
        elif character == '(':
            stack.append('(')
        elif character == ')':
            while stack and stack[-1]!= '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!= '(' and precedence[character] <= precedence[stack[-1]]:
                output += stack.pop()
            stack.append(character)

    while stack:
        output += stack.pop()

    return output

expression = input('Enter infix expression: ')
print('Infix notation: ', expression)
print('Postfix notation: ', infixToPostfix(expression))