from crewai import Task
from textwrap import dedent


class SentimentAnalysisTasks:

    def __tip_section(self):
        return "If you do your BEST WORK, you will be rewarded with a bonus of $1000."

    def research(self, agent, company, date_range):
        task = Task(
            description=dedent(
                f"""
                Collect and summarize news articles and social media posts related to the sentiment of the public towards the company.
                {self.__tip_section()}
                Make sure to use the most relevant and up-to-date data as possible.
                Selected company by the customer: {company}
                Date range: {date_range}
            """
            ),
            agent=agent,
            expected_output="A detailed summary of the news articles, social media posts, company announcements, and market analysis reports related to the sentiment of the public towards the company.",
        )
        return task

    def sentiment_analysis(self, agent, company, date_range):
        task = Task(
            description=dedent(
                f"""
                Conduct sentiment analysis on the collected data to determine the overall sentiment of the public towards the company.
                {self.__tip_section()}
                Selected company by the customer: {company}
                Date range: {date_range}
            """
            ),
            agent=agent,
            expected_output="A detailed sentiment analysis report on the public sentiment towards the company spanning the specified date range.",
        )
        return task

    def write_report(self, agent, company, date_range):
        task = Task(
            description=dedent(
                f"""
                Write a detailed report in markdown format encompassing the insights provided by the Research Analyst 
                and Sentiment Analysis Specialist on the sentiment of the public towards the company.
                Your final report should include a summary of the data collected, sentiment analysis results, and key findings.
                Also, include the time series analysis of the sentiment over the specified date range.
                
                {self.__tip_section()}
                Selected company by the customer: {company}
                Date range: {date_range}
            """
            ),
            agent=agent,
            expected_output="A well-structured report in markdown format detailing the sentiment of the public towards the company.",
        )
        return task
