from src.ExtractData import extract_and_filter_data
from SearchFile import find_file_by_serial

if __name__ == "__main__":
    directories = [
        "N:/Test Data/07034-3-0000 M3-F-1p8-1p5-M12-LQ/ScanData",
        "N:/Test Data/05516-3-0000 M3-F-1.8-1.5-M12/ScanData"
    ]

    serial_numbers = input("Enter the serial numbers (comma separated): ").split(',')
    batch_note = input("Enter a batch note: ").replace(" ",
                                                       "_")  # Replacing spaces with underscores for filename safety

    while True:
        choice = input(
            "Would you like to find the oldest or most recent files? (Enter 'oldest' or 'recent'): ").strip().lower()
        if choice in ["oldest", "recent"]:
            break
        else:
            print("Invalid choice. Please enter either 'oldest' or 'recent'.")

    # for serial in serial_numbers:
    # serial = serial.strip()  # Remove any extra spaces
    input_filepath, output_filepath = find_file_by_serial(directories, serial_numbers, choice, batch_note)

    if input_filepath:
        extract_and_filter_data(input_filepath, output_filepath)
