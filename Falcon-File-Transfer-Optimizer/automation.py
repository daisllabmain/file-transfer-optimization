import paramiko
import sys

# Replace with your actual values
private_key_path = "/home/cc/key/chameleon_key.ppk"
receiver_ip = "129.114.108.66"
sender_ip = "129.114.109.142"
receiver_username = "cc"
receiver_env = "source mak_env/falcon_env/bin/activate"
receiver_script = "python3 /home/cc/Falcon-File-Transfer-Optimizer/receiver.py"

def run_remote_script(private_key_path, receiver_ip, receiver_username, receiver_env, receiver_script):
  """
  Establishes an SSH connection to the receiver, activates the environment, and runs the script.
  """
  try:
    # Load the private key
    key = paramiko.RSAKey.from_private_key_file(private_key_path)
    print("key loaded!") 

    # Create SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=receiver_ip, username=receiver_username, pkey=key)

    print("host connected!")

    # Activate virtual environment (if necessary)
    stdin, stdout, stderr = client.exec_command(receiver_env)
    print(stdout.read().decode())  # Print any output from environment activation
    print(stderr.read().decode(), file=sys.stderr)  # Print any errors

    print("env created!")

    # Run the receiver script
    stdin, stdout, stderr = client.exec_command(receiver_script)

    print("receiver run!")

    print(stdout.read().decode())  # Print output from receiver script
    print(stderr.read().decode(), file=sys.stderr)  # Print any errors from script execution

    client.close()
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  run_remote_script(private_key_path, receiver_ip, receiver_username, receiver_env, receiver_script)
