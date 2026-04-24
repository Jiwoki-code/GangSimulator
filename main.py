import json
import os

# Load raw data from JSONS
names_data = []
with open("data/names.JSON") as json_file:
    names_data = json.load(json_file)

# Main

def main():
    os.system("clear")
    print("Main section started")
    print("Loaded names : ")
    print(names_data)

if __name__ == "__main__":
    main()