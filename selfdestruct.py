print ("This system will self-destruct in...")
count = 10
import time
while True:
	print(count)
	count = count - 1
	time.sleep(1)
	if count < 1: break
print("BOOM")
