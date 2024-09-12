import datetime
import sys
import time
from subprocess import run
from typing import List


class Timer:

    @staticmethod
    def get_timer_name() -> str:
        prompt: str = 'Specify custom timer name or leave empty:\n>>> '
        timer_name: str = input(prompt)

        return timer_name

    @staticmethod
    def get_timer_duration() -> (int, int, int):
        time_units: List[str] = ['hours', 'minutes', 'seconds']
        duration_inputs: List[int] = []

        for time_unit in time_units:
            prompt: str = f'Enter the time in {time_unit}: '
            duration_input: str = input(prompt)

            if duration_input:
                duration_inputs.append(int(duration_input))
            else:
                duration_inputs.append(0)

        hours, minutes, seconds = duration_inputs

        return hours, minutes, seconds

    def countdown(self):
        hours, minutes, seconds = self.get_timer_duration()
        duration_in_seconds: int = hours * 3600 + minutes * 60 + seconds

        while duration_in_seconds > 0:
            timer = datetime.timedelta(seconds=duration_in_seconds)

            # print(timer, end="\r") didn't work
            sys.stdout.write(f'\r{timer}')
            sys.stdout.flush()

            time.sleep(1)
            duration_in_seconds -= 1

    def main(self):
        timer_name = self.get_timer_name()

        self.countdown()

        end_message: str = '\n\nCountdown ended...'
        if timer_name:
            end_message = f'\n\nCountdown ended for {timer_name}...'

        # presupposes you have 'spd-say' installed
        speech_command: List[str] = ['spd-say', f'{end_message}']

        print(f'{end_message}')
        run(speech_command, check=True)
