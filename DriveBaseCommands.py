import debug as d
from debug import test_decorator

class RobotCommand:

    def run():

        pass

    def undo():

        pass

class RobotStraight(Command):

    def run(distance):

        d.straight(distance)

    def undo(distance):

        d.straight(-distance)

class Invoker:
    def __init__(self):

        self._commands = {}  # It registers all the commands

        self._history = []  # It registers the command objects in the order they were called.

    def show_history(self):

        for row in self._history:

            print(f"{datetime.fromtimestamp(row[0]).strftime('%H:%M:%S')}", f" : {row[1]}")

    def register(self, command_name, command):

        self._commands[command_name] = command

    def execute(self, command_name):

        if command_name in self._commands.keys():

            self._commands[command_name].execute()

            self._history.append((time.time(), command_name))

    def undo(self, command_name):

        if command_name in self._commands.keys():

            self._commands[command_name].undo()

            self._history.append((time.time(), "Undo"))


    def replay_last(self, number_of_commands=1):

        """Replay the last N commands"""

        commands = self._history[-number_of_commands:]

        for command in commands:


            # The below line will just replay the code, it will not be logged in history
            # self._commands[command[1]].execute()

            self.execute(command[1])  # The command will be replayed and the action will be logged

    def undo_last(self, number_of_commands=1):

        """Redoes the last N commands"""

        commands = self._history[-number_of_commands:]

        for command in commands:

            # The below line will just undo the code, it will not be logged in history
            # self._commands[command[1]].undo()

            self.undo(command[1])  # The command will be undone and the action will be logged