#!/usr/bin/env python


"""
Main project file
"""

# ########### #
# # Imports # #
# ########### #


import os.path
import inspect

# ################## #
# # Initialisation # #
# ################## #


# General configuration
import config

# Import all the utils
import utils


# ############# #
# # Functions # #
# ############# #


def read_integer_between_numbers(prompt, mini, maximum):
    """
    Continuously prompt the user to enter an integer within a specified range.

    This function asks the user to enter an integer until they provide a value that is 
    within the inclusive range defined by `mini` and `maximum`. If the user inputs a 
    non-integer value, an error message is shown, and the prompt repeats.

    Parameters:
    - prompt (str): The message displayed to the user when asking for input.
    - mini (int): The minimum allowable integer value (inclusive).
    - maximum (int): The maximum allowable integer value (inclusive).

    Returns:
    - int: The valid integer entered by the user, guaranteed to be within the specified range.

    Error Handling:
    - Prints an error message if the input is not an integer.
    - Prints an error message if the input is outside the specified range.
    """
    while True:
        try:
            users_input = int(input(prompt))
            if mini <= users_input <= maximum:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - number only, please")


def read_nonempty_string(prompt: str) -> str:
    """
    Read a string from the user and make sure it is not empty
    :param prompt: The prompt to be shown to the user
    :return: Users input
    """

    # Check if the prompt is valid
    if not isinstance(prompt, str):
        raise TypeError("Prompt is not string")

    # Loop until the user inputs a valid string
    for _ in range(config.LOOP_LIMIT):

        # Get users input
        users_input = input(prompt)

        # Check user input
        if users_input.isalpha():
            break
        else:
            print("Invalid input")

    # If our for ended normally
    else:
        raise RecursionError

    # Return the users input
    return users_input


def read_integer(prompt):
    """
    Prompt the user to enter a non-negative integer and continue retrying until valid input is provided.

    This function repeatedly prompts the user for an integer input using the specified prompt message.
    It accepts only non-negative integers (greater than or equal to 0). If the user enters a non-integer
    value or a negative integer, the function catches the ValueError and prints an error message,
    then prompts the user again.

    Args:
        prompt (str): The message to display when asking the user for input.

    Returns:
        int: The first valid non-negative integer input from the user.
    """
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry -numbers only please")


def runners_data() -> (list, list):
    """
    Gets information about runner names and IDs
    :return: List of runner names & list of runner IDs, matching in length and index
    """

    # Use our utils to parse the files
    file_data = utils.read_text_file(os.path.join(config.ASSETS_FOLDER, "runners.txt"))

    # Extract the data from it
    extracted_data = utils.extract_info_text(file_data, separator=',')

    # Extract the data into two lists
    runners_name = [runner[0] for runner in extracted_data]
    runners_id = [runner[1] for runner in extracted_data]

    # Return the data
    return runners_name, runners_id


