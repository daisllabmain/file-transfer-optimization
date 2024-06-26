#!/bin/bash

# Path to the RAPL energy consumption file
RAPL_PATH="/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj"

# Interval in seconds
INTERVAL=1

# Function to get the current energy consumption
get_energy() {
    cat $RAPL_PATH
}

# Open the CSV file in append mode (>>)
csv_file="/home/cc/daisllab/file-transfer-optimization/Falcon-File-Transfer-Optimizer/automation/power_data.csv"
#echo "Timestamp,Power (W)" >> "$csv_file"  # Add header row

# Initial energy value
initial_energy=$(get_energy)

while true; do
    # Sleep for the specified interval
    sleep $INTERVAL

    # Get the new energy value
    new_energy=$(get_energy)

    # Calculate the energy consumed during the interval
    energy_diff=$((new_energy - initial_energy))

    # Convert energy to watts (joules per second)
    power=$(echo "$energy_diff / ($INTERVAL * 1000000)" | bc -l)

    # Log the power consumption with timestamp
    #echo "$(date) : $power W"
    # Log the power consumption with timestamp to the CSV file
    echo "$(date),$power" >> "$csv_file"

    # Update the initial energy value
    initial_energy=$new_energy
done