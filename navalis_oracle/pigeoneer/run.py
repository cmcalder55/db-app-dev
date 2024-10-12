import subprocess
import threading

# Function to run a script
def run_script(script_name):
    subprocess.run(['python', script_name])

# Function to monitor and terminate subprocesses
def monitor_subprocesses(scripts):
    # Start subprocesses
    processes = [subprocess.Popen(['python', script]) for script in scripts]

    try:
        # Wait for any subprocess to exit
        while all(proc.poll() is None for proc in processes):
            pass
    finally:
        # Terminate all subprocesses
        for proc in processes:
            if proc.poll() is None:  # Check if subprocess is still running
                proc.terminate()
                proc.wait()

if __name__ == "__main__":
    # List of scripts to run
    scripts = ['send_bot_msg.py', 'poe_messenger.py']

    # Start the monitoring thread
    monitor_thread = threading.Thread(target=monitor_subprocesses, args=(scripts,))
    monitor_thread.start()

    # Wait for the monitoring thread to finish
    monitor_thread.join()