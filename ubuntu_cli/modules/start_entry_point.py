import os
from subprocess import run

from ubuntu_cli.modules.sys_paths import ubuntu_cli_dir


def main() -> None:
    available_scripts: list = get_available_scripts(
        script_to_ignore='start_ubuntu_cli.py'
    )
    prompt: str = create_input_prompt(available_scripts)
    command_input_interface(prompt, available_scripts)


def command_input_interface(prompt: str, available_scripts: list) -> None:
    is_active: bool = True

    while is_active:
        print(prompt)
        command: str = input('\n>>> ')

        if command == 'q':
            is_active = False
        else:
            if command in available_scripts:
                command: list[str] = ['poetry', 'run', f'{command}']
                run(command, check=True)

            else:
                print(
                    f'Command "{command}" not recognized.\n'
                    f'Please make sure one of the commands shown in the '
                    f'greeting is entered.'
                )
            print('=' * 10)


def get_available_scripts(script_to_ignore: str) -> list:
    available_scripts: list = os.listdir(
        path=f'{ubuntu_cli_dir}/ubuntu_cli/scripts'
    )

    # filter out non-scripts, current file and .py extensions
    available_scripts = [
        os.path.splitext(script)[0]
        for script in available_scripts
        if script.endswith('.py') and
           script != script_to_ignore and script != '__init__.py'
    ]

    return available_scripts


def create_input_prompt(available_scripts: list) -> str:
    prompt: str = (
        'Welcome to UbuntuCLI!\n\n'
        'Choose the script you\'d like to run from the list of available '
        'commands.\n'
        'Alternatively, enter "q" to exit. Available commands are listed '
        'below:\n' +
        ''.join(f'\n{script}' for script in available_scripts)
    )
    return prompt
