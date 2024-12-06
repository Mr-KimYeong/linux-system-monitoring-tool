import psutil
import time
import matplotlib.pyplot as plt

# Initialize lists for plotting
cpu_usage_list = []
memory_usage_list = []
disk_usage_list = []
network_sent_list = []
network_recv_list = []
timestamps = []

def log_to_file(data):
    with open("system_logs.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {data}\n")

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_usage_list.append(cpu_usage)
    return f"CPU Usage: {cpu_usage}%"

def get_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage_list.append(memory.percent)
    return f"Memory Usage: {memory.percent}%"

def get_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage_list.append(disk.percent)
    return f"Disk Usage: {disk.percent}%"

def get_network_stats():
    net = psutil.net_io_counters()
    network_sent_list.append(net.bytes_sent // (1024 ** 2))  # MB
    network_recv_list.append(net.bytes_recv // (1024 ** 2))  # MB
    return f"Network: Sent: {net.bytes_sent // (1024 ** 2)} MB, Received: {net.bytes_recv // (1024 ** 2)} MB"

def generate_report():
    # Plot CPU Usage
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, cpu_usage_list, label="CPU Usage (%)", color='blue')
    plt.plot(timestamps, memory_usage_list, label="Memory Usage (%)", color='green')
    plt.plot(timestamps, disk_usage_list, label="Disk Usage (%)", color='red')
    plt.plot(timestamps, network_sent_list, label="Network Sent (MB)", color='orange')
    plt.plot(timestamps, network_recv_list, label="Network Received (MB)", color='purple')

    plt.title("System Monitoring Report")
    plt.xlabel("Time")
    plt.ylabel("Usage / Traffic")
    plt.legend()
    plt.grid(True)
    plt.savefig("system_report.png")
    plt.close()

if __name__ == "__main__":
    for _ in range(10):  # Run for 10 cycles (can adjust)
        timestamps.append(time.strftime('%H:%M:%S'))
        print(get_cpu_usage())
        print(get_memory_usage())
        print(get_disk_usage())
        print(get_network_stats())
        time.sleep(60)  # Wait for 1 minute
    
    # Generate a report after collection
    generate_report()

