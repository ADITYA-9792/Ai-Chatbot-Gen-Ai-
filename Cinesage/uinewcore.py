
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

load_dotenv()

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Movie Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Extract structured movie information from a paragraph.")

# ---------------- Schema ----------------
class Movie(BaseModel):
    title: str
    release_date: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# ---------------- LLM ----------------
llm = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    (
        'system',
        """
Extract movie information from the paragraph.

{format_instructions}
"""
    ),
    (
        'human',
        """
{paragraph}
"""
    )
])

# ---------------- Input ----------------
para = st.text_area(
    "Movie Description",
    height=250,
    placeholder="Paste a movie description here..."
)

# ---------------- Process ----------------
if st.button("Extract Information"):

    if para.strip():

        final_prompt = prompt.invoke(
            {
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            }
        )

        with st.spinner("Analyzing..."):
            response = llm.invoke(final_prompt)
            movie_data = parser.parse(response.content)

        st.success("Information Extracted Successfully!")

        st.subheader("🎥 Movie Details")

        st.markdown(f"### {movie_data.title}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("📅 Release Year",
                      movie_data.release_date if movie_data.release_date else "N/A")

        with col2:
            st.metric("⭐ Rating",
                      movie_data.rating if movie_data.rating else "N/A")

        st.markdown("#### 🎭 Genres")
        st.write(", ".join(movie_data.genre))

        st.markdown("#### 🎬 Director")
        st.write(movie_data.director or "Not Mentioned")

        st.markdown("#### 👥 Cast")
        if movie_data.cast:
            for actor in movie_data.cast:
                st.write(f"• {actor}")
        else:
            st.write("Not Mentioned")

        st.markdown("#### 📝 Summary")
        st.info(movie_data.summary)

    else:
        st.warning("Please enter a movie description.")
