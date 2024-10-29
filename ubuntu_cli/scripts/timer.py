from ubuntu_cli.modules.sys_paths import ubuntu_cli_dir
from ubuntu_cli.modules.terminal import run_terminal

timer: str = 'modules.timer.run_timer'
commands: list[str] = [
    f'cd {ubuntu_cli_dir}',
    f'python3 -m {timer}',
]

if __name__ == '__main__':
    run_terminal(commands=commands, window_size='52x10')
