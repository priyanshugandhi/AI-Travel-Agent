## 🛫 AI Travel Agent
This Streamlit app is an AI-powered travel Agent that generates personalized travel itineraries using Lyzr open studio Agent framework. It automates the process of researching, planning, and organizing your dream vacation, allowing you to explore exciting destinations with ease.

### Features
- Research and discover exciting travel destinations, activities, and accommodations
- Customize your itinerary based on the number of days you want to travel
- Utilize the power of Lyzr Agents to generate intelligent and personalized travel plans

### How to get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/priyanshugandhi/AI-Travel-Agent
cd AI-Travel-Agent
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Get your Lyzr Agent ID Key

- Sign up for an [Lyzr account](https://studio.lyzr.ai/)

4. Run the Streamlit App
```bash
streamlit run travel_planner.py
```

### How it Works?

The AI Travel Agent has two main components:
- Researcher: Responsible for generating search terms based on the user's destination and travel duration, and searching the web for relevant activities and accommodations using Perplexity tool.
- Planner: Takes the research results and user preferences to generate a personalized draft itinerary that includes suggested activity