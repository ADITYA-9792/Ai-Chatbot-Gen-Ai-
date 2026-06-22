from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)
model=ChatHuggingFace(llm=llm)
hg=model.invoke("who are u?")
print(hg.content)