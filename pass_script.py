import os
import sys
import ctypes

def run_as_admin():
    # Check if the script is already running as admin
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Relaunch the script with admin rights
        script = sys.executable
        params = ' '.join([f'"{arg}"' for arg in sys.argv])  # Quotes for safety
        ctypes.windll.shell32.ShellExecuteW(None, "runas", script, params, None, 1)
        sys.exit()

# --- First thing we do: ensure admin ---
run_as_admin()

# password definition
# os.environ['password']="password1, password2, password3"

pass_list=os.environ['password'].split(",")
pass_list.append(pass_list[0])
pass_list.pop(0)
os.environ['password']=",".join(pass_list)

os.system(f"net users LENOVO {pass_list[0]}") 
