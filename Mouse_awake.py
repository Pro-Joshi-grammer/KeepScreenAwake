import pyautogui
import time

def keep_awake(duration_hours=3):#for how many hours you want the file to run
    duration_seconds = duration_hours * 3600
    interval = 25 #after every 25 seconds mouse moves 1 px you can change this to your convenience 
    start_time = time.time()

    print(f"Keeping screen awake for {duration_hours} hours")

    while time.time() - start_time < duration_seconds:
        pyautogui.moveRel(1, 0, duration=0.1)   
        pyautogui.moveRel(-1, 0, duration=0.1)   
        time.sleep(interval)  

    print("Done! Screen should be back to normal behavior.")

if __name__ == "__main__":
    keep_awake(3)  
