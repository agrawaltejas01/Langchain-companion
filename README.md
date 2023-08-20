## [Deeplearning.Ai - Langchain](https://learn.deeplearning.ai/langchain/) - Andrew Ng, Harrison Chase

## [Langchain Docs](https://python.langchain.com/docs/get_started/introduction.html)

## Models

- ### [Doc](https://python.langchain.com/docs/modules/model_io/models/llms/)

- Different models like GPT 4.5, GPT-3-turbo. Each with its capabilities and features
- 4 layers of neural n/w
  - Embedding layer
    - converts each word in the input text into a high-dimensional vector representation.
    - These embeddings capture semantic and syntactic information about the words and help the model to understand the context
  - Feedforward layer
    - have multiple fully connected layers that apply nonlinear transformations to the input embeddings
    - These layers help the model learn higher-level abstractions from the input text.
  - Recurrent layer
    - designed to interpret information from the input text in sequence
    - These layers maintain a hidden state that is updated at each time step, allowing the model to capture the dependencies between words in a sentence
  - Attention layer
    - allows the model to focus selectively on different parts of the input text
    - This mechanism helps the model attend to the input text’s most relevant parts and generate more accurate predictions.

## Completion

- ### [Doc](https://python.langchain.com/docs/modules/model_io/prompts/)

- Send a prompt to user and get a response

## Template messages and Output parser

- ### Template messages

  - [Doc](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)
  - When building an app, you will have a specific use case that you want to serve. For e.g you have built an
    application on providing insights on a document you are reading
  - You will provide specific functionalities around it, providing fact checks, references and citations etc
  - For this, _**we will use a template which has a defined use case that we want our model to give output for**_

- ### Output parser

  - [Doc](https://python.langchain.com/docs/modules/model_io/output_parsers/)
  - In that application of yours, you cant read human strings returned by Template messages always.
  - Output parser provided by Langchain will help you put it in parsable formats like JSON, List, Enums, etc

- ### [Check out Complete module](openAi/prompt_template.py)
