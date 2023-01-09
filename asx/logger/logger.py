from datetime import datetime
import inspect




class Logger():
    log_base_dir = "logs/asx/"
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
       

    def write_to_logs(self, added=None, skipped=None, dropped=None):
        if added:
            filename = "logs/added.log"
            self.write_log(added, filename)
        if skipped:
            filename = "logs/skipped.log"
            self.write_log(skipped, filename, formatted=False)
        if dropped:
            filename = "logs/dropped.log"
            self.write_log(dropped, filename)


    def write_log(self, log, filename, formatted=True):
        for entry in log:
            if not formatted:
                entry = entry + ", "
            with open (filename, "a") as f:
                f.write(entry)


    def clear_logs(self):
        logs = ["dropped", "query", "added", "errors", "skipped"]
        for log in logs:
            with open(f"logs/{log}.log", "w") as f:
                f.truncate(0)


    def print_stats(self, errors, skipped_symbols, dropped_columns):
        print("")
        print(f"Skipped Symbols: {str(skipped_symbols)}")
        print(f"Dropped Columns: {len(dropped_columns)}")
        print("")
        print(f"Task completed with {errors} error/s.")


    class Log():
        name = ""
        data = None


        def __init__(self, args) -> None:
            if self.data == None:
                self.data = []
            self.name = args


        def __str__(self):
            return f"{str(self.name)} = {str(self.data)}"


        def add_entry(self, *args) -> None:
            for arg in args:
                self.data.append(arg)



test_logger = Logger("added", "dropped")
stuff = ["qw", "df", "sd"]
test_logger.entry("added", *stuff)

print(test_logger)

test_logger.add_logs("skipped")
print(test_logger)

test_logger.entry("skipped", "sdf")
print(test_logger)

test = Logger("new", "old")
print(test_logger.)