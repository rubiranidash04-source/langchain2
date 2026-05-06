from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found. Please check your .env file.")
    exit()

try:
    # Initialize model
    model = ChatOpenAI(model="gpt-3.5-turbo")

    # Send test message
    response = model.invoke([
        HumanMessage(content="Explain LangChain in one sentence.")
    ])

    print("Environment setup successful!\n")
    print("Model Response:")
    print(response.content)

except Exception as e:
    print("Error during validation:")
    print(e)
