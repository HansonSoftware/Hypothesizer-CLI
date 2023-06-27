import json
import sys

# Open Hypotheses DB
file = open("hypotheses.json")
# Load JSON object as a dict
data = json.load(file)


# ================================================================================
# ============================= EVIDENCE PARSING =================================
# ================================================================================


# allEvidence:
# Input: None
# Output: Prints all evidence objects in the DB.
def allEvidence():
    evidence = data["evidence"]
    keys = evidence.keys()
    for key in keys:
        if key == "API_calls":
            print(key)
            print(len(evidence[key]))
        if key == "DOM_events":
            print(key)
            print(len(evidence[key]))
        if key == "Network_events":
            networkEvents = evidence[key]
            networkEventCount = 1
            print("\n%s:" % key)
            for i in range(0, len(networkEvents)):
                networkEventKeys = networkEvents[i].keys()
                print("\tNetwork Event %d." % networkEventCount)
                for networkEventKey in networkEventKeys:
                    if networkEventKey == "objectShape":
                        print("\t\tobjectShape:")
                        objKeys = networkEvents[i][networkEventKey].keys()
                        for objKey in objKeys:
                            print(
                                "\t\t\t%s: %s"
                                % (objKey, networkEvents[i][networkEventKey][objKey])
                            )
                        continue
                    print(
                        "\t\t%s: %s"
                        % (networkEventKey, networkEvents[i][networkEventKey])
                    )
                networkEventCount = networkEventCount + 1


# networkEvents:
# Input: None
# Output: Prints all Network Event evidence objects in the DB.
def networkEvents():
    evidence = data["evidence"]
    keys = evidence.keys()
    for key in keys:
        if key == "Network_events":
            networkEvents = evidence[key]
            networkEventCount = 1
            print("\n%s:" % key)
            for i in range(0, len(networkEvents)):
                networkEventKeys = networkEvents[i].keys()
                print("\tNetwork Event %d." % networkEventCount)
                for networkEventKey in networkEventKeys:
                    if networkEventKey == "objectShape":
                        print("\t\tobjectShape:")
                        objKeys = networkEvents[i][networkEventKey].keys()
                        for objKey in objKeys:
                            print(
                                "\t\t\t%s: %s"
                                % (objKey, networkEvents[i][networkEventKey][objKey])
                            )
                        continue
                    print(
                        "\t\t%s: %s"
                        % (networkEventKey, networkEvents[i][networkEventKey])
                    )
                networkEventCount = networkEventCount + 1


# ================================================================================
# ============================= HYPOTHESES PARSING ===============================
# ================================================================================


# allHypotheses:
# Input: None
# Output: Prints all hypotheses objects in the JSON.
def allHypotheses():
    hypotheses = data["hypotheses"]
    for i in range(0, len(hypotheses)):
        print(
            "--------------------------------------------------------------------------------\n"
        )
        print("%s:\n" % hypotheses[i]["id"].replace("_", " "))
        keys = hypotheses[i].keys()
        for key in keys:
            section = hypotheses[i][key]
            if key == "tags":
                print("Tags:")
                tagCount = 1
                for tag in section:
                    print("\t%d." % tagCount, tag)
                    tagCount = tagCount + 1
                continue
            if key == "evidence":
                print("Related Evidence:")
                count = 1
                for evidence in section:
                    print("\tEvidence %d." % count)
                    evidenceKeys = evidence.keys()
                    for evidenceKey in evidenceKeys:
                        if evidenceKey == "HowToFix":
                            print("\t\t%s:" % evidenceKey)
                            steps = evidence[evidenceKey]["steps"]
                            print("\t\tSteps:")
                            stepCount = 1
                            for j in range(0, len(steps)):
                                stepKeys = steps[j].keys()
                                print("\t\t\tStep %d." % stepCount)
                                for stepKey in stepKeys:
                                    print(
                                        "\t\t\t\t%s: %s" % (stepKey, steps[j][stepKey])
                                    )
                                stepCount = stepCount + 1
                            continue
                        print("\t\t%s:" % evidenceKey, evidence[evidenceKey])
                    count = count + 1
                continue
            print("%s:" % key, section)


