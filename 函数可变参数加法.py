def addV(*args):
    sides=len(args)
    print('There are',sides,'sides to the object')
    total=0
    for i in range(0,sides):
        total=total +args[i]
    return total

object1 = addV(2,3,4)
print('the object1 total is:',object1)

object2 = addV(2,3,4,5)
print('the object2 total is:',object2)

object3 = addV(2,3,4,5,10)
print('the object3 total is:',object3)
