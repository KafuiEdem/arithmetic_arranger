def arithmetic_arranger(problems,cal=False):

    #placeholer to keep the arrange problems
    arranged_problems = ""
    numerator = ""
    denominator = ""
    equal_to = ""
    answer = ""

    
    count_item = 0
    for _ in problems:
        count_item +=1
    
    if count_item > 5:
        return "Error: Too many problems."
    
    else:
        for problem in problems:
            #storing the problems into tuples
            first_number, arithmetic_operator, second_number = problem.split()
            
            #checking if the correct operator has been used
            if arithmetic_operator not in ["-","+"]:
                return "Error: Operator must be \'+\' or \'-\'."

            #checking if the first and second number is a digit
            if not first_number.isdigit() or not second_number.isdigit():
                return "Error: Numbers must only contain digits."
            
            #checking if the first and second number are not greater than 4
            if  len(second_number)> 4 or len(first_number) > 4:
                return "Error: Numbers cannot be more than four digits."

            #checking the space to use

            space_to = max(len(first_number), len(second_number)) + 2

            
            #performing calculation
            if cal==True:
                if arithmetic_operator == "+":
                    add = int(first_number) + int(second_number)
                    answer += f"{str(add).rjust(space_to)}\n"
                    
                if arithmetic_operator == "-":
                    sub = int(first_number) - int(second_number)
                    answer += f"{str(sub).rjust(space_to)}\n"
                   

            numerator += f"{first_number.rjust(space_to)}    "
            denominator += f"{arithmetic_operator} {second_number.rjust(space_to -2)}    "
            equal_to += f"{'-'*space_to}    "
            

            arranged_problems = numerator.rstrip() + "\n" + denominator.rstrip() + "\n" + equal_to.rstrip()

            if answer:
                answer = f"{answer.rstrip()}    "
                arranged_problems += f"\n{answer.rstrip()}"

        return  arranged_problems

p = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(p)