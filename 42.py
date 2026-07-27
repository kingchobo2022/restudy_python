count = 0

def increase_count():
    global count
    count = count + 1
    return count

a = increase_count()    
print(a)