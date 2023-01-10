from pathlib import Path


class TempLogger():

    log_base_dir = "logs/"
    logs = None

    def __init__(self, *args) -> None:
        if self.logs == None:
            self.logs = set()
        self.add_logs(*args)

    def __str__(self):
        logs_str = set()
        for log in self.logs:
            logs_str.add(f"{log.name}, {len(log.data)}")

        return str(logs_str)

    def add_logs(self, *args) -> None:
        for arg in range(len(args)):
            self.logs.add(self.Log(args[arg]))

    def entry(self, log_name, *entries) -> None:
        for log in self.logs:
            if log_name == log.name:
                for entry in entries:
                    log.add_entry(entry)

    def write_to_files(self, *list_of_logs, all=False):
        for log in self.logs:
            if log.name in list_of_logs or all:
                self.__write_log(log)

    def __write_log(self, log):
        Path(self.log_base_dir).mkdir(parents=True, exist_ok=True)
        filename = f"{self.log_base_dir}{log.name}.log"
        for entry in log.data:
            entry = entry + ", "
            with open(filename, "a") as f:
                f.write(entry)

    def clear_logs(self, *list_of_logs, all=False):
        for log in self.logs:
            if log.name in list_of_logs or all:
                with open(f"{self.log_base_dir}{log.name}.log", "w") as f:
                    f.truncate(0)

    def edit(self, name):
        for log in self.logs:
            if log.name == name:
                return log

    def print_stats(self):
        print("")
        for log in self.logs:
            if log.text and log.stats:
                print(f"{log.text}: {log.stats}")

    class Log():

        name = ""
        data = None
        stats = None
        text = None

        def __init__(self, name) -> None:
            if self.data == None:
                self.data = []
            self.name = name

        def __str__(self):
            return f"{str(self.name)} = {str(self.data)}"

        def add_entry(self, *args) -> None:
            for arg in args:
                self.data.append(arg)

        def add_text(self, text=None, stats=None):
            if text:
                self.text = text
            if stats == "total":
                self.stats = str(len(self.data))
            if stats == "data":
                self.stats = str(self.data)
