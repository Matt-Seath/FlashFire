
class ASXLogger():
    
    log_base_dir = "logs/asx/"
    


    def write_to_logs(added=None, skipped=None, dropped=None):

        def write_log(log, filename, formatted=True):
            for entry in log:
                if not formatted:
                    entry = entry + ", "
                with open (filename, "a") as f:
                    f.write(entry)

            return

        if added:
            filename = "logs/added.log"
            write_log(added, filename)
        if skipped:
            filename = "logs/skipped.log"
            write_log(skipped, filename, formatted=False)
        if dropped:
            filename = "logs/dropped.log"
            write_log(dropped, filename)
        
        return


    def clear_logs():
        logs = ["dropped", "query", "added", "errors", "skipped"]
        for log in logs:
            with open(f"logs/{log}.log", "w") as f:
                f.truncate(0)

        return


    def print_stats(errors, skipped_symbols, dropped_columns):
        print("")
        print(f"Skipped Symbols: {str(skipped_symbols)}")
        print(f"Dropped Columns: {len(dropped_columns)}")
        print("")
        print(f"Task completed with {errors} error/s.")

        return