import json
import sys


# exampleHypothesis:
# Input: String fileName
# Output: Prints an example hypothesis in the JSON.
def exampleHypothesis():
    # Open Hypotheses DB File
    file = open("hypotheses.json")
    # Load JSON object as a dict
    data = json.load(file)

    print(data)

    # Close the file
    file.close()


# This allows for calling a specific funtion from the command line.
# Usage: python3 ParseHypotheses.py functionName
if __name__ == "__main__":
    if len(sys.argv) > 1:
        globals()[sys.argv[1]]()
