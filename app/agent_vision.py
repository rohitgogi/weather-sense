from smolagents import CodeAgent, FinalAnswerTool, InferenceClientModel
from agent_tools import describe_outfit

model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")  # back to text-only model
final_answer = FinalAnswerTool()

vision_agent = CodeAgent(
    model=model,
    tools=[describe_outfit, final_answer],
    name="vision_agent",
    description="Analyzes outfit images and decides if they fit the weather."
)

if __name__ == "__main__":
    image_path = "app/toji.png"
    response = vision_agent.run(
        f"Describe the outfit shown in {image_path} and say if it fits warm weather."
    )
    print("\nFinal Output:\n", response)
