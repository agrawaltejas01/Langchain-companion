from lib.config import Config

import openai

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough


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

    # Need Chain1's output as a string, so that it can be passed in chain2
    chain1 = prompt1 | llm | StrOutputParser()
    chain2 = prompt2 | llm | StrOutputParser()

    # Call chain1's output as emotion and pass this to chain2
    chain = {"emotion": chain1
             } | RunnablePassthrough() | chain2

    # As chain2 also outputs string, we can simply print this output

    output = chain.invoke({"text": "What is this chain in langchain?"})
    print(output)
    # Output
    '''
        Curiosity plays a crucial role in human development and learning. 
        It drives children to explore their surroundings, ask questions, and experiment with new things. 
        It also fuels the pursuit of knowledge and innovation in adults, pushing them to seek answers, 
        discover new ideas, and make breakthroughs in various fields.        

    '''
