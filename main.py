from health_monitor import (
    check_endpoint,
    get_recent_reports,
    save_report,
)


def display_record(record):
    print(f"\nURL: {record['url']}")
    print(f"Result: {record['result']}")
    print(f"HTTP status: {record['status_code'] or 'N/A'}")
    print(f"Response time: {record['response_ms']} ms")

    if record["error"]:
        print(f"Error: {record['error']}")

    print(f"Checked at: {record['checked_at']}")


def main():
    while True:
        print("\n===== API HEALTH MONITOR =====")
        print("1. Check a URL")
        print("2. View recent reports")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            url = input("Enter website/API URL: ").strip()

            try:
                record = check_endpoint(url)
                display_record(record)
                save_report(record)
                print("\nReport saved.")

            except (ValueError, OSError) as error:
                print(f"\nError: {error}")

        elif choice == "2":
            records = get_recent_reports()

            if not records:
                print("\nNo reports found yet.")
            else:
                for record in records:
                    display_record(record)
                    print("-" * 35)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()