# WeatherSense

## Overview
I’m exploring Hugging Face’s SmolAgents to see how different agentic frameworks actually work in practice.  
The goal was to mess around with as many features as possible and push SmolAgents to its limits — especially around multi-agent communication, tool integration, and vision-based reasoning.

---

## Goal
Test out multi-agent reasoning, tool use, and vision analysis to see what works, what breaks, and what actually feels usable when building real AI systems.

---

## Architecture

| Agent | Role | Tools Used |
|--------|------|------------|
| `weather_analyst` | Pulls and interprets current weather data for any city. | `current_weather`, `c_to_f` |
| `stylist_agent` | Recommends what to wear based on the data. | `final_answer` |
| `style_manager` | Delegates tasks between the two agents and composes a final response. | `weather_analyst`, `stylist_agent` |
| `vision_agent` | Describes outfit images and decides if they fit the weather. | `describe_outfit`, `final_answer` |

---

## Features
- Real weather pulled from an API  
- Multi-step reasoning (`Thought → Code → Observation`)  
- Agents that communicate and delegate tasks  
- Custom prompts to shape reasoning behavior  
- Modular tools defined with `@tool` decorators  
- Vision agent that interprets clothing images and relates them to weather context  

---

## Folder Layout
```
app/
│
├── weather.py                # Fetches weather data
├── agent_tools.py            # Tool definitions
├── agent_weather_stylist.py  # Single-agent demo
├── agent_manager_team.py     # Multi-agent system
├── agent_vision.py           # Vision model testing
└── prompts.yaml              # Custom prompt template (did not work for me)
```

---

## Example
```bash
python app/agent_manager_team.py
```

**Output**
```
For Tokyo today with a temperature of 12°C (54°F) and clear skies,
wear a light jacket or cardigan with jeans and sneakers.
Add sunglasses or a cap for the afternoon.
```

---

## Development Notes

| Phase | Focus | Result |
|--------|--------|--------|
| 1. Baseline | Single agent fetching weather | Working prototype |
| 2. Tools | Added conversion + comparison tools | Modular setup done |
| 3. Multi-Agent | Manager-based coordination | Agents cooperating |
| 4. Prompts | Added stylist behavior | More natural output |
| 5. Vision | Added outfit image reasoning | Extended use cases |
| 6. Cleanup | Logging + structure | Repo ready to share |

---

## Takeaways
- Creating the agents themselves was simple like defining tools and connecting logic worked smoothly and was easy to understand.
- Combining them under a manager agent was actually a great design choice; it made communication between multiple agents surprisingly straightforward.
- The hard part was modifying the system prompt. It feels like the framework fights you when you try to customize it. I absolutely dreaded this part.
- The documentation around prompt templates isn’t clear, and the .yaml file setup was frustrating — every run seemed to complain - Adding the vision part was fun — I tried connecting true multimodal models like LLaVA and Qwen-VL but none worked with InferenceClientModel, so I had to wrap a local transformers pipeline as a tool instead.
- That workaround actually worked great, and showed that using local tools for image tasks is a practical approach.
- Overall, SmolAgents is promising for modular, tool-driven reasoning, but still rough around the edges for extensibility and multimodal workflows.