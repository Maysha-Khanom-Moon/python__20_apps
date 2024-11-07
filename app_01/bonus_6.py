a = [1, 2, 3]
b = [10, 20, 30]

for i, j in zip(a, b):
    print(f'a: {i} And b: {j}')
    

contents = ['All carrots are to be sliced longitudinally.', 
            'The carrots were reportedly sliced.', 
            'The slicing process was well presented.']

filenames = ['doc.txt', 'roport.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    # folder have to create before!
    file = open(f'bonus_6/{filename}', 'w')
    
    # write --> single content
    file.write(content)
    

# a = 'abc' \
# 'def' --> 'abc def'
# never gives a space after \

a = 'I am a string' \
    'on my own'

print(a)