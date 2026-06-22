from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
text=[
    "hello this is aditya",
    "hello your full name is aditya vikram singh", 
    "you are gen ai developer"
]
vector=embedding.embed_documents(text)
print(vector)