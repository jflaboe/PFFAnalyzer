import time
with open(time.strftime("%H_%M_%S.txt"), "w") as f:
    f.write("hello")