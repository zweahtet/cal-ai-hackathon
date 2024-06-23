from crewai import Task
from textwrap import dedent

class SentimentAnalysisTasks:

    def research(self, agent, company, date_range):
        return Task(
            description=dedent(f"""
                Collect and summarize recent news articles or social media posts spanning the last week related to .
                Analyze the sentiment of the public towards the {topic} from each source using the Hume AI Sentiment Analysis Tool.

                Make sure to use the most relevant and up-to-data as possible.
                Selected company by the customer: {company}
                Date range: {date_range}
            """),
            agent=agent,
            expected_output="A comprehensive analysis of the sentiment of the public towards the {topic} based on the data gathered.",
        )
    
    def sentiment_analysis(self, agent, company, date_range):
        return Task(
            description=dedent(f"""
                Analyze the sentiment of the public towards the {topic} based on the data provided by the research analyst.
                Use the Hume AI Sentiment Analysis Tool to analyze the sentiment of the public towards the {topic}.

                Selected company by the customer: {company}
                Date range: {date_range}
            """),
            agent=agent,
            expected_output="A detailed report on the sentiment of the public towards the {topic} based on the analysis conducted.",
        )
    
    def write_report(self, agent, company, date_range):
        return Task(
            description=dedent(f"""
                Write a detailed report in markdown based on the insights provided by the research analyst.
                The report should include a summary of the sentiment analysis conducted and the key findings.

                Selected company by the customer: {company}
                Date range: {date_range}
            """),
            agent=agent,
            expected_output="A well-structured report in markdown format summarizing the sentiment of the public towards the {topic}.",
        )
    
    def __tip_section(self):
        return "If you do your BEST WORK, you will be rewarded with a bonus of $1000."
