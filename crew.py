from crewai import Crew

from agents import SentimentAnalysisAgents
from tasks import SentimentAnalysisTasks


class SentimentCrew:
    verbose: bool = True
    memory: bool = True
    cache: bool = True

    def __init__(self, company, date_range):
        self.company = company
        self.date_range = date_range

    def run(self):
        agents = SentimentAnalysisAgents()
        tasks = SentimentAnalysisTasks()

        # Create agents
        research_analyst_agent = agents.research_analyst()
        sentiment_analyst_agent = agents.sentiment_analyst()
        report_writer_agent = agents.report_writer()

        # Create tasks
        research_task = tasks.research(
            research_analyst_agent, self.company, self.date_range
        )

        sentiment_task = tasks.sentiment_analysis(
            sentiment_analyst_agent, self.company, self.date_range
        )

        report_task = tasks.write_report(
            report_writer_agent, self.company, self.date_range
        )

        crew = Crew(
            agents=[
                research_analyst_agent,
                sentiment_analyst_agent,
                report_writer_agent,
            ],
            tasks=[research_task, sentiment_task, report_task],
            verbose=self.verbose,
            memory=self.memory,
            cache=self.cache,
            max_rpm=100,
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    sentiment_crew = SentimentCrew("Apple", "01-01-2022 to 03-01-2022")
    result = sentiment_crew.run()
    print("### Result ###")
    print(result)
