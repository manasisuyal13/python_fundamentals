#gathering inputs and type conversion
first_number = float(input("Enter your first number: "))
math_operator = input("Enter your operator [+, -, *, /, //, %]: ").strip()
second_number = float(input("Enter your second number: "))

result = f"The answer is: {first_number} + {math_operator.strip()} + {second_number}"

if math_operator == "+":
    result = first_number + second_number
    
elif math_operator == "-":
    result = first_number - second_number
    
elif math_operator == "*":
    result = first_number  * second_number
    
elif math_operator == "/":
    result = first_number  / second_number

elif math_operator == "//":
    result = first_number  // second_number
    
elif math_operator == "**":
    result = first_number  ** second_number
    
elif math_operator == "%":
    result = first_number  % second_number

else:
    result = None


result_type = type(result)

calc_history = {
    "first_number" : first_number,
    "math_operator" : math_operator,
    "second_number" : second_number,
    "result" : result_type
}

operator_result = calc_history.get("result", result)
parinaam_prakar = calc_history.get("reuslt_type", result_type)
summary = f"{first_number} {math_operator} {second_number} = {result} \n Your result is a {result_type}"
print(summary)
# yayyyyy
