from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

load_dotenv()

class Movie(BaseModel):
    title: str
    release_date: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

llm = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            """You are an expert content analyst.

Your task is to read the provided movie description and extract all useful information in a well-structured human-readable format.

Guidelines:
- Extract only information that is present or can be reasonably inferred.
- Do not invent facts.
- If a field is unavailable, write \"Not Mentioned\".
- Keep the summary concise and informative.
- Identify both factual details and opinions expressed in the text.

Provide the output in the following format:

MOVIE NAME:
<movie name>

GENRE:
<genre(s)>

SUB-GENRE:
<sub-genre(s)>

MAIN CHARACTERS:
<main characters>

CAST:
<cast if mentioned>

DIRECTOR:
<director if mentioned>

PLOT:
<short plot description>

QUICK SUMMARY:
<2-3 sentence summary>

SETTING:
<where and when the story takes place>

KEY THEMES:
- Theme 1
- Theme 2
- Theme 3

NOTABLE FEATURES:
- Feature 1
- Feature 2
- Feature 3

VISUALS:
<information about cinematography or visual quality>

MUSIC / SOUNDTRACK:
<information about music>

STRENGTHS:
- Point 1
- Point 2
- Point 3

WEAKNESSES:
- Point 1
- Point 2

CRITICAL RECEPTION:
<overall opinion or reputation>

TARGET AUDIENCE:
- Audience type 1
- Audience type 2

KEYWORDS:
keyword1, keyword2, keyword3 ...

OVERALL SENTIMENT:
Positive / Neutral / Negative

RECOMMENDATION:
Who would enjoy this movie and why?"""
        ),
        HumanMessagePromptTemplate.from_template(
            """Movie Description:
{movie_description}"""
        ),
    ]
)

para = input("Write your paragraph: ")
final_prompt = prompt.format_prompt(movie_description=para)
response = llm.invoke(final_prompt)
print(response.content)






