def race_results(races_location):
    """
    Display a menu of race venues, prompt the user to select one, and return the 
    race results for the selected venue.

  
    Parameters: races_location (list of str): A list of race venue names.

    Returns:
    : id (list of str): A list of runner IDs for the venue.
    : time_taken (list of int): A list of times for each runner at the venue.
    : venue (str): The name of the race venue.

    Dependencies:
     Calls 'read_integer_between_numbers' to validate user input.
     Calls 'reading_race_results' to get race results for the venue.

    """
    for i in range(len(races_location)):
        print(f"{i + 1}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    runner_id, time_taken = reading_race_results(venue)
    return runner_id, time_taken, venue


def race_venues() -> ([str], [str]):
    """
    Read race venue locations from a file and return them as a list.

    This function opens the file "races.txt", reads each line, removes any surrounding 
    whitespace (such as newline characters) along with corresponding times, and stores each line in a list. 
    The list of race locations is then returned.

    Returns:
    - list of str: A list containing each race venue location from the file as a separate string.

    """

    # Extract information from the file
    file_data = utils.read_text_file(os.path.join(config.ASSETS_FOLDER, "races.txt"))
    extracted_data = utils.extract_info_text(file_data, separator=',')

    # Extract into their own sets
    places = [each[0] for each in extracted_data]
    qualifies = [each[1] for each in extracted_data]

    # Return then
    return places, qualifies


def winner_of_race(runner_id, time_taken):
    """
    Determines the winner of a race based on the shortest time taken, ignoring times of 0.

    Parameters:
    ----------
    id : list
        A list of participant IDs.
    time_taken : list
        A list of finish times. 

    Returns:
    -------
    str
        The ID with the shortest completion time, excluding any times of 0.
    """
    # Create lists of id's and finish times, excluding times of zero
    valid_ids = []
    valid_times = []

    for i in range(len(time_taken)):
        if time_taken[i] > 0:
            valid_ids.append(runner_id[i])
            valid_times.append(time_taken[i])

    # If no participants, return an empty string
    if not valid_ids:
        return ""

    # Find the index of the smallest time in valid_times
    min_time_index = valid_times.index(min(valid_times))

    # Return the ID of the smallest time
    return valid_ids[min_time_index]


def display_races(runner_id, time_taken, venue, fastest_runner):
    """
    :param runner_id: ID of a runner
    :param time_taken: Time it took a runner to complete the race
    :param venue: Area where the race took place
    :param fastest_runner: Fastest runner that partook in the race.
    :return: nothing
    """
    minute = 60
    print(f"Results for {venue}")
    print(f"=" * 37)
    minutes = []
    seconds = []
    for i in range(len(time_taken)):
        minutes.append(time_taken[i] // minute)
        seconds.append(time_taken[i] % minute)
    for i in range(len(runner_id)):
        print(f"{runner_id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"{fastest_runner} won the race.")


def users_venue(races_location: [str], races_qualify: [str], runners_id: [str]) -> None:
    """
    Adds a runner to the venue

    :param races_location: The list of locations of races
    :param races_qualify: Qualification times
    :param runners_id: The list of ids of the runners
    :return: Nothing
    """

    # Check the input
    if not isinstance(races_location, list) or not isinstance(runners_id, list) or not isinstance(races_qualify, list):
        raise ValueError("The input must be a list")
    if len(races_location) <= 0 or len(runners_id) <= 0 or len(races_qualify) <= 0:
        raise ValueError("List must not be empty")
    if len(races_location) != len(races_qualify):
        raise ValueError("Lists must be of the same length")
    if not all(isinstance(each, str) for each in races_location + races_qualify + runners_id):
        raise ValueError("All values inside list must be strings")

    # Gets the location that we will add the user
    for _ in range(config.LOOP_LIMIT):
        user_location = read_nonempty_string("Where will the new race take place? ").lower()
        # Check if the location is valid
        if user_location not in races_location:
            break
        else:
            print("There was already a race recorded for this place")
    else:
        raise RecursionError

    # Update the list of locations
    races_location.append(user_location)

    # Open the file
    with utils.open_text_file_write(os.path.join(config.INFO_FOLDER, f"{user_location.lower()}.txt")) as file:

        # Create a sum for all the times
        all_times = 0

        # Iterate all the runners
        for runner in runners_id:

            # Get the time for the runner
            time_taken_for_runner = read_integer(f"Time for {runner} >> ")

            # Accumulate all the times
            all_times += time_taken_for_runner

            # Write it to the file
            print(runner, time_taken_for_runner, sep=',', file=file)

        # Calculate the mean times
        mean_time = all_times / len(runners_id)
        # Transform it to minutes
        mean_minutes = round((mean_time / config.SECONDS_IN_MINUTES) * 2) / 2
        # Add it to the list of times
        races_qualify.append(str(mean_minutes))


def updating_races_file(races_location: [str], races_qualifies: [str]) -> None:
    """
    Updates the races file with the new races information

    :param races_location: New locations of the races
    :param races_qualifies: Qualifying times for the
    :return: Nothing
    """

    # Check the input
    if not isinstance(races_location, list) or not isinstance(races_qualifies, list):
        raise ValueError("The input must be a list")
    if len(races_location) <= 0 or len(races_qualifies) <= 0:
        raise ValueError("List must not be empty")
    if len(races_location) != len(races_qualifies):
        raise ValueError("Lists must be of the same length")
    if not all(isinstance(each, str) for each in races_location + races_qualifies):
        raise ValueError("All values inside list must be strings")

    # Open the file so that we can write to it
    with utils.open_text_file_write(os.path.join(config.ASSETS_FOLDER, "races.txt"), append=False) as file:
        # Iterate the lists
        for location, qualify in zip(races_location, races_qualifies):
            print(location.capitalize(), qualify, sep=',', file=file)


def competitors_by_county(name, runner_id):
    """
    Prints a list of competitors organized by county code, sorted alphabetically by name.

    Parameters:
    name (list of str): A list of competitor names.
    id (list of str): A list of competitor IDs corresponding to each name.

    Returns: None
    """
    # Check that name and id lists have the same length
    if len(name) != len(runner_id):
        print("Error: Name and ID lists must have the same length.")
        return
    
    # Create a dictionary to store competitors by their county code
    competitors_by_code = {}

    # Loop through the names and IDs to separate competitors by county code
    for i in range(len(name)):
        county_code = runner_id[i].split('-')[0]  # Get the county code
        if county_code not in competitors_by_code:
            competitors_by_code[county_code] = []
        competitors_by_code[county_code].append((name[i], runner_id[i]))

    # Sort competitors within each county by name
    for county_code in competitors_by_code:
        competitors_by_code[county_code].sort()  

    # Sort the county codes alphabetically
    sorted_county_codes = sorted(competitors_by_code.keys())

    # Print out the results
    for county_code in sorted_county_codes:
        print(f"{county_code} runners")
        print("=" * 20)
        for competitor in competitors_by_code[county_code]:
            print(f"{competitor[0]} ({competitor[1]})")  
        print() 


def reading_race_results(location):
    """
    Reads and processes race results from a text file corresponding to a specific location.

    :param location: name of the text file to use
    :return: runner_id (list of str): A list of runner IDs extracted from the file.
           : time_taken (list of int): A list of times taken by each runner.
    
    """
    file_data = utils.read_text_file(os.path.join(config.INFO_FOLDER, f"{location.lower()}.txt"))
    extracted_data = utils.extract_info_text(file_data, separator=',')

# Validate and ensure all rows are properly formatted
    for runner in extracted_data:
        if len(runner) < 2 or not runner[0] or not runner[1].isdigit():
            raise ValueError(f"Invalid data format: {runner}")

    runner_id = [runner[0] for runner in extracted_data]
    time_taken = [int(runner[1]) for runner in extracted_data]
    return runner_id, time_taken


def reading_race_results_of_relevant_runner(location: str, runner_id_in: str) -> int or None:
    """
    Reads the race results of the relevant runner

    :param location: Location we will read the information from
    :param runner_id_in: ID of the runner that we want information of
    :return: The time of the runner given
    """

    # Check the inputs
    if not isinstance(location, str) or not isinstance(runner_id_in, str):
        raise ValueError("Input needs to be string")

    # Check if the given location is valid
    file_location = os.path.join(config.INFO_FOLDER, f"{location.lower()}.txt")
    if not os.path.isfile(file_location):
        raise ValueError("The location does not exist")

    # Extract the runner data
    file_data = utils.read_text_file(file_location)
    extracted_data = utils.extract_info_text(file_data, separator=',')

    # Split the information into readable format
    runner_id = [runner[0] for runner in extracted_data]
    time_taken = [runner[1] for runner in extracted_data]

    # Check if the user is present
    if runner_id_in not in runner_id:
        return None

    # Find the runners time
    common_index = runner_id.index(runner_id_in)

    # Return the time
    return int(time_taken[common_index])


def displaying_winners_of_each_race(races_location):
    """
    Displays the winners and losers of each race
    :param races_location: The list of locations for each race
    :return: None
    """

    # Check the input
    if not isinstance(races_location, list):
        raise ValueError("The input must be a list")
    if len(races_location) <= 0:
        raise ValueError("List must not be empty")
    if not all(isinstance(each, str) for each in races_location):
        raise ValueError("All values inside list must be strings")

    # Print table
    print(f"{'Venue' : <{config.TABLE_SIZE // 2}}{'Winner' : >{config.TABLE_SIZE // 2}}")
    print("=" * config.TABLE_SIZE)

    # Iterate the races
    for race in races_location:

        # Get the race results
        runner_id, time_taken = reading_race_results(race)

        # Get the winner of the race
        fastest_runner = winner_of_race(runner_id, time_taken)

        # Print the entry in the table
        print(f"{race : <{config.TABLE_SIZE // 2}}{fastest_runner : >{config.TABLE_SIZE // 2}}")


def relevant_runner_info(runners_name: [str], runners_id: [str]) -> (str, str):
    """
    Returns the information of a selected runner

    :param runners_name: Names of the runners
    :param runners_id: IDs of the runners
    :return: The runner name and runner ID
    """

    # Input checking
    if not isinstance(runners_name, list) or not isinstance(runners_id, list):
        raise ValueError("Input should be a list")
    if len(runners_name) != len(runners_id):
        raise ValueError("Both lists should have the same size")
    if len(runners_name) <= 0:
        raise ValueError("Input lists cannot be empty")
    if not all(isinstance(each, str) for each in runners_name + runners_id):
        raise ValueError("Item in list is not a string")

    # Iterate all the runners and create list
    for index in range(len(runners_name)):
        print(f"{index + 1}: {runners_name[index]}")

    # Get the users input
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))

    # Extract the data from the lists
    runner = runners_name[user_input - 1]
    chosen_id = runners_id[user_input - 1]

    # Return the data
    return runner, chosen_id


def convert_time_to_minutes_and_seconds(time_taken: int):
    """
    Take input from user
    Get value of how many seconds in a minute from a file
    This function takes an input str value and divides it by number of minutes and seconds
    It will convert a standard number for example 130 to 2 minutes and 10 seconds.

    :param time_taken: amount of time something took

    Return:
        When process finish display result to user and store it in minutes_taken and seconds_taken
    """
    minutes_taken = time_taken // config.SECONDS_IN_MINUTES
    seconds_taken = time_taken % config.SECONDS_IN_MINUTES
    return minutes_taken, seconds_taken


def sorting_where_runner_came_in_race(location, time):
    """
    Determine position of runner based on time taken and total number of runners
    The function reads a file for a certain race location that has each runner name and time
    separated by a comma. The function then calucates the position of that time in the sorted lists and returns the
    position and total number of runners.

    :param location: File that contains race results
    :param time: time of runner to find position for

    Return:
        - postion of each other by rank. for example 1 is fastest 2 is second and so on.
        - total number of runners in race
        For example if it returns 1, 5. That means that persona came first out of 5 people.


    """

    lines = utils.read_text_file(os.path.join(config.INFO_FOLDER, f"{location.lower()}.txt")).splitlines()
    time_taken = []
    for line in lines:
        split_line = line.strip().split(",")
        t = int(split_line[1])
        time_taken.append(t)
    time_taken.sort()
    return time_taken.index(int(time)) + 1, len(lines)


def displaying_race_times_one_competitor(races_location: [str], runner: str, runner_id: str) -> None:
    """
    Display the race times for one competitor only

    :param races_location: All the race locations
    :param runner: Runner name
    :param runner_id: ID of the runner
    :return: Nothing
    """

    print(f"{runner} ({runner_id})")
    print(f"-" * 35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], runner_id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, runners_id, runners_name):
    """
    Returns the name of the winner by matching fastest runners id to runner names

    :param fastest_runner: id of runner that won
    :param runners_name: Names of the runners
    :param runners_id: IDs of the runners
    :return: The name of the runner that won and stored it in namer_of_winner
    """
    for i in range(len(runners_id)):
        if fastest_runner == runners_id[i]:
            name_of_winner = runners_name[i]
            return name_of_winner
    return None


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        runner_id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(runner_id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")


# ######## #
# # Main # #
# ######## #


def main():
    """
    Main function to run the main logic
    """

    # Get data
    races_location, races_qualifies = race_venues()
    runners_name, runners_id = runners_data()

    # Create the menu
    current_menu = inspect.cleandoc(
        f"""1. Show the results for a race
            2. Add results for a race
            3. Show all competitors by county
            4. Show the winner of each race
            5. Show all the race times for one competitor
            6. Show all competitors who have won a race
            7. Quit
            {config.INPUT_MARKER} """)

    # Get the menu input
    input_menu = read_integer_between_numbers(current_menu, 1, 7)
    print()

    # Menu selection
    for _ in range(config.LOOP_LIMIT):

        # Possible inputs for the menu
        match input_menu:

            case 1:
                ids, time_taken, venue = race_results(races_location)
                fastest_runner = winner_of_race(ids, time_taken)
                display_races(ids, time_taken, venue, fastest_runner)

            case 2:
                users_venue(races_location, races_qualifies, runners_id)
                updating_races_file(races_location, races_qualifies)

            case 3:
                competitors_by_county(runners_name, runners_id)

            case 4:
                displaying_winners_of_each_race(races_location)

            case 5:
                runner, ids = relevant_runner_info(runners_name, runners_id)
                displaying_race_times_one_competitor(races_location, runner, ids)

            case 6:
                displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)

            case 7:
                break

            case _:
                continue

        # Always ask for input
        print()
        input_menu = read_integer_between_numbers(current_menu, 1, 7)
        print()

    # The loop went on for too long
    else:
        raise RecursionError


if __name__ == "__main__":
    main()
