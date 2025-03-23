import time
seconds=int (input("enter seconds:"))    
def countdown_timer(seconds):    
    while seconds>0:
        print(f"Time left : {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Times up")
print(countdown_timer(seconds)) 