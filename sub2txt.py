from langchain_groq import ChatGroq
from dotenv import load_dotenv

def file_operation(file_path, operation, content= ''):
    with open(file_path, operation) as file:
        #launch an error if operation isn't r or w
        if operation == 'r':
            return file.read()
        
        if operation == 'w':
            file.write(content)
        

load_dotenv()

source_language = 'english'
target_language = 'italian'
extension = 'vtt'
file_name = "example"

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

messages = [
    (
        "system", f"You are a helpful assistant that translates {source_language.title()} to {target_language.title()}. Translate the user text, convert it from {extension} into text and return only the text.",
    ),
    ("human", file_operation(f"{file_name}.{extension}", 'r')),
]

ai_msg = llm.invoke(messages)

file_operation(f"{file_name}.txt", 'w', ai_msg.content)