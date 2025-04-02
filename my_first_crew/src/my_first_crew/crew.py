from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class LearningDevelopmentCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def curriculum_analyst(self) -> Agent:
        return Agent(config=self.agents_config["curriculum_analyst"])

    @agent
    def learning_researcher(self) -> Agent:
        return Agent(config=self.agents_config["learning_researcher"])

    @task
    def material_analysis_task(self) -> Task:
        return Task(config=self.tasks_config["material_analysis_task"])

    @task
    def outline_generation_task(self) -> Task:
        return Task(config=self.tasks_config["outline_generation_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.curriculum_analyst(), self.learning_researcher()],
            tasks=[self.material_analysis_task(), self.outline_generation_task()],
            verbose=True
        )
