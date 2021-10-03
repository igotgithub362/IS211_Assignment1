"Function listDivide with arguments numbers and divide"
def listDivide(numbers, divide = 2):
    divisibleCount = 0
    for everyNum in numbers:
        if everyNum % divide == 0:
            divisibleCount += 1

    return divisibleCount

"Custom exception class"

class ListDivideException(Exception):
    pass

"Function testListDivide"

def testListDivide():
    try:
        if not listDivide([1,2,3,4,5]) == 2:
            raise ListDivideException
        if not listDivide([2,4,6,8,10]) == 5:
            raise ListDivideException
        
