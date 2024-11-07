todos = []

while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()
    
    match user_action: 
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
            
        case 'show':
            # enumerate --> also works for string
            # ennumerate --> list of tuple --> (index, item)
            for index, item in enumerate(todos):
                # f'string'
                print(f'{index+1}. {item}')
            
            # This could cause an error if todos is empty because index and item will not be defined if the loop never runs.
            print(f'Length is {index+1}')
        
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        
        case 'complete':
            # remove --> romove that index's item
            # clear --> remove all the items
            # pop --> remove the index's item and return that!
            number = int(input('Number of the todo to complete: '))
            todos.pop(number-1)
        
        case 'exit':
            break 

print('Bye!')