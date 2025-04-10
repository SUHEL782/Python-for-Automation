import execute_command
def docker_run()
    # Run a Docker container with the specified image and options
    execute_command.execute_command("docker run -it --rm -v $(pwd):/app -w /app python:3.9-slim bash")
    # The command above runs a Docker container with the following options:
    # -it: Interactive terminal
    # --rm: Automatically remove the container when it exits
    # -v $(pwd):/app: Mount the current directory to /app in the container
    # -w /app: Set the working directory to /app in the container
    # python:3.9-slim: The Docker image to use (Python 3.9 slim version)