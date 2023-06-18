
x = input("Enter num: ")
error_margin = 1
square_root(x)

def square_root(x)
    if x<0 
      then print("Please enter non-negative integer")
    a = 1
    b = x
    while (abs(a-b)>error_margin) 
        a = (a+b)/2
        b = x/a
    endwhile
    return abs(a);
