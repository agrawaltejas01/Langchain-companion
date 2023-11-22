from lib.config import Config

import openai

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

from langchain.schema.runnable import RunnableLambda


def routerChain(model="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model=model,
                     openai_api_key=Config.openAiApiKey)

    input_chain = (ChatPromptTemplate.from_template(
        "Explain the emotion in 1 word for this text {text} ")
        | llm | StrOutputParser)

    curiosity_chain = (ChatPromptTemplate.from_template(
        """
        Always answer questions starting with "Going in Curiosity chain - " \
        Explain a bit about the emotion ${emotion}
        """) | llm)

    anger_chain = (ChatPromptTemplate.from_template(
        """
        Always answer questions starting with "Going in Anger chain - " \
        Explain a bit about the emotion ${emotion}
        """) | llm)

    happy_chain = (ChatPromptTemplate.from_template(
        """
        Always answer questions starting with "Going in Happy chain - " \
        Explain a bit about the emotion ${emotion}
        """) | llm)

    other_chain = (ChatPromptTemplate.from_template(
        """
        Always answer questions starting with "Going in Other chain - " \
        Explain a bit about the emotion ${emotion}
        """) | llm)

    def route(info):
        if "curiosity" in info["emotion"].lower():
            return curiosity_chain
        if "anger" in info["emotion"].lower():
            return anger_chain
        if "happy" in info["emotion"].lower():
            return happy_chain
        else:
            return other_chain

    # # Think, here we could have made it more complex if needed
    # branchChain = RunnableBranch(
    #     (lambda x: "curiosity" in x["emotion"].lower(
    #     ), curiosity_chain),
    #     (lambda x: "anger" in x["emotion"].lower(), anger_chain),
    #     (lambda x: "happy" in x["emotion"].lower(), happy_chain),
    #     other_chain
    # )
    chain = {
        "emotion": input_chain,
        # "emotion": lambda x: x["emotion"]
    } | RunnableLambda(route)

    output = chain.invoke({"text": "What is this chain in langchain?"})
    print(output)
    # Output
    '''
        Curiosity is an emotion that drives individuals to seek out new knowledge, 
        experiences, and understanding. It is a natural human instinct that compels us to explore, 
        investigate, and learn about the world around us. Curiosity is often characterized by 
        a strong desire to know, discover, and uncover the unknown.
    '''
