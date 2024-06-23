import os

from langchain_core.messages import SystemMessage
from hume import HumeStreamClient
from hume.models.config import LanguageConfig
from crewai import Agent
from crewai_tools import (
    SerperDevTool,
    BrowserbaseLoadTool,
    SeleniumScrapingTool,
    EXASearchTool,
    BaseTool,
)

# locals
from llms import (
    llama_3_70b_llm_groq,
    llama_3_8b_llm_groq,
    mixtral_8x7b_llm_groq,
    gpt4_turbo_llm_openai,
)

# Tools
search_tool = SerperDevTool()
scraping_tool = SeleniumScrapingTool()

class HumeAISentimentTool(BaseTool):
    name: str = "Hume AI Sentiment Analysis Tool"
    description: str = (
        "An AI tool that analyzes the sentiment of text data using the Hume API."
    )

    async def _do_sentiment_analysis(self, text: str):
        client = HumeStreamClient(api_key=os.getenv("HUME_API"))
        config = LanguageConfig()
        async with client.connect([config]) as socket:
            result = await socket.send_text(text)
            emotions = result["language"]["predictions"][0]["emotions"]
            return emotions

    async def _run(self, text: str):
        return await self._do_sentiment_analysis(text)


# Agents
class SentimentAnalysisAgents:
    verbose: bool = True

    def research_analyst(self):
        return Agent(
            role="Staff Research Analyst",
            goal="Being the BEST at gathering, analyzing, and summarizing news articles, social media posts, company announcements, and market sentiments.",
            backstory="Known as the BEST Research Analyst, you are skilled in sifting through news, social media posts, company announcements, and market sentiments. Now, you are working on super important customer project to analyze the sentiment of the public towards a specific company.",
            verbose=self.verbose,
            llm=gpt4_turbo_llm_openai,
            tools=[search_tool, scraping_tool],
        )

    def sentiment_analyst(self):
        return Agent(
            role="Sentiment Analysis Specialist",
            goal="Analyze the sentiment of the public towards a specific company based on the data provided by the research analyst.",
            backstory="""Excel in interpreting nuanced emotions and opinions expressed in text.""",
            verbose=self.verbose,
            llm=llama_3_70b_llm_groq,
            tools=[HumeAISentimentTool()],
        )

    def report_writer(self):
        return Agent(
            role="Senior Report Writer",
            goal="Write a detailed report in markdown based on the insights provided by the research analyst and sentiment analysis specialist on the sentiment of the public towards a specific company.",
            backstory="Known for your exceptional writing skills and ability to present complex information in a clear and concise manner.",
            verbose=self.verbose,
            llm=mixtral_8x7b_llm_groq,
            response_template="""{{ .Response }}
            Format the final report in markdown with the following sections:
            [OUTPUT_FORMAT]
            # Sentiment Analysis Report
            ## Introduction
            - Provide an overview of the report and the topic of analysis.
            ## Methodology
            - Describe the methodology used to gather and analyze the data.
            ## Findings
            - Summarize the key insights from the data analysis.
            ## Conclusion
            - Provide a conclusion based on the findings.
            ## References
            - Include references to the data sources used in the analysis.
            [END_OUTPUT_FORMAT]
            """,
        )
