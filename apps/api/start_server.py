import subprocess
from security import safe_command

command = ["poetry", "run", "uvicorn", "server:app", "--port", "8999"]


def uvi():
    try:
        process = safe_command.run(subprocess.Popen, command)
        process.wait()
    except Exception as e:
        print(f"Error occurred: {e}")


uvi()
