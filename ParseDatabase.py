import json
import sys

# Open Hypotheses DB
file = open("hypotheses.json")
# Load JSON object as a dict
data = json.load(file)


# allEvidence:
# Input: None
# Output: Prints all evidence objects in the JSON.
def allEvidence():
    evidence = data["evidence"]
    keys = evidence.keys()

    for key in keys:
        print("\n", key, ":", evidence[key])


# allHypotheses:
# Input: None
# Output: Prints all hypotheses objects in the JSON.
def allHypotheses():
    hypotheses = data["hypotheses"]

    for i in range(0, len(hypotheses)):
        print(hypotheses[i]["id"], ":\n")


# exampleHypothesis:
# Input: String fileName
# Output: Prints an example hypothesis in the JSON.
def exampleHypothesis():
    print(data)


# Close the file
file.close()

# This allows for calling a specific funtion from the command line.
# Usage: python3 ParseHypotheses.py functionName
if __name__ == "__main__":
    if len(sys.argv) > 1:
        globals()[sys.argv[1]]()
