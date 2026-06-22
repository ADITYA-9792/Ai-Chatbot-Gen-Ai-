from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage,AIMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
    
)
print("choose ur mode of response")
print("press 1 for Angry mode")
print("press 2 for funny mode")
print("press 3 for Sad mode")

choice = int(input("enter ur mode of response: "))
if choice==1:
 mode="you are Angry ai agent"
elif choice==2:
 mode="you are funny ai agent"
elif choice==3:
 mode="you are sad ai agent"  




messages=[
 SystemMessage(content=mode)
]
print("------------Welcome to Chatbot--------------")
while True:
 prompt=input("You: ")
 messages.append(HumanMessage(content=prompt))
 if prompt=="0":
  print("Thanks for using our chatbot")
  break
 
 response = llm.invoke(messages)
 messages.append(AIMessage(content=response.content))
 print('Bot: ',response.content)