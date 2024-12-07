from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import subprocess
import send_email

app = FastAPI()

class CommandInput(BaseModel):
    base_command: str
    arguments: List[str]  # Use typing.List for compatibility

@app.post("/run-command/")
def run_command(command_input: CommandInput):
    """
    Run a shell command with multiple arguments securely.
    """
    try:
        # Base command validation
        allowed_commands = ["tctl"] #Ex: tctl users add <user_name> --role=<role_name> --logins=<logins> => tctl users add bao --roles=admin --logins=root
        if command_input.base_command not in allowed_commands:
            raise HTTPException(status_code=403, detail="Command not allowed!")
        
        email_to = list(filter(lambda x: x.startswith("--email"), command_input.arguments))
        if(email_to):
            command_input.arguments.remove(email_to[0])

        # Combine the command and its arguments
        command = [command_input.base_command] + command_input.arguments

        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        body = result.stdout.strip().replace("https://cloud:3080/", "https://14.225.69.121:3080/")
        if(("add" in command_input.arguments or "reset" in command_input.arguments) and email_to[0]):
            send_email.send_email(
                to_email=email_to[0].replace("--email=", ""),
                subject='Create User Teleport',
                body=body
        )
        # Return the output
        return {"output": body}

    except subprocess.CalledProcessError as e:
        # Handle command execution errors
        raise HTTPException(status_code=500, detail=f"Command failed: {e.stderr.strip()}")
    except Exception as e:
        # Catch-all for unexpected errors
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")