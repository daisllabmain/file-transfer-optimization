import subprocess
import time

# Private key path (replace with actual path)
private_key_path = "/home/cc/key/chameleon_key.ppk"

# Define method and thread combinations
methods = ["probe", "brute"]  # Add more methods as needed
threads = [1, 2, 3, 4]  # Add more thread values as needed

# Receiver information
receiver_ip = "129.114.108.66"
receiver_port = 8000
receiver_script = "/home/cc/Falcon-File-Transfer-Optimizer/receiver.py"
receiver_env = "source mak_env/falcon_env/bin/activate"

def run_remote_command(command):
  """
  Runs a command on the remote server using the specified private key.
  """
  ssh_command = f"ssh -i {private_key_path} cc@{receiver_ip} 'nohup {command} &'"
  subprocess.run(ssh_command.split(), check=True)

def main():
  """
  Starts the receiver on the remote server.
  """
  run_remote_command(f"source mak_env/falcon_env/bin/activate")
  run_remote_command(f"python3 /home/cc/Falcon-File-Transfer-Optimizer/receiver.py")


# def main():
#   # Start the receiver
#   run_remote_command()


if __name__ == "__main__":
  main()

