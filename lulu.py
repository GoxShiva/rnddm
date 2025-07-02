import os
import subprocess

# Ensure the script is executable
os.chmod("gsshiv_script", 0o777)

# Run the script
subprocess.run(["./gsshiv_script"])
