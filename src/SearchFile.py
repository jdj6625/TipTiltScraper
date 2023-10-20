import os
from datetime import datetime
import cmath


def find_file_by_serial(directories: list, serialNumbers: list, choice: str, batch_note: str) -> tuple:
    """
    Searches through file directories to find files associated with inputted serial numbers
    :param directories: List of directories to search
    :param serialNumbers: List of serial numbers to search for in the filename
    :param choice: Choose to sort from the oldest file or the newest file
    :param batch_note: User inputted note that goes in file name
    :return: Returns the oldest or newest files matching the serial numbers you input and the output filepath
    """
    matchingFiles = []
    outputFilenames = []
    # Create the output filename based on user choice
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the script itself
    output_directory = os.path.join(script_dir, "../TipTilt Output")
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    getTime = 0

    for serialNum in serialNumbers:
        serialFound = False
        for directory in directories:
            for filename in os.listdir(directory):
                if f"M3-F_{serialNum}_" in filename:
                    if not outputFilenames:
                        getTime = os.path.getmtime(os.path.join(directory, filename))

                    if choice == "oldest":
                        if os.path.getmtime(os.path.join(directory, filename)) >= getTime:
                            getTime = os.path.getmtime(os.path.join(directory, filename))
                            if serialFound:
                                outputFilenames.pop()
                                matchingFiles.pop()
                            matchingFiles.extend([os.path.join(directory, filename)])
                            outputFilenames.append(f"1st_test_output_{batch_note}_{serialNum}_{current_datetime}.csv")

                    else:
                        if os.path.getmtime(os.path.join(directory, filename)) <= getTime:
                            getTime = os.path.getmtime(os.path.join(directory, filename))
                            if serialFound:
                                outputFilenames.pop()
                                matchingFiles.pop()
                            matchingFiles.extend([os.path.join(directory, filename)])
                            outputFilenames.append(f"most_recent_test_output_{batch_note}_{serialNum}_"
                                                   f"{current_datetime}.csv")

                    serialFound = True
        if not serialFound:
            print(f"Serial Number {serialNum} not found")
    if not matchingFiles:
        print("No matching files found")
        return None, None

    # Sort files by their modification time
    matchingFiles.sort(key=lambda x: os.path.getmtime(x))

    outputFilepath = []
    for i in range(len(outputFilenames)):
        outputFilepath.append(os.path.join(output_directory, outputFilenames[i]))
    #print(outputFilenames)

    # Return the oldest or most recent file based on user choice
    if choice == "oldest":
        return matchingFiles, outputFilepath
    else:
        return matchingFiles, outputFilepath
