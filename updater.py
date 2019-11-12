import time
with open(time.strftime("data/%Y-%m%-d %H_%M_%S.txt"), "w") as f:
    f.write("hello")