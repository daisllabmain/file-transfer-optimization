#!/bin/bash

# Sender Variables
remoteSenderUser="cc"
remoteSenderIP="129.114.109.142"
remoteSenderKey="C:/Users/mosta/key_storage/chameleon_key.pem"
powerCommand="sudo nohup python3 /home/cc/daisllab/file-transfer-optimization/Falcon-File-Transfer-Optimizer/automation/power_data.py"

# Function to run a command on a remote machine using SSH
run_remote_command() {
    local user=$1
    local ip=$2
    local key=$3
    local command=$4
    ssh -i "$key" "$user@$ip" "$command"
}
senderCommand="bash -c '$powerCommand' &"
run_remote_command "$remoteSenderUser" "$remoteSenderIP" "$remoteSenderKey" "$senderCommand"

read -p "Press Enter to exit"
