#!/usr/bin/env python


"""
Helpful utility functions
"""


# ############# #
# # Functions # #
# ############# #


def read_text_file(text_file_path: str, clear: bool = False) -> str:
    """
    Reads a text file and loads it in to memory
    :param text_file_path: Path to the text file
    :param clear: Should we sanitise the input and remove empty lines
    :return: File contents
    :raises: File not found error
    """

    # Check input types
    if not isinstance(text_file_path, str):
        raise TypeError("Path is not a string")
    if not isinstance(clear, bool):
        raise TypeError("Clear flag it not boolean")

    # Dynamic imports
    import os.path

    # Check if the file exists
    if not os.path.isfile(text_file_path):
        raise FileNotFoundError(f"{text_file_path} is not a file")

    # Load it in to memory
    file_contents = ""
    with open(text_file_path, 'r') as file:
        file_contents = file.read()

    # Check if we need to remove empty lines
    if clear:
        # Join all valid lines
        file_contents = os.linesep.join([line for line in file_contents.splitlines() if line])

    # Return the file contents
    return file_contents


def extract_info_text(text: str, separator: str = ',', clear: bool = False) -> list:
    """
    Extracts the information in a string by using separators
    :param text: Input text to be broken down
    :param separator: Field separator
    :param clear: Should we sanitise each field
    :return: Contents of all fields split
    """

    # Create the return list
    data = []

    # Iterate each line
    for line in text.splitlines():

        # Create list for the separator items
        field_items = []

        # Split using the separator
        for field in line.split(separator):

            # Should we sanitise the field
            if clear:
                field = field.strip()

            # Add it to list
            field_items.append(field)

        # Add all to data
        data.append(field_items)

    # Return our data
    return data