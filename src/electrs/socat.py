#Batch file
    # @echo off
    # wsl -d <your-distro> -- bash -c "nohup socat TCP-LISTEN:8080,fork TCP:localhost:9090 &"

import win32com.client

def create_scheduled_task():
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()

    rootFolder = scheduler.GetFolder('\\')
    taskDef = scheduler.NewTask(0)

    # Trigger: At startup
    trigger = taskDef.Triggers.Create(1)  # 1 = TASK_TRIGGER_BOOT

    # Action: Run WSL command
    action = taskDef.Actions.Create(0)  # 0 = TASK_ACTION_EXEC
    action.Path = 'wsl.exe'
    action.Arguments = '-d Ubuntu-20.04 -- bash -c "nohup socat TCP-LISTEN:8080,fork TCP:localhost:9090 &"'

    # Task settings
    taskDef.RegistrationInfo.Description = 'Start socat in WSL at startup'
    taskDef.Principal.UserId = 'SYSTEM'
    taskDef.Principal.LogonType = 0  # TASK_LOGON_SERVICE_ACCOUNT
    taskDef.Settings.Enabled = True
    taskDef.Settings.StartWhenAvailable = True
    taskDef.Settings.DisallowStartIfOnBatteries = False
    taskDef.Settings.StopIfGoingOnBatteries = False

    # Register the task
    rootFolder.RegisterTaskDefinition(
        'StartSocatWSL',  # Task name
        taskDef,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # No user context
        None,  # No password
        3,  # TASK_LOGON_SERVICE_ACCOUNT
        None  # No password
    )

########################################################################################    

#alternative to socat...
import socket
import threading

# Define the source and destination addresses and ports
SOURCE_HOST = '0.0.0.0'  # Listen on all interfaces
SOURCE_PORT = 8080  # Port to listen on
DESTINATION_HOST = '127.0.0.1'  # Forward to localhost or another address
DESTINATION_PORT = 80  # Port to forward to

# Function to handle incoming connections
def handle_client(client_socket, destination_host, destination_port):
    # Create a socket to connect to the destination
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as forward_socket:
        try:
            forward_socket.connect((destination_host, destination_port))

            # Start forwarding data between the client and the destination
            while True:
                # Receive data from the client
                client_data = client_socket.recv(4096)
                if len(client_data) == 0:
                    break

                # Send the data to the destination
                forward_socket.sendall(client_data)

                # Receive data from the destination
                forward_data = forward_socket.recv(4096)
                if len(forward_data) == 0:
                    break

                # Send the data back to the client
                client_socket.sendall(forward_data)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

# Main function to start the port forwarding
def start_forwarding(source_host, source_port, destination_host, destination_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((source_host, source_port))
        server_socket.listen(5)
        print(f"Listening on {source_host}:{source_port} and forwarding to {destination_host}:{destination_port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            client_handler = threading.Thread(
                target=handle_client,
                args=(client_socket, destination_host, destination_port)
            )
            client_handler.start()

if __name__ == "__main__":
    start_forwarding(SOURCE_HOST, SOURCE_PORT, DESTINATION_HOST, DESTINATION_PORT)
    
