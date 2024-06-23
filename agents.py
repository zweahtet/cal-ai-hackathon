import os
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
        agent = Agent(
            role="Staff Research Analyst",
            goal="Being the BEST at gathering, analyzing, and summarizing news articles and social media posts, only related to ESG.",
            backstory="Known as the BEST Research Analyst, you are skilled in sifting through news and social media posts. Now, you are working on super important customer project to analyze the ESG towards a specific company.",
            verbose=self.verbose,
            llm=gpt4_turbo_llm_openai,
            tools=[scraping_tool, search_tool],
        )
        return agent

    def sentiment_analyst(self):
        agent = Agent(
            role="ESG Analysis Specialist",
            goal="Analyze the ESG towards a specific company based on the data provided by the research analyst.",
            backstory="Experienced in analyzing ESG data, you are known for your expertise in identifying key trends and insights.",
            verbose=self.verbose,
            llm=llama_3_70b_llm_groq,
            # tools=[HumeAISentimentTool()],
        )
        return agent

    def report_writer(self):
        agent = Agent(
            role="Senior Report Writer",
            goal="Write a detailed report in markdown based on the insights provided by the research analyst and sentiment analysis specialist on the sentiment of the public towards a specific company.",
            backstory="Known for your exceptional writing skills and ability to present complex information in a clear and concise manner.",
            verbose=self.verbose,
            # llm=mixtral_8x7b_llm_groq,
            # llm=llama_3_70b_llm_groq,
            llm=gpt4_turbo_llm_openai,
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
            allow_delegation=False,
        )
        return agent
