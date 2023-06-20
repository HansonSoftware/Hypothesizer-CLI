# Hypothesizer-CLI
A Command Line Interface for interacting with OpenAI's API. There is additional functionality built on top to support [Hypothesizer](https://github.com/Alaboudi1/Hypothesizer-Debugger).

## Getting Started:

1.  Clone the repo and add a .env file with your OpenAI API Key.

    Example:
    .env should contain
    ```
    OPENAI_KEY = abc123secretkey
    ```

    You want to make sure this key is not shared.

2. Run HypothesizerCLI.py from your terminal, follow the prompts.


## Using ParseJSON.py:

Usage:
```python3 ParseJSON.py functionName "fileName.json"```

### List of functions:
1. exampleEntry
2. entireDataset
3. getTypeValues
4. countOccurrences
5. withoutCodeCoverage
6. firstCodeCoverage

Example:
```python3 ParseJSON.py exampleEntry "recording.json"```
