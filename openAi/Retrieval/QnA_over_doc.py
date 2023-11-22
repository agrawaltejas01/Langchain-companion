from langchain.document_loaders import PyPDFLoader
from lib.config import Config

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import DocArrayInMemorySearch

from langchain.indexes import VectorstoreIndexCreator

import openai

openai.api_key = Config.openAiApiKey


def load_pdf():
    loader = PyPDFLoader("openAi/Retrieval/SampleFoodBusinessPlan.pdf")

    # pages = loader.load_and_split()
    # print(pages[0])

    return loader


def create_indexes(loader):
    index = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch
    ).from_loaders([loader])

    return index


def qna():
    loader = load_pdf()
    index = create_indexes(loader=loader)

    response = index.query("What is this document about?")
    print(response)

    # Output
    """
    > response = index.query("What is this document about?")
    print(response)
     This document is about a business plan for a small food business.
    """
