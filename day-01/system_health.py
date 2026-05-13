import psutil


def get_thresholds():
    print("=== Enter Threshold Values ===")

    cpu_threshold = float(input("CPU Threshold (%): "))
    memory_threshold = float(input("Memory Threshold (%): "))
    disk_threshold = float(input("Disk Threshold (%): "))

    return cpu_threshold, memory_threshold, disk_threshold


def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    return {
        "CPU": cpu_usage,
        "Memory": memory_usage,
        "Disk": disk_usage
    }


def check_health(metrics, thresholds):
    print("\n=== System Health Report ===")

    threshold_map = {
        "CPU": thresholds[0],
        "Memory": thresholds[1],
        "Disk": thresholds[2]
    }

    for metric, value in metrics.items():
        threshold = threshold_map[metric]

        print(f"{metric} Usage: {value}%")

        if value > threshold:
            print(f"WARNING: {metric} usage exceeded threshold!\n")
        else:
            print(f"{metric} usage is under control.\n")


def main():
    thresholds = get_thresholds()
    metrics = get_system_metrics()
    check_health(metrics, thresholds)


if __name__ == "__main__":
    main()
