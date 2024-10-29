from subprocess import run


def run_terminal(commands: list[str], window_size: str = '80x24') -> None:
    # without this, the window is closed after commands execution
    standby_command: str = 'read -p "\nPress Enter to exit..."'
    commands.append(standby_command)

    terminal_cmd: list[str] = [
        'gnome-terminal',
        f'--geometry={window_size}',
        '--',
        '/bin/bash',
        '-c',
        ';'.join(commands)
    ]

    run(terminal_cmd)


def wait_until_terminal_closed() -> None:
    standy_message: str = (
        '\nWaiting for temporary terminal window to be closed. '
        '\nOnce ready, close the window and press "Enter" to continue...'
    )

    input(standy_message)
