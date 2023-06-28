# Hypothesizer-CLI

A Command Line Interface for interacting with OpenAI's API. There is additional functionality built on top to support [Hypothesizer](https://github.com/Alaboudi1/Hypothesizer-Debugger).

# Getting Started With OpenAI:

1.  Clone the repo and add a .env file with your OpenAI API Key.

    Example:
    .env should contain

    ```
    OPENAI_KEY = abc123secretkey
    ```

    You want to make sure this key is not shared.

2.  cd into OpenAI-Walkthrough and run TestAPI.py from your terminal to make sure you're all set.

3.  TODO: Create Walkthrough

# Using the Parsers

## ParseRecordings.py:

Usage:
`python3 ParseRecordings.py functionName "fileName.json"`

### List of functions:

1. exampleEntry
2. entireDataset
3. getTypeValues
4. countOccurrences
5. withoutCodeCoverage
6. firstCodeCoverage

Example:
`python3 ParseRecordings.py exampleEntry "example_recording.json"`

## ParseDatabase.py:

Usage:
`python3 ParseDatabse.py functionName`

### List of functions:

Hypotheses

1. exampleHypothesis
2. allHypotheses
3. getHypothesisById id

Evidence

4. allEvidence
5. apiCalls
6. domEvents
7. networkEvents
8. rawAPIEvidence
9. rawDOMEvidence
10. rawNetworkEvidence

Example:
`python3 ParseDatabse.py allHypotheses`
