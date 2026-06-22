from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬")

st.title("🎬 Movie Information Extractor")
st.write("Paste a movie description and extract useful information.")

llm = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert content analyst.

Your task is to read the provided movie description and extract all useful information in a well-structured human-readable format.

Guidelines:
- Extract only information that is present or can be reasonably inferred.
- Do not invent facts.
- If a field is unavailable, write "Not Mentioned".
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
        (
            "human",
            """Movie Description:
{movie_description}"""
        ),
    ]
)

para = st.text_area(
    "Enter Movie Description",
    height=250,
    placeholder="Paste movie description here..."
)

if st.button("Extract Information"):
    if para.strip():

        final_prompt = prompt.invoke(
            {"movie_description": para}
        )

        with st.spinner("Analyzing..."):
            response = llm.invoke(final_prompt)

        st.subheader("Extracted Information")
        st.markdown(response.content)

    else:
        st.warning("Please enter a movie description.")