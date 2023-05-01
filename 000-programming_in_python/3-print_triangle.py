def print_right_triangle(height):
        for i in range(height):
            for j in range(i+1):
                print("*", end='')
            print("")


print_right_triangle(int(input("Enter height size; ")))
    
    