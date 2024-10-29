from ubuntu_cli.modules.sys_paths import ubuntu_cli_dir
from ubuntu_cli.modules.terminal import run_terminal


def run_timer() -> None:
    timer: str = 'ubuntu_cli.modules.timer.run_timer'
    commands: list[str] = [
        f'cd {ubuntu_cli_dir}',
        f'python3 -m {timer}',
    ]

    run_terminal(commands=commands, window_size='52x10')


if __name__ == '__main__':
    run_timer()
