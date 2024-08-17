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