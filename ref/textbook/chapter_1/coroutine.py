import asyncio
import time

async def main():
    for i in range(1, 6):
        await myfunction(i)
        print("In main", i)

async def myfunction(num):
    print("In my function", num)
    time.sleep(2)

start_time = time.time()  # Record start time
asyncio.run(main())
end_time = time.time()  # Record end time
print(f"Asynchronous execution time: {end_time - start_time:.10f} seconds")

print("Without async programming")

def main2():
    for i in range(1, 6):
        myfunction2(i)
        print("In main2", i)

def myfunction2(num):
    print("In my function2", num)
    time.sleep(2)

start_time = time.time()  # Record start time
main2()
end_time = time.time()  # Record end time
print(f"Synchronous execution time: {end_time - start_time:.10f} seconds")
