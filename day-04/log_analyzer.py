try:
    file = open("app.log", "r")

    logs = file.readlines()

    info = 0
    warning = 0
    error = 0

    for log in logs:

        if "INFO" in log:
            info += 1

        elif "WARNING" in log:
            warning += 1

        elif "ERROR" in log:
            error += 1

    print("\n===== Log Summary =====")
    print("INFO   :", info)
    print("WARNING:", warning)
    print("ERROR  :", error)

    output = open("log_summary.txt", "w")

    output.write("===== Log Summary =====\n")
    output.write(f"INFO   : {info}\n")
    output.write(f"WARNING: {warning}\n")
    output.write(f"ERROR  : {error}\n")

    output.close()
    file.close()

    print("\nSummary saved in log_summary.txt")

except FileNotFoundError:
    print("app.log file not found!")
