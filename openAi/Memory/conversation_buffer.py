from lib.config import Config

import openai

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory


openai.api_key = Config.openAiApiKey


def memoryTester(llm, memory):
    conversation = ConversationChain(
        llm=llm, memory=memory, verbose=False)

    print(conversation.predict(input="Hi, my name is Tejas"))

    prediction = conversation.predict(input="How is the weather today?")
    prediction = conversation.predict(input="Hmm, its quite sunny here")

    print(conversation.memory.buffer)

    print(conversation.predict(input="What is my name again?"))


def conversationBufferMemory(model="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model=model,
                     openai_api_key=Config.openAiApiKey)
    memory = ConversationBufferMemory(llm=llm)

    memoryTester(llm=llm, memory=memory)
    # Output
    '''
    > print(conversation.predict(input="Hi, my name is Tejas"))
    Hello Tejas! It's nice to meet you. How can I assist you today?

    > print(conversation.memory.buffer)
    Human: Hi, my name is Tejas
    AI: Hello Tejas! It's nice to meet you. How can I assist you today?
    Human: How is the weather today?
    AI: I'm sorry, but as an AI, I don't have access to real-time information. I don't know the current weather. However, you can check the weather by using a weather app or website, or by asking a voice assistant like Siri or Google Assistant.
    Human: Hmm, its quite sunny here
    AI: That's great to hear! Sunny weather can be quite enjoyable. Is there anything else I can help you with?

    > print(conversation.predict(input="What is my name again?"))
    Your name is Tejas.
    '''


def conversationBufferWindowMemory(model="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model=model,
                     openai_api_key=Config.openAiApiKey)
    memory = ConversationBufferWindowMemory(k=1)

    # Lets load up memory with pre-defined context
    memory.save_context({"input": "hi"}, {"output": "whats up"})
    memory.save_context({"input": "not much you"}, {"output": "not much"})

    memory_variables = memory.load_memory_variables({})
    print(memory_variables)

    memoryTester(llm=llm, memory=memory)
    # Output
    '''
    > print(memory_variables)
    # As the window length is defined as 1, it only remembered Last context
    {'history': 'Human: not much you\nAI: not much'}

    > print(conversation.predict(input="Hi, my name is Tejas"))
    Hello Tejas! It's nice to meet you. How can I assist you today?

    > print(conversation.memory.buffer)
    Human: Hmm, its quite sunny here
    AI: That's great to hear! Sunny weather can be really enjoyable. 
    It's always nice to have some sunshine and clear skies. Is there anything else you would like to talk about?

    > print(conversation.predict(input="What is my name again?"))
    I'm sorry, but I don't have access to personal information about individuals unless it 
    has been shared with me in the course of our conversation. I am designed to respect user privacy and confidentiality.
    '''
