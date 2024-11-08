from crewai import Task
from tools import yt_tool
from agents import youtube_video_researcher, blog_writer

### Content research task
research_task = Task(
    description=(
        "Identify the video on the topic {topic}"
        "Get detailed information about the video from the Youtube channel"
    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} content of the video",
    tools=[yt_tool],
    agent=youtube_video_researcher
)

### Blog writing task
writing_task = Task(
    description=(
        "Get the info from the Youtube channel video on the topic {topic}."
    ),
    expected_output="Summarize the info from Youtube channel video on the topic {topic} and create content for the blog",
    tools=[],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog.md'
)