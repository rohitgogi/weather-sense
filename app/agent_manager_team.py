from smolagents import tool, CodeAgent, FinalAnswerTool, InferenceClientModel, DuckDuckGoSearchTool
from agent_tools import current_weather, c_to_f


model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")
final_answer = FinalAnswerTool()

weather_analyst = CodeAgent(
    model=model,
    tools=[current_weather, c_to_f, final_answer],
    name="weather_analyst",
    description="Fetches and analyzes current weather data for a given city.",
)

stylist_agent = CodeAgent(
    model=model,
    tools=[final_answer],
    name="stylist_agent",
    description="Provides outfit recommendations based on weather data.",
)

manager_agent = CodeAgent(
    model=model,
    tools=[final_answer],
    managed_agents=[weather_analyst, stylist_agent],
    verbosity_level=2,
    name="style_manager",
    description="Delegates weather analysis and outfit advice to sub-agents.",
)

if __name__ == "__main__":
    response = manager_agent.run("Advise what to wear in Tokyo today.")
    print(response)
