# Auto-Admin Password Rotator

## Description
This script automatically **relaunches itself with administrator privileges** (if not already running as admin) and **rotates a stored password** within the system environment variable `password`. After rotating, it **updates a Windows user account password** (`LENOVO` in this case) to the new password.

## How It Works
1. **Run as Admin**:  
   If the script isn't already running with administrative privileges, it relaunches itself with elevated permissions.
2. **Password Rotation**:  
   It expects an environment variable named `password`, containing a comma-separated list of passwords.
   - The script moves the first password to the end of the list (rotating it).
   - Updates the `password` environment variable with the new sequence.
3. **User Password Update**:  
   It updates the password for the user `LENOVO` to the new first password in the list using the `net users` Windows command.

## Requirements
- Windows OS
- Python 3.x
- Admin rights to modify user passwords

Example of setting the environment variable before running the script:

## Important Notes
- The script modifies the password of a **local user account** named `LENOVO`.  
  Ensure that this user exists, or update the username in the script accordingly.
- The password rotation is done **only in the running environment**.  
  Persistent storage (like writing back to system environment variables) is **not implemented**.
- Use carefully, especially in production environments, as it directly changes system user passwords.

## Disclaimer
This script is intended for educational, automation, or controlled environment usage.  
Use at your own risk.

---
