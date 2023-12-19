#const.py
PI = 3.14
print ("1_Constant name root is: ", __name__)
 
def main():
   print ("PI:", PI)
   print ("2_Constant name main is: ", __name__)

print ("3_Constant name bf if is: ", __name__)

if __name__ == "__main__":
    main()
   
print ("4_Constant name after main() is: ", __name__)