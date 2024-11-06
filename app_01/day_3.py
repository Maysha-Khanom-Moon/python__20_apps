# user_prompt = 'Enter a todo: '
todos = []

while True:
    user_action = input("Type add, show(display), or exit: ")
    user_action = user_action.strip()
    
    # 'add' != 'add ' != ' add'
    # strip --> romoves the whitespaces
    # lstrip --> romoves only left whitespaces
    # rstrip --> removes only right whitespaces
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        
        case 'show' | 'display':
            # print(todos)
            for item in todos:
                
                # title --> where the first character in every word is upper case
                item = item.title()
                print(item)            
            
        case 'exit':
            break
        
        # all others command will followed by _
        # we can use any ohter variable name also!
        case _:
            print("Hey, you entered an unknown commad!")

print('Bye')