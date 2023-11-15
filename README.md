## [Deeplearning.Ai - Langchain](https://learn.deeplearning.ai/langchain/) - Andrew Ng, Harrison Chase

## [Langchain Docs](https://python.langchain.com/docs/get_started/introduction.html)

- ### What does it do?
  - A model that takes a sentence as input breaks the word into token, makes it a list and
  - returns a sentence (sequence of words ) that has the best probability of relevance
  - Now this input can be textual or any media depending on model

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

## Pricing of Open AI

- Ok, OpenAI has built a great model. Why is it so costly?
- They charge on a per token basis. [What is token and how to count them?](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
  - [Remember how it works?](https://github.com/agrawaltejas01/Langchain-companion#what-does-it-do)

## Memory

- ### [Doc](https://python.langchain.com/docs/modules/memory/)

- More the context these models are accurate. Context ∝ Accuracy
- These models are use and throw. They dont remember anything
- So you have to send a long message to them so they can answer more correctly and relevant answer.
- **:euro:** Most models charge on per token basis. Not just input, but output **:cold_sweat:**
- Nope, there is no way, !! [See for yourself](https://cdn.sanity.io/images/vr8gru94/production/927ca8cc5d92ee75f36d7eb4bef4685c4e3118e5-2880x1370.png) (Great idea, you anti FOSS MBAs). They say are trying this in GPT-4, lets see.

- Alright,
- Now we have to manage the memory on our own. How do we do that?
- ## [I do it here](openAi/Memory/README.md)
