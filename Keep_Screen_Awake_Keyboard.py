import time
import keyboard

def keep_awake(duration_hours=3):#for how many hours you want the file to run 
    duration_seconds = duration_hours * 3600
    interval = 5 #after every 5 seconds a key is pressed you can change this to your convenience 
    start_time = time.time()
    keys = ["shift", "ctrl", "alt", "caps lock"]

    print(f"Keeping screen awake for {duration_hours} hours...")

    i = 0
    while time.time() - start_time < duration_seconds:
        key = keys[i % len(keys)]
        #print(f"Pressing: {key}")
        #uncomment the print statement if you want to see which key is being pressed not mandatory 
        keyboard.press_and_release(key)
        i += 1
        time.sleep(interval)

    print("Done!")

if __name__ == "__main__":
    keep_awake(3)
