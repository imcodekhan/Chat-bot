from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os

os.environ['OPENAI_API_KEY'] = "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"


def createVectorIndex(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20

    prompt_helper = PromptHelper(
        max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)

    # define LLM
    llmPredictor = LLMPredictor(llm=OpenAI(
        temperature=0, model_name='text-ada-001', max_tokens=tokens))

    # load data

    docs = SimpleDirectoryReader(path).load_data()

    # create vector index
    vectorIndex = GPTSimpleVectorIndex(
        documents=docs, llm_predictor=llmPredictor, prompt_helper=prompt_helper)
    vectorIndex.save_to_disk('vectorIndex.json')
    return vectorIndex


vectorIndex = createVectorIndex('Data')


def answerMe(swaal, vectorIndex=vectorIndex):
    vIndex = GPTSimpleVectorIndex.load_from_disk(vectorIndex)
    while True:
        # prompt = if swaal input('Please ask: ')
        response = vIndex.query(swaal, response_mode='compact')
        return response

    # print(f'Response: {response} \n')
