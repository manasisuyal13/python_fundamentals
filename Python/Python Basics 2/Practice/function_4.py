'''
HOMEWORK [28/09/2026]
GenAI Prompt Guard & Rate Limiter
You are building a security middleware layer for a Large Language Model (LLM) API. Write a function named genai_prompt_guard that takes two parameters:
max_tokens (an integer representing the maximum total token budget allowed for the session, e.g., 100)
api_key (a string representing the valid authorization key, e.g., "sk-genai2026")
 Requirements:
Authentication Phase
Prompt the user using input("Enter API Key: ").
Allow up to 3 attempts to enter the correct api_key.
If wrong, deduct an attempt and print "Authentication failed! Attempts remaining: X".
If 3 failed attempts occur, print "API Key Blocked: Unauthorized Access!" and return "UNAUTHORIZED".
Prompt Processing Loop (Once authenticated)
Print "API Authenticated. Session Active." and enter a while loop that continuously prompts:
input("Enter prompt action (generate/flag/test/tokens/exit): ")
Process commands as follows:
"generate":
Prompt for the prompt text using input("Enter your prompt: ").
Sanity / Safety Check: If the word "hack" is in the prompt text (e.g., "how to hack"), print "SAFETY TRIGGER: Jailbreak attempt detected! Prompt rejected." and use continue to restart the loop without using any tokens.
Prompt for the estimated token cost: int(input("Enter prompt token cost: ")).
If token cost is greater than max_tokens:
Print "Token limit exceeded for this request! Remaining budget: ".
Otherwise:
Deduct the token cost from max_tokens.
Print "Prompt processed successfully! Remaining token budget: ".
If max_tokens reaches 0, print "Token budget exhausted! Closing session." and return "BUDGET_EXHAUSTED".
"flag":
Print "Prompt flagged for manual safety review." and use continue to immediately request the next action.
"test":
Use pass as a temporary placeholder for testing custom system prompts.
"tokens":
Print "Current available token budget: ".
"exit":
Print "Session ended by user." and return max_tokens (exiting the function with the remaining token balance).
Any other action:
Print "Unknown prompt action. Please try again.".
 Example Call to Test Your Code:
# Test with a token budget of 50 and API key "sk-genai2026"
result = genai_prompt_guard(50, "sk-genai2026")
print("Session Result:", result)
'''
def genai_prompt_guard(max_tokens, api_key):
    attempts = 3

    while attempts > 0:
        key = input("Enter API Key: ")
        if key == api_key:
            break
        attempts -= 1
        if attempts > 0:
            print(f"Authentication failed! Attempts remaining: {attempts}")
        else:
            print(f"Authentication failed! Attempts remaining: 0")
    else:
        print("API Key Blocked: Unauthorized Access!")
        return "UNAUTHORIZED"

    print("API Authenticated. Session Active.")

    while True:
        action = input("Enter prompt action (generate/flag/test/tokens/exit): ")

        if action == "generate":
            prompt = input("Enter your prompt: ")

            if "hack" in prompt:
                print("SAFETY TRIGGER: Jailbreak attempt detected! Prompt rejected.")
                continue

            cost = int(input("Enter prompt token cost: "))

            if cost > max_tokens:
                print(f"Token limit exceeded for this request! Remaining budget: {max_tokens}")
            else:
                max_tokens -= cost
                print(f"Prompt processed successfully! Remaining token budget: {max_tokens}")

                if max_tokens == 0:
                    print("Token budget exhausted! Closing session.")
                    return "BUDGET_EXHAUSTED"

        elif action == "flag":
            print("Prompt flagged for manual safety review.")
            continue

        elif action == "test":
            pass

        elif action == "tokens":
            print(f"Current available token budget: {max_tokens}")

        elif action == "exit":
            print("Session ended by user.")
            return max_tokens

        else:
            print("Unknown prompt action. Please try again.")

result = genai_prompt_guard(50, "sk-genai2026")
print("Session Result:", result)