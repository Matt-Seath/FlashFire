from datetime import datetime
import inspect




class Logger():

    log_base_dir = "logs/asx/"
    logs = []


    def __init__(self, *args) -> None:
        self.add_logs(*args)


    def __str__(self):
        
        return str("hi")


    def add_logs(self, *args) -> None:

        for arg in range(len(args)):
            self.logs.append(args[arg])
    


    def entry(self, log_name, *entries) -> None:
         for log in range(len(self.logs)):
            if log_name == self.logs[log]:
                for entry in entries:
                    self.logs[log].append(entry)
       


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
        
        return


    def write_log(self, log, filename, formatted=True):
        for entry in log:
            if not formatted:
                entry = entry + ", "
            with open (filename, "a") as f:
                f.write(entry)

        return


    def clear_logs(self):
        logs = ["dropped", "query", "added", "errors", "skipped"]
        for log in logs:
            with open(f"logs/{log}.log", "w") as f:
                f.truncate(0)

        return


    def print_stats(self, errors, skipped_symbols, dropped_columns):
        print("")
        print(f"Skipped Symbols: {str(skipped_symbols)}")
        print(f"Dropped Columns: {len(dropped_columns)}")
        print("")
        print(f"Task completed with {errors} error/s.")

        return
    

    class Log():

        name = ""
        entries = []

        def __init__(self, args) -> None:
            self.name = args

        def __str__(self):
            return str(self.name)
        
        def append(self, *args) -> None:
            for arg in args:
                self.entries.append(arg)



test_logger = Logger("added", "dropped")
stuff = ["qw", "df", "sd"]
test_logger.entry("added", stuff)

print(test_logger)
