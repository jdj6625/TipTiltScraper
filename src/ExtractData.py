import os


def extract_and_filter_data(input_filepath: list, output_filepath: list) -> bool:
    """
    Read the file line by line and extract data between "ZGC2" and "ZGC3"
    :param input_filepath:
    :param output_filepath:
    :return:
    """
    data_between_markers = []
    finishedExecution = True
    capture_data = False
    for i in range(len(input_filepath)):
        try:
            with open(input_filepath[i], 'r') as infile:
                for line in infile:
                    if 'ZGC2' in line:
                        capture_data = True
                        continue
                    if 'ZGC3' in line:
                        capture_data = False
                    if capture_data:
                        data_between_markers.append(line.strip())
        except FileNotFoundError:
            print(f"Invalid filename: {input_filepath}")

        # Filter out rows without a numerical value in the leftmost cell
        filtered_data = [line for line in data_between_markers if line.split(",")[0].replace('.', '', 1).isdigit()]

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_filepath[i]), exist_ok=True)

        # Write the filtered data to the output file
        try:
            with open(output_filepath[i], 'w') as outfile:
                for line in filtered_data:
                    outfile.write(line + "\n")
            print(f"Processed {input_filepath[i]} and wrote filtered data to {output_filepath[i]}")
        except:
            print("File could not be written")
            finishedExecution = False

    return finishedExecution