# exampleHypothesis:
# Input: String fileName
# Output: Prints the first hypothesis in the DB.
def exampleHypothesis():
    hypothesis = data["hypotheses"][0]
    print("%s:\n" % hypothesis["id"].replace("_", " "))
    keys = hypothesis.keys()
    for key in keys:
        section = hypothesis[key]
        if key == "tags":
            print("Tags:")
            tagCount = 1
            for tag in section:
                print("\t%d." % tagCount, tag)
                tagCount = tagCount + 1
            continue
        if key == "evidence":
            print("Related Evidence:")
            count = 1
            for evidence in section:
                print("\tEvidence %d." % count)
                evidenceKeys = evidence.keys()
                for evidenceKey in evidenceKeys:
                    if evidenceKey == "HowToFix":
                        print("\t\t%s:" % evidenceKey)
                        steps = evidence[evidenceKey]["steps"]
                        print("\t\tSteps:")
                        stepCount = 1
                        for j in range(0, len(steps)):
                            stepKeys = steps[j].keys()
                            print("\t\t\tStep %d." % stepCount)
                            for stepKey in stepKeys:
                                print("\t\t\t\t%s: %s" % (stepKey, steps[j][stepKey]))
                            stepCount = stepCount + 1
                        continue
                    print("\t\t%s:" % evidenceKey, evidence[evidenceKey])
                count = count + 1
            continue
        print("%s:" % key, section)


# getHypothesisById:
# Input: Integer id
# Output: Prints the hypothesis at id
def getHypothesisById(id):
    found = False
    hypotheses = data["hypotheses"]
    for i in range(0, len(hypotheses)):
        hypothesisId = hypotheses[i]["id"].replace("_", " ").split()
        for token in hypothesisId:
            if token.isnumeric():
                if token == id:
                    found = True
                    hypothesis = data["hypotheses"][i]
                    print("%s:\n" % hypothesis["id"].replace("_", " "))
                    keys = hypothesis.keys()
                    for key in keys:
                        section = hypothesis[key]
                        if key == "tags":
                            print("Tags:")
                            tagCount = 1
                            for tag in section:
                                print("\t%d." % tagCount, tag)
                                tagCount = tagCount + 1
                            continue
                        if key == "evidence":
                            print("Related Evidence:")
                            count = 1
                            for evidence in section:
                                print("\tEvidence %d." % count)
                                evidenceKeys = evidence.keys()
                                for evidenceKey in evidenceKeys:
                                    if evidenceKey == "HowToFix":
                                        print("\t\t%s:" % evidenceKey)
                                        steps = evidence[evidenceKey]["steps"]
                                        print("\t\tSteps:")
                                        stepCount = 1
                                        for j in range(0, len(steps)):
                                            stepKeys = steps[j].keys()
                                            print("\t\t\tStep %d." % stepCount)
                                            for stepKey in stepKeys:
                                                print(
                                                    "\t\t\t\t%s: %s"
                                                    % (stepKey, steps[j][stepKey])
                                                )
                                            stepCount = stepCount + 1
                                        continue
                                    print(
                                        "\t\t%s:" % evidenceKey, evidence[evidenceKey]
                                    )
                                count = count + 1
                            continue
                        print("%s:" % key, section)
    if found == False:
        print("Sorry, the hypothesis id you entered is not in the database yet.")


# Close the file
file.close()

# This allows for calling a specific funtion from the command line.
# Usage: python3 ParseHypotheses.py functionName
if __name__ == "__main__":
    if len(sys.argv) == 2:
        globals()[sys.argv[1]]()
    if len(sys.argv) == 3:
        globals()[sys.argv[1]](sys.argv[2])
