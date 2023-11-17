## [Official Doc](https://python.langchain.com/docs/modules/chains/)

## Chains

- While doing real world tasks, we will require to have a complex system which deals with multiple prompts to get the required result
- To do this, Langchain provides a simple architecture called chains.
- Chain is a composition of different components. These components can be
  - prompts
  - Output parsers
  - A chain itself
  - Etc
- Example
  - Trading Bot Chain
  - Data Collection -> Text Processing -> Sentiment Analysis -> Prompt Selector -> Trend Detection -> Language Model -> Trading Decision
- Method used in the video is different that the code, because at the time of writing, Langchain has introduced a new way of building and dealing with chains called LCEL (LangChain Expression Language).
- I build a basic chain [here](./building_chain.py)

## Types of chains

- There are 3 main types of chains

- ### Simple sequential

  - Makes a series of calls to a language model. This is particularly useful when you want to take the output from one call and use it as the input to another.
  - ![](./Simple-sequential.png)
  - [Code here](./simple_sequential.py)

- ### Sequential
  - Code here
  - ![](./Sequential.png)
  - Code here
- ### Router
  - Code here
