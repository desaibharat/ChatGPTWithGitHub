# ChatGPTWithGitHub

This repository contains a minimal example showing how to use [LangChain](https://python.langchain.com/) with an [Ollama](https://ollama.ai/) model.

## Requirements

- Python 3.8+
- `langchain` and `ollama` Python packages
- An Ollama server with a model installed (for example `llama2`)

## Running the example

1. Install the dependencies:

```bash
pip install langchain ollama
```

2. Ensure the Ollama server is running and the model specified in `langchain_ollama_example.py` is available.

3. Execute the script:

```bash
python langchain_ollama_example.py
```

The script sends a prompt to the model asking it to translate a short text into French. The response from Ollama will be printed to the console.
