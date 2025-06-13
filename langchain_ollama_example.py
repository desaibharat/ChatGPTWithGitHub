from langchain import PromptTemplate, LLMChain
from langchain.llms import Ollama


def main():
    """Run a simple LangChain example using an Ollama model."""
    prompt = PromptTemplate(
        template="Translate the following text to {language}: {text}",
        input_variables=["language", "text"],
    )

    # Replace 'llama2' with the name of an Ollama model you have installed
    llm = Ollama(model="llama2")
    chain = LLMChain(prompt=prompt, llm=llm)

    result = chain.run({"language": "French", "text": "Hello, my friend!"})
    print(result)


if __name__ == "__main__":
    main()
