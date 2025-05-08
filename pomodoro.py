import time
import click
import tqdm

def sessions_validation(sessions):
    return True if sessions >= 1 else False

@click.command()
@click.option('-w','--work', default = 1, help="Working time (minutes)")
@click.option('-b','--break_', default = 1, help="Rest time (minutes)")
@click.option('-s','--sessions', default = 4, help="Number of 🍅Pomodoro rounds")
def pomodoro(work, break_, sessions):
    # Input validation
    while not sessions_validation(sessions):
        click.echo("Error: Numbers of sessions must be equal or greater than 1")
        sessions = int(input("Please enter a new session numbers: "))
    session_progress = 1
    while session_progress <= sessions:
        click.echo("####################")
        click.echo(f"# [ Session: {session_progress}/{sessions} ] #")
        click.echo("####################")


        for i in tqdm.trange(work, desc=f'🍅 Sessions: {session_progress}/{sessions}'):
            time.sleep(1)
        session_progress += 1
        if session_progress >  sessions:
            response = input("congratulations 🎉, press any button to quit.")
            break
        response = input(f"End of session {session_progress}, press any button to start a break")
        for i in tqdm.trange(break_, desc="☕ Break"):
            time.sleep(1)
        response = input(f"End of the break, press any button to begin session {session_progress}")

if __name__ == '__main__':
    pomodoro()
    