from lib.config import Config

import openai

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory


openai.api_key = Config.openAiApiKey


def conversationSummaryMemory(model="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model=model,
                     openai_api_key=Config.openAiApiKey)
    memory = ConversationSummaryMemory(llm=llm, max_token_limit=50)

    conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

    print(conversation.predict(input="Hi, my name is Tejas"))

    prediction = conversation.predict(input="How is the weather today?")
    prediction = conversation.predict(input="Hmm, its quite sunny here")

    print(conversation.memory.buffer)
    # Output
    '''
    > print(conversation.predict(input="Hi, my name is Tejas"))
    Hello Tejas! It's nice to meet you. How can I assist you today?

    > print(conversation.memory.buffer)
    Tejas introduces themselves to the AI and the AI greets them and asks how it can assist. 
    The AI explains that it can provide general weather conditions based on the user's location. 
    Tejas mentions that it is sunny where they are. The AI responds positively to the sunny weather and asks Tejas where they are located.
    '''

    print(conversation.predict(input="What is my name again?"))
    # Output - Run 1
    '''
    I'm sorry, but I don't have access to personal information about individuals unless it has been 
    shared with me in the course of our conversation. I am designed to respect user privacy and confidentiality.
    '''

    # Output - Run 2
    '''Your name is Tejas.'''
