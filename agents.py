import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="groq/Gemma2-9b-it",groq_api_key=groq_api_key)

from crewai import Agent 
from tools import yt_tool


## create a senior blog content researcher 

blog_researcher = Agent(
    role="Blog Researcher from youtube videos",
    goal="get the relevant video content for the blog post",
    name="Senior Blog content researcher",  ## optional
    description="A Senior Blog content researcher from youtube videos",  ## optional
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science, Machine Learning (ML) and GEN AI and providing suggestion"
    ),
    tool= [yt_tool],
    allow_delegation = True,  ## transfering the work done by the agent to someone else
    llm = llm
    )




## create a senior blog writer agent with YT tool
 
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm = llm,
    output_file = "new_blog_post.md"

)

