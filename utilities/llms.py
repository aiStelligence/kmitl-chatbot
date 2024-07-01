from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
# Load environment variables from .env file
import os
load_dotenv()

AZURE_OPENAI_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_KEY")

llm = ChatOpenAI(
    api_key='sk-proj-gfA9WQMdhwOmo2lOMFtAT3BlbkFJ9qwC52ExKO4FTTatmUNH',
    model='gpt-4o', 
)

embedding = OpenAIEmbeddings(
    api_key='sk-proj-gfA9WQMdhwOmo2lOMFtAT3BlbkFJ9qwC52ExKO4FTTatmUNH',
    model='text-embedding-ada-002'
)