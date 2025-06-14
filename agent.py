import os
import requests
from dotenv import load_dotenv


def chat_with_agent(user_id,agent_id,session_id,message):
    url=os.getenv("STUDIO_URL")
    headers={
        "accept": "application/json",
        "Content-Type":"application/json",
        "x-api-key":os.getenv("X-API-KEY"),
    }
    data ={
        "user_id":user_id,
        "agent_id":agent_id,
        "session_id":session_id,
        "messsage":message
    }

    try:
        response=requests.post(url,headers=headers,json=data,timeout=900)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as err:
        print(f"Error Occured": {err}")
        return None


    def travel_research(session_id,message):
        user_id="default_user"
        agent_id=os.getenv("RESEARCH_AGENT_ID")
        response=chat_with_agent(user_id,agent_id,session_id,message)
        return response

    def travel_planner(session_id,message):
        user_id="default_user"
        agent_id=os.getenv("PLANNER_AGENT_ID")
        response=chat_with_agent(user_id,agent_id,session_id,message)
        return response    


