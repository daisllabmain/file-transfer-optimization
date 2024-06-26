import subprocess
import csv
from datetime import datetime
import multiprocessing

# Path to the RAPL energy consumption file
RAPL_PATH = "/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj"

# Interval in seconds
INTERVAL = 1


def get_energy():
    """Gets the current energy consumption from RAPL file, handling empty output."""
    output = subprocess.run(["cat", RAPL_PATH], capture_output=True, text=True)
    if output.stdout.strip():  # Check if output is not empty
        return int(output.stdout.strip())
    else:
        # Handle empty output (e.g., log a message, return a default value)
        print("WARNING: Empty output from RAPL file!")
        return 0  # Or any appropriate default value


def main():
    """Continuously monitors and logs power consumption."""

    # Open the CSV file in append mode
    csv_file = "/home/cc/daisllab/file-transfer-optimization/Falcon-File-Transfer-Optimizer/automation/power_data.csv"
    #with open(csv_file, "a", newline="") as f:
        # Add header row (optional, uncomment if needed)
        # writer = csv.writer(f)
        # writer.writerow(["Timestamp", "Power (W)"])

    # Initial energy value
    initial_energy = get_energy()

    while True:
        # Sleep for the specified interval
        subprocess.run(["sleep", str(INTERVAL)])

        # Get the new energy value
        new_energy = get_energy()

        # Calculate the energy consumed during the interval
        energy_diff = new_energy - initial_energy

        # Convert energy to watts (joules per second)
        power = energy_diff / (INTERVAL * 1000000)

        # Log the power consumption with timestamp to the CSV file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(csv_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, power])

        # Update the initial energy value
        initial_energy = new_energy


if __name__ == "__main__":
    p = multiprocessing.Process(target=main)
    p.start()
