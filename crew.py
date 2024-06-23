from crewai import Crew
import streamlit as st
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
        with st.spinner("Creating Agents..."):
            research_analyst_agent = agents.research_analyst()
            sentiment_analyst_agent = agents.sentiment_analyst()
            report_writer_agent = agents.report_writer()
        st.status("Agents Created.", state="complete")

        # Create tasks
        with st.spinner("Creating Tasks..."):
            research_task = tasks.research(
                research_analyst_agent, self.company, self.date_range
            )

            sentiment_task = tasks.sentiment_analysis(
                sentiment_analyst_agent, self.company, self.date_range
            )

            report_task = tasks.write_report(
                report_writer_agent, self.company, self.date_range
            )
        st.status("Tasks Created.", state="complete")

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

        with st.spinner("Running Sentiment Analysis Crew..."):
            result = crew.kickoff()

        st.info("Sentiment Analysis Crew has completed the tasks.")
        return result

