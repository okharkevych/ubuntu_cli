from ubuntu_cli.modules.terminal import run_terminal


def update_sw() -> None:
    commands: list[str] = [
        'snap-store --quit',
        'sudo snap refresh',
        'sudo apt update',
        'sudo apt upgrade -y',
        'sudo apt-get update',
        'sudo apt-get upgrade -y',
        'sudo apt autoremove -y',
        'flatpak update -y',
    ]
    run_terminal(commands)
