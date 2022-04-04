import os
print("The file folder in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
