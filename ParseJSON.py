import json

# Open Hypothesizer recording file
file = open('recording.json')
  
# Load JSON object as a dict
data = json.load(file)

# Example entry at index 0
# i = data[0]
# keys = i.keys()
# for key in keys:
#     if key == "stack":
#         for j in i[key]:
#             print("\n", j)
#     else:
#         print("\n", key, ":", i[key])

# Printing the entire dataset:
# for i in range(0, len(data)):
#     print("\nSection:", i + 1)
#     section = data[i]
#     keys = section.keys()
#     for key in keys:
#         if key == "stack":
#             for j in section[key]:
#                 print("\n", j)
#         else:
#             print("\n", key, ":", section[key])

# Getting all type values:
# typeValues = set(())
# for i in range(0, len(data)):
#     section = data[i]
#     keys = section.keys()
#     for key in keys:
#         if key == "type":
#             typeValues.add(section[key])
# print(typeValues)
#
# These are the following type values:
# {'codeCoverage', 'responseReceived', 'click', 'mouseout', 'keydown', 'childList', 'attributes', 'requestWillBeSent', 'mouseover'}

# Counting the number of each type:
# numCodeCov = 0
# numResRec = 0
# numClick = 0
# numMouseOut = 0
# numKeyDown = 0
# numChildList = 0
# numAttr = 0
# numReqWillBeSent = 0
# numMouseOver = 0
# for i in range(0, len(data)):
#     section = data[i]
#     keys = section.keys()
#     for key in keys:
#         if key == "type":
#             match section[key]:
#                 case "codeCoverage":
#                     numCodeCov += 1
#                 case "resopnseRecieved":
#                     numResRec += 1
#                 case "click":
#                     numClick += 1
#                 case "mouseout":
#                     numMouseOut += 1
#                 case "keydown":
#                     numKeyDown += 1
#                 case "childList":
#                     numChildList += 1
#                 case "attributes":
#                     numAttr += 1
#                 case "requestWillBeSent":
#                     numReqWillBeSent += 1
#                 case "mouseover":
#                     numMouseOver +=1
#
# Occurrences of each type (from run 1):
#     Code Coverage: 3930 
#     Click: 2 
#     Attributes: 9 
#     Child List: 2 
#     Key Down: 8 
#     Mouse Out: 4 
#     Mouse Over: 4 
#     Request Will Be Sent: 1 
#     Request Sent: 0

# Filtering out Code Coverage type:
# for i in range(0, len(data)):
#     section = data[i]
#     keys = section.keys()
#     for key in keys:
#         if key == "type":
#             # Ignore all 3000+ Code Coverage Sections
#             if section[key] == "codeCoverage":
#                 break;
#             else:
#                 print("\n", section[key], ":",  section)

# Looking at what exatly is in a Code Coverage object:
i = data[10]
keys = i.keys()
for key in keys:
    if key == "stack":
        for j in i[key]:
            print("\n", j)
    else:
        print("\n", key, ":", i[key])

# Close the file
file.close()