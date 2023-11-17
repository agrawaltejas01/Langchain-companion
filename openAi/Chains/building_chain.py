from lib.config import Config

import openai

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def basicChain(model="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model=model,
                     openai_api_key=Config.openAiApiKey)
    prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")

    # Chaining Prompt and LLM
    chain = prompt | llm

    output = chain.invoke({"foo": "bears"})
    print(output)

    # Output
    '''
    content="Why don't bears wear shoes?\n\nBecause they have bear feet!" additional_kwargs={} example=False
    '''

    # Trying different order for chains
    '''
    chain = llm | prompt
    output = chain.invoke({"foo": "bears"})
    print(output)

    # Output
    ValueError: Invalid input type <class 'dict'>. Must be a PromptValue, str, or list of BaseMessages.

    = Input was expected for LLM and not Prompt, thats why it failed

    # Conclusion - 
    1. Order of chain matters
    '''
