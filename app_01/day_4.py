todos = []

while True:
    user_action = input('Type add, show, edit, or exit: ')
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
            
        case 'show':
            for item in todos:
                print(item)
        
        case 'edit':
            for i in range(len(todos)):
                print(i+1, ". ", todos[i])
            
            # index = todos.index('item')
            # dir(list)
            # todos.__setitem__(index, 'new value')
            number = int(input('Number of the todo to edit: '))
            new_todo = input('Enter new todo: ')
            todos[number-1] = new_todo
            print('Edit successful')
        
        case 'exit':
            break
        
        case _:
            print('Hey, you entered an unknown commad!')

print('Bye!')