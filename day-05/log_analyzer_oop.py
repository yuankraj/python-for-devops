class LogAnalyzer:

    def __init__(self, log_file):

        self.log_file = log_file

        self.counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "UNKNOWN": 0
        }

    def read_logs(self):

        try:
            with open(self.log_file, "r") as file:
                return file.readlines()

        except FileNotFoundError:
            print("Log file not found!")
            return []

    def analyze_logs(self, logs):

        for log in logs:

            if "INFO" in log:
                self.counts["INFO"] += 1

            elif "WARNING" in log:
                self.counts["WARNING"] += 1

            elif "ERROR" in log:
                self.counts["ERROR"] += 1

            else:
                self.counts["UNKNOWN"] += 1

        return self.counts

    def show_summary(self):

        print("\n===== Log Summary =====")

        for level, count in self.counts.items():
            print(f"{level}: {count}")


def main():

    analyzer = LogAnalyzer("app.log")

    logs = analyzer.read_logs()

    if not logs:
        print("No logs found!")
        return

    analyzer.analyze_logs(logs)

    analyzer.show_summary()


if __name__ == "__main__":
    main()
