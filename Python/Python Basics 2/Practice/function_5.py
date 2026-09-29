'''

Practice Challenge: GenAI Token Estimator & Request Manager
Write a Python function named manage_genai_request with the following parameters:

prompt (positional parameter, required string)

model_name *(default parameter set to "gemini-pro")

max_tokens (default parameter set to 100)

safety_filter (default parameter set to True)

Function Requirements:
Part 1: Initial Safety Check
If safety_filter is True AND the word "exploit" is in prompt (case-sensitive check: "exploit" in prompt):

Print "Request blocked by safety filter!"

return "BLOCKED" immediately.

Part 2: Interactive Token Trimming Loop
If it passes the safety check, print:

"Processing prompt with model '<model_name>'..."

Then enter a while loop to manage the token limit:

Calculate estimated tokens as the length of the prompt divided by 4:

estimated_tokens = len(prompt) // 4

Check if estimated_tokens <= max_tokens:

If yes, print "Prompt approved! Estimated tokens: <estimated_tokens>".

return estimated_tokens (exiting the function with the final token count).

If estimated_tokens > max_tokens:

Print "Prompt exceeds max token limit (<estimated_tokens>/<max_tokens>)!"

Ask the user: choice = input("Option: 'trim' prompt, 'skip', or 'cancel'? ")

"trim": Ask for a new shortened prompt using input("Enter shorter prompt: "), update your prompt variable with this new string, and use continue to re-evaluate the length at the top of the loop.

"skip": Use pass as a placeholder for override logic, then print "Skipping token check." and return estimated_tokens.

"cancel": Print "Request canceled." and return "CANCELED".

Any other input: Print "Invalid option."

Requirements for Function Calls (Test Cases):
Write 3 different calls to manage_genai_request demonstrating your knowledge of arguments:

Call 1: Pass only the required positional argument prompt (e.g., "How does a neural network learn?").

Call 2: Use keyword arguments to change max_tokens to 5 and model_name to "gemini-flash", while leaving safety_filter at its default.

Call 3: Pass a prompt containing "exploit" using positional arguments, but set safety_filter=False using a keyword argument to bypass the block.

'''

def manage_genai_request(prompt, model_name = "gemini-pro", max_tokens = 100, safety_filter = True):
    if safety_filter and "exploit" in prompt:
        print("Request blocked for safety filter!")
        return "BLOCKED"
    print(f"Processing prompt with model {model_name}")
    
    while True:
        estimated_tokens = len(prompt) // 4
        if estimated_tokens <= max_tokens:
            print(f"Prompt approved! Estimated tokens {estimated_tokens}")
            return estimated_tokens
        
        if estimated_tokens > max_tokens:
            print(f"Prompt exceeds max token limit ({estimated_tokens} / {max_tokens})!")
            choice = input("Option: 'trim' prompt, 'skip', or 'cancel'? ")
            if choice == "trim":
                prompt = input("Enter shorter prompt: ")
                continue
            elif choice == "skip":
                pass
                print("SKipping token check")
                return estimated_tokens
            elif choice == "cancel":
                print("Request canceled.")
                return "CANCELED"
            else:
                print("Invalid option.")
                
manage_genai_request("How does a neural network learn")
manage_genai_request("What is a neural network?", max_tokens = 5, model_name = "gemini-flash")
manage_genai_request(prompt = "exploit", safety_filter = False)