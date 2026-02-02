from textwrap import dedent
from crewai import Agent

from tools import ExaSearchToolset

class MeetingPrepAgents():
    def research_agent (self):
        return Agent(
            role="Research Specialist",
            goal='Conduct thorough research on people and companies involved in the meeting', 
            tools=ExaSearchToolset.tools(),
            backstory=dedent(f"""\
            As a researcher Specialist, your mission is to uncover detailed information about the individuals and entities in the meeting.
            Your insights will lay the groundwork for strategic meeting preparation.
            """),
            verbose=True
        )

    def industry_analysis_agent (self):
        return Agent(
            role="Industry Analyst",
            goal='Analyse the current trends, challenges, and opportinuties', 
            tools=ExaSearchToolset.tools(),
            backstory=dedent(f"""\
            As a industry analyst, your analysis will identify key trends, challenges facing the industry, and potential opportinuties
            that could be leverage during the meeting for strategic advantage
            """),
            verbose=True
        )

    def meeting_strategy_agent (self):
        return Agent(
            role="Meeting Strategy Advisor",
            goal='Develop talking points, questions, and strategic angles for the meeting',
            backstory=dedent(f"""\
            As strategy Advisor, your expertise will guide the development of talking points, insightful questions, and strategic angles 
            to ensure the meeting's objectives are achieved
            """),
            verbose=True
        )

    def summary_and_briefing_agent (self):
        return Agent(
            role="Briefing Coordinator",
            goal='Compile all gathered information into a concise, informative briefing document', 
            backstory=dedent(f"""\
            As a Briefing coordonator, your role is to consolidate the research, analysis, and strategic insights
            """),
            verbose=True
        )