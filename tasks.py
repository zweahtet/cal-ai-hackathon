from crewai import Task
from textwrap import dedent

class SentimentAnalysisTasks:

    def research(self, agent, topic, ):
        return Task(
            description=dedent(f"""
                Collect and summarize recent news articles or social media posts spanning the last week related to .
                Analyze the sentiment of the public towards the {topic} from each source using the Hume AI Sentiment Analysis Tool.

                Make sure to use the most relevant and up-to-data as possible.
                Selected company by the user: {topic}
            """),
            agent=agent,
            expected_output="A comprehensive analysis of the sentiment of the public towards the {topic} based on the data gathered.",
        )
