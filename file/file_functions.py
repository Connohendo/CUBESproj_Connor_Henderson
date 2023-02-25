from api.api_functions import get_wufoo_data


# Optional print function for testing
def print_file(file):
    with open(file) as f:
        print(f.read())


def fileCreation():
    # Create a dictionary obj through calling the wufoo api call function in api_functions.py
    output = get_wufoo_data()['Entries']

    # Create a file called Entries.txt using with open write
    # loop over each item's key value pair checking if the value is empty before filling the file
    with open("Entries.txt", "w") as outfile:
        for item in output:
            for key, value in item.items():
                if value == "":
                    continue
                else:
                    outfile.write(f"{key}:{value}\n")

    # print_file("Entries.txt")
