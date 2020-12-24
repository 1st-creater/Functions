def spam():
    egg = 'spam local'
    print(egg)

def bacon():
    egg = 'bacon local'
    print(egg)
    spam()
    print(egg)

egg = 'global'
bacon()
print(egg)