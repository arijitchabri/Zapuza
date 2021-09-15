tag = input()
vl = {"A", "E", "I", "O", "U", "Y"}
if tag[2] in vl:
    print('invalid')
elif (int(tag[0]) + int(tag[1])) % 2 != 0 or (int(tag[3]) + int(tag[4])) % 2 != 0 or (int(tag[4]) + int(tag[5])) % 2 !=\
        0 or (int(tag[7]) + int(tag[8])) % 2 != 0:
    print('invalid')
else:
    print('valid')

"""
    Algo technique used:- 
        Here we are using the brute force method for solving the problem.
    Algorithm:
        1.> Take the tag as an input.
        2>  if 3rd element is in vl list
                print invalid
        3>  elif the consecutive numbers sum is not even
                print invalid
        4>  else
                print valid   
            
    Thinking behind the logic building :-     
        The problem has given us the information that the input format will be: "DDADDD-DD"
    So in our code we first take the input and referencing the variable "tag" to it.
    We created the vl set for storing the vowels "A, E, I, O, U, Y" we used set
    because set gives us a edge in comparison.
    Then we check the alphabet if it is in the vl set then the code will print invalid 
    else it will go to the elif block and check if the sum of the consecutive elements are even or not
    if not Then it will again print invalid.
    Else it will go to the else block and print valid and the program will be successfully executed.
    We dont check the condition for zero as the problem instruct us that zero will not be given to us as an input.
    
    Why brute force:
        As we mention earlier that the input for this problem is provided to us. 
    We used the brute force method to solve the problem. But rather than this we try to implement other 
    approaches and found some prose and cons and decided to stick with the brute force method.
    (Though the solution is a static solution for this problem but gives us the best efficient time complexity).
    Rather than this the brute force method is easy to implement and better for understanding.
    
    **The complexity of the code is in liner.

"""
