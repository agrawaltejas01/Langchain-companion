from lib.config import Config

import openai

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser


def simpleSequentialChain(model="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model=model,
                     openai_api_key=Config.openAiApiKey)

    prompt1 = ChatPromptTemplate.from_template(
        "Explain the emotion in 1 word for this text {text}")
    prompt2 = ChatPromptTemplate.from_template(
        "Explain a bit about the emotion ${emotion}")

    # Cant just | them 🤣
    '''
    # Chaining Prompt and LLM
    chain = prompt1 | prompt2 | llm

    output = chain.invoke({"text": "What is this chain in langchain?"})
    print(output)

    # Output
    
    langchain.prompts.chat.BaseChatPromptTemplate.format_prompt() argument after ** must be a mapping, not ChatPromptValue
    '''

    chain = (
        {"emotion": prompt1 | llm | StrOutputParser()}
        | prompt2
        | llm
        | StrOutputParser()
    )

    output = chain.invoke({"text": "What is this chain in langchain?"})
    print(output)
    # Output
    '''
        Curiosity is an emotion that drives individuals to seek out new knowledge, 
        experiences, and understanding. It is a natural human instinct that compels us to explore, 
        investigate, and learn about the world around us. Curiosity is often characterized by 
        a strong desire to know, discover, and uncover the unknown.
    '''
