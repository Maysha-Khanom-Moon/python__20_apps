date = input("Enter today's date: ")
mode = input("rate your mode between 0 to 10: ")
thought = input("tell me your thought: ") + '\n'

with open(f'bonus_8/{date}.txt', 'w') as file:
    file.write(mode + '\n\n')
    file.write(thought + '\n\n')

print("Thanks for today!")