import os
from datetime import datetime


def find_file_by_serial(directories: list, serialNumbers: list, choice: str, batch_note: str) -> tuple:
    """
    Searches through file directories to find files associated with inputted serial numbers
    :param directories: List of directories to search
    :param serialNumbers: List of serial numbers to search for in the filename
    :param choice: Choose to sort from the oldest file or the newest file
    :param batch_note: User inputted note that goes in file name
    :return: Returns the oldest or newest files matching the serial numbers you input and the output filepath
    """
    # Filepath to location of matching files
    matchingFiles = []

    # Used to get the newest or oldest version. Value = date/time created, filepath
    outputFilenames = {}

    # List of filenames created to be used for the outputs
    outputFileList = []

    # Create the output filename based on user choice
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the script itself
    output_directory = os.path.join(script_dir, "../TipTilt Output")
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for serialNum in serialNumbers:
        serialFound = False
        for directory in directories:
            for filename in os.listdir(directory):
                if f"M3-F_{serialNum}_" in filename:
                    if serialNum not in outputFilenames:
                        outputFilenames[serialNum] = (os.path.getmtime(os.path.join(directory, filename)),
                                                      os.path.join(directory, filename))
                    else:
                        if choice == "n":
                            if outputFilenames[serialNum][0] <= os.path.getmtime(os.path.join(directory, filename)):
                                outputFilenames[serialNum] = ((os.path.getmtime(os.path.join(directory, filename)),
                                                               os.path.join(directory, filename)))
                        else:
                            if outputFilenames[serialNum][0] >= os.path.getmtime(os.path.join(directory, filename)):
                                outputFilenames[serialNum] = ((os.path.getmtime(os.path.join(directory, filename)),
                                                               os.path.join(directory, filename)))
        if serialNum in outputFilenames:
            serialFound = True
            if choice == 'o':
                outputFileList.append(f"oldest_test_output_{batch_note}_{serialNum}_"
                                  f"{current_datetime}.csv")
            else:
                outputFileList.append(f"newest_test_output_{batch_note}_{serialNum}_"
                                      f"{current_datetime}.csv")
        if not serialFound:
            print(f"Serial Number {serialNum} not found")

    # Create list of filepaths from final values in dictionary
    for filepath in outputFilenames.values():
        matchingFiles.append(filepath[1])

    if not matchingFiles:
        print("No matching files found")
        return None, None

    outputFilepath = []
    for i in range(len(outputFileList)):
        outputFilepath.append(os.path.join(output_directory, outputFileList[i]))

    # Return the oldest or most recent file based on user choice
    if choice == "o":
        return matchingFiles, outputFilepath
    else:
        return matchingFiles, outputFilepath
