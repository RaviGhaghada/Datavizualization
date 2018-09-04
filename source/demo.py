def guess(low, high):
    if low == high:
        return low
    print("\nIs your number more than ", int((low+high)/2), "? (enter y or n): ")
    ans = input()
    while ans!="y" and ans!="n":
        print("\nHEY! Please enter only 'y'(for yes) or 'n' (for no): ")
        ans=input()
    if ans == 'y':
        return guess(1+int((low+high)/2), high)
    elif ans == 'n':
        return guess(low, int((low+high)/2))   

print("Hello! Get ready for a magic trick! THINK of any number between 1 and 100...I will guess it in 7 tries!\n")
answer = guess (1, 100)
print("\nYou were thinking of ", answer, "!!!")
