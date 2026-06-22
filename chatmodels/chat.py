from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0,max_tokens=400)

print(llm.invoke("Write a joke on ai").content)

#for groq
###from langchain_groq import ChatGroq

###llm = ChatGroq(model="llama-3.3-70b-versatile")
##print(llm.invoke("What is cricket?").content)

#for mistralai
"""from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    model="mistral-small-latest",
    
)

response = llm.invoke("What is cricket?")
print(response.content)"""
