# ChatGPTWithGitHub

This repository contains a minimal example showing how to use [LangChain](https://python.langchain.com/) with an [Ollama](https://ollama.ai/) model.

## Requirements

- Python 3.8+
- `langchain` and `ollama` Python packages
- An Ollama server with a model installed (for example `llama2`)

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Install the model on your Ollama server (replace `llama2` if you want a
   different model):

```bash
ollama pull llama2
```

4. Start the Ollama server so the script can access the model:

```bash
ollama serve
```

## Running the example

1. Ensure the Ollama server is running and the model specified in `langchain_ollama_example.py` is available (see the Setup section above).

2. Execute the script:

```bash
python langchain_ollama_example.py
```

The script sends a prompt to the model asking it to translate a short text into French. The response from Ollama will be printed to the console.
