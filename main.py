import chromadb
from langchain_ollama.llms import OllamaLLM
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import chainlit as cl


@cl.on_chat_start
def main():
    sentence_transformers_ef =  SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")
    client = chromadb.PersistentClient(path="C:\\Users\\Bishal\\Documents\\Langchain\\chroma")


    ## Init Langchain for Chroma
    chroma = Chroma(
        collection_name="news",
        embedding_function=sentence_transformers_ef,
        client=client
    )

    #### Init ML
    # Initialize the LLM
    llm = OllamaLLM(model='llama3.1', temperature=0, max_token=1000)

    # Create the retriever
    retriever = chroma.as_retriever()

    # Initialize the chain
    memory = ConversationBufferMemory( memory_key="chat_history", return_messages=True,output_key='answer')
    
    chain = ConversationalRetrievalChain.from_llm(llm=llm, 
                                                retriever=retriever,
                                                memory = memory, 
                                                verbose=True,    # For seeing output on terminal
                                                return_source_documents=True,
                                                output_key="answer"
                                                )

    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message: str):
    # Retrieve the chain from the user session
    chain = cl.user_session.get("chain") 

    # Call the chain asynchronously
    res = await chain.ainvoke(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])

    # Send the response
    await cl.Message(content=f'Answer:\n {res["answer"]}\n\n Sources:\n {res["source_documents"][0].metadata["source"]}').send()