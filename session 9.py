try:
    a=10
    b=90
    print(a+b)
except TypeError:
    print("Errpor occurs")
finally:
    print("finally works here")

class InsufficientBalanceError(Exception):
    pass
try:
    bal=1000
    withdraw=3000
    if withdraw>bal:
        raise InsufficientBalanceError("Insufficient bal")
    bal=bal-withdrawprint(bal)
except InsufficientBalanceError as e:
    print("occur occoured",e)
 