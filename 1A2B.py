import random 

def game_start():
    print("Robot: I have generated a secret number for you. That's guessing time!")
    mode = input("Choose a mode [A]:unlimited, [B]:limited,[R]:rule,[X]:exit : ").strip().upper()
    ## exit mode
    if mode == 'X':
        print("Exiting the game. Goodbye!")
        return "exit"
    ## rules mode
    if mode == 'R':
        print("Rules of the game:")
        print("1. The secret number consists of 4 unique digits (0-9).")
        print("2. You will receive feedback in the format 'xAyB', where x is the number of correct digits in the correct position, and y is the number of correct digits in the wrong position.")
        print("3. In mode [A], you can guess as many times as you want until you find the secret number.")
        print("4. In mode [B], you have a limited number of attempts to guess the secret number.")
        return 
    ## GAME mode
    if mode == 'B':
        max_attempts = int(input("Enter the maximum number of attempts: "))
    elif mode == 'A':
        max_attempts = float('inf')  # Unlimited attempts
    else:
        print("Invalid mode selected. Please choose A, B, R, or X.")
        return
    
    attempts = 0
    secret_number = random.sample(range(10), 4)
    #print(secret_number)
    while attempts < max_attempts:
        guess = input("Enter your guess (4 unique digits): ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Please enter 4 unique digits.")
            continue
        
        guess_digits = [int(digit) for digit in guess]
        a_count = sum(1 for i in range(4) if guess_digits[i] == secret_number[i])
        b_count = sum(1 for digit in guess_digits if digit in secret_number) - a_count
        
        print(f"{a_count}A{b_count}B")
        
        if a_count == 4:
            print("Congratulations! You've guessed the secret number!")
            break
        
        attempts += 1
        if attempts >= max_attempts:
            print("Game over! You've used all your attempts.")
            print(f"The secret number was: {''.join(map(str, secret_number))}")

        # prompt for next guess
        n = 0
        if do_prompt():
            print("Robot: Do you want to have some hints? [Y/N]")
            hint = input().strip().upper()
            if hint == 'Y':
                print(f"Hint: The first digit is {secret_number[n]}.")
                n+=1
                if n>= 3:
                    print("Robot: emm... Do you to try a new game?")
            else:
                print("No hints provided.")

def do_prompt():
    if random.randint(0, 10) <= 2:
        return True
    else:
        return False
def main():
    print("Welcome to the 1A2B game!")
    print("Try to guess the secret number consisting of 4 unique digits.")
    r = ""
    while r != "exit":
        r = game_start()
        if r == "exit":
            break
        print("Do you want to play again? [Y/N]")
        play_again = input().strip().upper()
        if play_again != 'Y':
            print("Thank you for playing! Goodbye!")
            break 
    

if __name__ == "__main__":
    main()