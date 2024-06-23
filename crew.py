from crewai import Crew

from agents import SentimentAnalysisAgents
from tasks import SentimentAnalysisTasks

class SentimentCrew:
    verbose: bool = True
    memory: bool = True
    cache: bool = True

    def __init__(self, company, start_date, end_date):
        self.company = company
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        agents = SentimentAnalysisAgents()
        tasks = SentimentAnalysisTasks()

        research_analyst_agent = agents.research_analyst()
        sentiment_analyst_agent = agents.sentiment_analyst()
        report_writer_agent = agents.report_writer()

        research_task = tasks.research(research_analyst_agent, self.company)
        sentiment_task = tasks.sentiment_analysis(sentiment_analyst_agent)
        report_task = tasks.write_report(report_writer_agent)

        crew = Crew(
            agents=[research_analyst_agent, sentiment_analyst_agent, report_writer_agent],
            tasks=[research_task, sentiment_task, report_task],
            verbose=self.verbose,
            memory=self.memory,
            cache=self.cache,
            max_rpm=100,
        )

        result = crew.kickoff()
        return result