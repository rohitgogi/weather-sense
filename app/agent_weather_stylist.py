from smolagents import tool, CodeAgent, FinalAnswerTool, InferenceClientModel, DuckDuckGoSearchTool
from weather import get_weather
from agent_tools import current_weather, c_to_f, compare_temps
import yaml

with open("app/prompts.yaml", "r") as f:
    prompt_templates = yaml.safe_load(f)

search_tool = DuckDuckGoSearchTool(3)
model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")
final_answer = FinalAnswerTool()

agent = CodeAgent(model=model, tools=[current_weather, c_to_f, compare_temps, search_tool, final_answer], verbosity_level = 2) #, prompt_templates=prompt_templates)
response = agent.run("Find the official tourism site for London and tell me today's weather in one sentence.")
print(response)