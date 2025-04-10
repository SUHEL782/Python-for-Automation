import subprocess

def run_command(command):
    """Run a command in the shell and return the output."""
    try:
        result = subprocess.run(command, shell=True,
                                 check=True, text=True, 
                                 
                                 capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e.stderr.strip()}")
        return None
    
    # Check docker run or not
def check_docker_run():
 """Check if Docker is running."""
result = run_command("docker info")
if result:
    print("Docker is running.")
else:
            print("Docker is not running. Please start Docker.")