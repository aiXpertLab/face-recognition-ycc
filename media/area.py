#area.py
from const import PI
print ("1area name root is : ", __name__)
 
def calc_round_area(radius):
    print ("2area name calc is: ", __name__)
    return PI * (radius ** 2)
    print ("3area name calc is: ", __name__)
 
def main():
    print ("round area: ", calc_round_area(2))
    print ("4area def name main is: ", __name__)

print ("5area name bf call main is: ", __name__)
main()
print ("6area name after call main is: ", __name__)
