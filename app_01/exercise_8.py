sides = []

while True:
    user_side = input("Throw the coin and enter head or tail here: ? ")
    user_side = user_side.strip()
    
    if user_side not in ('head', 'tail'):
        print('unknown side')
        continue
    
    sides.append(user_side)
    
    head_count = sides.count('head')
    
    percentage = (head_count / len(sides)) * 100
    
    print(f"Heads: {percentage}%")