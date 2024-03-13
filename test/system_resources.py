import psutil

def get_system_resources() -> tuple:
    # Get the current CPU usage as a percentage
    cpu_usage = psutil.cpu_percent(interval=None, percpu=False)

    # Get the current memory usage as a percentage
    memory_usage = psutil.virtual_memory().percent

    return cpu_usage, memory_usage
    
get_system_resources()
i = 0
for j in range(1000000):
    i += 0.001*j
cpu_usage, memory_usage = get_system_resources()

print(f"CPU usage: {cpu_usage}%")
print(f"Memory usage: {memory_usage}%")