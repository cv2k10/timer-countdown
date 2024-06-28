import time
import json
import os
import keyboard

def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config['timer_value']

def countdown_timer(timer_value):
    while timer_value:
        mins, secs = divmod(timer_value, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end='\r')
        time.sleep(1)
        timer_value -= 1
    os.system('afplay /System/Library/Sounds/Ping.aiff')
    print("Timer finished! Press 'r' to reset and run again.")

def main():
    while True:
        timer_value = load_config()
        countdown_timer(timer_value)
        keyboard.wait('r')

if __name__ == "__main__":
    main()
