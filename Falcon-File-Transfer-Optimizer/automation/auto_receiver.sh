#!/bin/bash

# Receiver Variables
remoteReceiverUser="cc"
remoteReceiverIP="192.5.87.150"
remoteReceiverKey="C:/Users/mosta/key_storage/chameleon_key_uc.pem"
activateREnvCommand="source mak_env/falcon_env/bin/activate"
additionalCommandR="python3 /home/cc/Falcon-File-Transfer-Optimizer/receiver.py"
stopFirewall="sudo service firewalld stop"

# Function to run a command on a remote machine using SSH
run_remote_command() {
    local user=$1
    local ip=$2
    local key=$3
    local command=$4
    ssh -i "$key" "$user@$ip" "$command"
}

# # Kill all processes of user "cc" on the remote machine
# echo "Killing all processes of user $remoteReceiverUser on $remoteReceiverIP"
# ssh -i "$remoteReceiverKey" "$remoteReceiverUser@$remoteReceiverIP" "pkill -u $remoteReceiverUser"

# # Connect to the remote receiver, activate the environment, and run the receiver command
# echo "Connecting to the remote receiver"
# receiverCommand="bash -c '$activateREnvCommand && $additionalCommandR && $stopFirewall'"
# run_remote_command "$remoteReceiverUser" "$remoteReceiverIP" "$remoteReceiverKey" "$receiverCommand"

# read -p "Press Enter to exit"

# Infinite loop to continuously run the script
while true; do
    # Kill all processes of user "cc" on the remote machine
    echo "Killing all processes of user $remoteReceiverUser on $remoteReceiverIP"
    ssh -i "$remoteReceiverKey" "$remoteReceiverUser@$remoteReceiverIP" "pkill -u $remoteReceiverUser"

    # Connect to the remote receiver, activate the environment, and run the receiver command
    echo "Connecting to the remote receiver"
    receiverCommand="bash -c '$activateREnvCommand && $additionalCommandR && $stopFirewall'"
    run_remote_command "$remoteReceiverUser" "$remoteReceiverIP" "$remoteReceiverKey" "$receiverCommand"

    #read -p "Press Enter to restart the process, or Ctrl+C to exit."
done
