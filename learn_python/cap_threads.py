import threading
import time

def worker_ex(num):
    print(f"Start thread number={num}")
    time.sleep(2)
    print(f"End thread number={num}")


threads = []
for i in range(1, 4):
    thread = threading.Thread(target=worker_ex, args=(i,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print("All threads are done!")