from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

chat = ChatOpenAI(temperature=0.0)
chat



# Now we will be defining output schema.
# Lets say we want it in a JSON

understanding_schema = ResponseSchema(
    name="understanding",
    description="""What all did you understand about the doc? return null if none"""
)
insight_schema = ResponseSchema(
    name="insights-and-persepective",
    description="""What all insights and perspective could you build about the doc? return null if none"""
)
facts_schema = ResponseSchema(
    name="facts",
    description="""What are facts stated in it? return null if none"""    
)
further_research_schema = ResponseSchema(
    name="facts",
    description="""What should I research further in this? return null if none"""
)

response_schemas = [
    understanding_schema,
    # insight_schema,
    facts_schema,
    further_research_schema,
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()




template_string = """ Read and analyse the text that is delimited by triple backticks. \
    It is a document that I want you to analyse. Provide me with following data
    1. Insights and Perspectives
    2. Conduct fact-checking
    3. Suggest further research
    Document content is ```{text}```

    {format_instructions}
     """
prompt_template = ChatPromptTemplate.from_template(template_string)


def run_prompt_template():
    userInput = input()

    if userInput == "-1":
        print("bye!")

    while userInput != "-1":
        prompt = prompt_template.format_messages(text=userInput, format_instructions=format_instructions)
        response = chat(prompt)

        output_dict = output_parser.parse(response.content)

        print("Response -> ")
        print(output_dict)

        print("----------------------")
        print("Prompt ->")
        userInput = input()
