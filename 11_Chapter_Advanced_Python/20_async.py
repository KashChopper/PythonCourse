"""
async is a keyword in Python that is used to define asynchronous functions, which are functions that can be paused and resumed, allowing for non-blocking execution. This is particularly useful for tasks that involve waiting for I/O operations, such as network requests or file handling, without blocking the main thread of execution.
"""

# example of async function 
import asyncio
async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
# To run the async function, we need to use an event loop
asyncio.run(main())

async def greet(name):
    print(f"Hello, {name}!")
    print(f"Goodbye, {name}!")

asyncio.run(greet("Aasif"))