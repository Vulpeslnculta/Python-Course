import time

# print(time.gmtime(0))
#
# time_here = time.localtime()
#
# print(time_here)
# print(f"Year: {time_here[0]} \nMonth:"
#       f" {time_here[1]} \nDay: {time_here[2]}")
#

from time import perf_counter as my_timer
import random

input("___PRESS ENTER TO START___")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("___PRESS ENTER TO STOP___")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print(f"Your reaction time was: {end_time - start_time}")