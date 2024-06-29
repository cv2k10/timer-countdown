import time
import json
import os

def load_config(file_path='config.json'):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config['timer_value']

def countdown_timer(timer_value, beep_function=None):
    while timer_value:
        mins, secs = divmod(timer_value, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end='\r', flush=True)
        time.sleep(1)
        timer_value -= 1
    if beep_function:
        beep_function()
    print("\nTimer finished! Press 'r' to reset to run again or 'x' to exit.")

def system_beep():
    os.system('afplay /System/Library/Sounds/Ping.aiff')

def main():
    while True:
        timer_value = load_config()
        countdown_timer(timer_value, system_beep)
        reset = input()
        while reset.lower() not in ('r', 'x'):
            print("Invalid input. Please press 'r' to reset to run again or 'x' to exit.")
            reset = input()
        if reset.lower() == 'x':
            print("Exiting the timer. Goodbye!")
            break

if __name__ == "__main__":
    main()
