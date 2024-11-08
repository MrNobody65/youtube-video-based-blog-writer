from crewai import Agent
from tools import yt_tool

### Create a senior youtube video content researcher
youtube_video_researcher = Agent(
    role='Blog content researcher from Youtube videos',
    goal="get the relevent video content for the topic {topic} from youtube channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in Data Science, Artificial Intelligence, Machine Learning and Generative AI and suggesting content for blog"
    ),
    tools=[],
    allow_delegation=True
)

### Create a senior blog writer
blog_writer = Agent(
    role='Blog writer',
    goal="Narrate compelling tech stories about the videos in topic {topic} from youtube channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)