#!/bin/bash

# Sender Variables
remoteSenderUser="cc"
remoteSenderIP="129.114.109.142"
remoteSenderKey="C:/Users/mosta/key_storage/chameleon_key.pem"
activateSEnvCommand="source mak_env/falcon_env/bin/activate"
stopFirewall="sudo service firewalld stop"

# Function to run a command on a remote machine using SSH
run_remote_command() {
    local user=$1
    local ip=$2
    local key=$3
    local command=$4
    ssh -i "$key" "$user@$ip" "$command"
}

# Loop for 3 iterations
for ((i = 4; i <= 40; i++)); do
    #echo "Iteration $i"

    # Calculate thread number dynamically
    # threadNumber=$((40 + i))

    # Construct additionalCommandS2 with dynamic thread number
    additionalCommandS2="python3 /home/cc/daisllab/file-transfer-optimization/Falcon-File-Transfer-Optimizer/sender.py --method probe --thread $i"

    # Delay for 5 seconds before each iteration (except the first)
    if [ $i -gt 1 ]; then
        sleep 5
    fi

    # # Kill all processes of user "cc" on the remote machine
    # echo "Killing all processes of user $remoteSenderUser on $remoteSenderIP"
    # ssh -i "$remoteSenderKey" "$remoteSenderUser@$remoteSenderIP" "pkill -u $remoteSenderUser"

    # # Connect to the remote sender, activate the environment, and run the sender command
    # echo "Connecting to the remote sender"
    # senderCommand="bash -c '$activateSEnvCommand && cd /home/cc/daisllab/file-transfer-optimization/Falcon-File-Transfer-Optimizer && $additionalCommandS2 && $stopFirewall'"
    # run_remote_command "$remoteSenderUser" "$remoteSenderIP" "$remoteSenderKey" "$senderCommand"

    # Nested loop for 10 iterations
    for ((j = 1; j <= 10; j++)); do
        echo "Iteration $i"_"$j"
        # Kill all processes of user "cc" on the remote machine
        echo "Killing all processes of user $remoteSenderUser on $remoteSenderIP"
        ssh -i "$remoteSenderKey" "$remoteSenderUser@$remoteSenderIP" "pkill -u $remoteSenderUser"

        # Connect to the remote sender, activate the environment, and run the sender command
        echo "Connecting to the remote sender"
        senderCommand="bash -c '$activateSEnvCommand && cd /home/cc/daisllab/file-transfer-optimization/Falcon-File-Transfer-Optimizer && $additionalCommandS2 && $stopFirewall'"
        run_remote_command "$remoteSenderUser" "$remoteSenderIP" "$remoteSenderKey" "$senderCommand"
        
        # Optional delay between nested iterations
        sleep 5
    done
done

read -p "Press Enter to exit"
