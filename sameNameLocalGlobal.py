def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs) # this is global statement. because there is not an assignment statemnt

eggs = 42
spam()
print(eggs)