from crewai import Crew, Process
from agents import youtube_video_researcher, blog_writer
from tasks import research_task, writing_task

import sys

### Create a tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[youtube_video_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

### Start the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': sys.argv[1]})
print(result)