import time
import json
import os

def load_config():
    """
    Load the configuration from the 'config.json' file.

    Returns:
        int: The value of the 'timer_value' key in the configuration.

    Raises:
        FileNotFoundError: If the 'config.json' file cannot be found.
        JSONDecodeError: If the 'config.json' file is not a valid JSON file.
    """
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config['timer_value']

def countdown_timer(timer_value):
    """
    Countdown timer that displays the remaining time in minutes and seconds.
    
    Args:
        timer_value (int): The initial value of the timer in seconds.
    
    Returns:
        None
    
    This function continuously displays the remaining time in minutes and seconds 
    until the timer reaches zero. After the timer finishes, it plays a sound 
    notification and prompts the user to press 'r' to reset the timer or 'x' to 
    exit.
    """
    while timer_value:
        mins, secs = divmod(timer_value, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end='\r', flush=True)
        time.sleep(1)
        timer_value -= 1
    os.system('afplay /System/Library/Sounds/Ping.aiff')
    print("\nTimer finished! Press 'r' to reset to run again or 'x' to exit.")

def main():
    """
    A function that controls the main flow of the timer program. It continuously loads the timer configuration, displays the countdown timer, and prompts the user for input to reset or exit the timer.
    """
    while True:
        timer_value = load_config()
        countdown_timer(timer_value)
        reset = input()
        while reset.lower() not in ('r', 'x'):
            print("Invalid input. Please press 'r' to reset to run again or 'x' to exit.")
            reset = input()
        if reset.lower() == 'x':
            print("Exiting the timer. Goodbye!")
            break

if __name__ == "__main__":
    main()
