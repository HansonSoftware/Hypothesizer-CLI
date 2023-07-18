# Hypothesizer Command Line Tools

A Command Line Interface for interacting with OpenAI's API, parsing our database of hypotheses, and creating Semgrep rules. These tools support [Hypothesizer](https://github.com/Alaboudi1/Hypothesizer-Debugger).

## Using the Hypothesizer-ChatBot:

1.  Clone the repo and create a .env file then add your OpenAI API Key.

    Example:
    .env should contain

    ```
    OPENAI_KEY = sk-youropenaikey
    ```

    You want to make sure this key is not shared.

2.  cd into Hypothesizer-ChatBot and run UseAPI.py from your terminal to make sure you're all set.

3.  Follow the initial instructions given by the script and follow the prompts for a successful chat!

## Using the Parsers

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
