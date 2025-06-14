import uuid
import streamlit as st
from agent import travel_research,travel_planner


# Set up the Streamlit app
st.title("AI Travel Planner ✈️")
st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary")


# Input fields for the user's destination and the number of days they want to travel for
destination = st.text_input("Where do you want to go?")
num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)


if "session_id" not in st.session_state:
    st.session_state.session_id=str(uuid.uuid4())


if st.button("Generate Itinerary"):
    with st.spinner("Researching your destination..."):
        # First get research results
        input_query= f"Research {destination} for a {num_days} day trip"
        research_results = travel_research(st.session_state.session_id,input_query)
        # Show research progress
        st.write("✓ Research completed")
    
    with st.spinner("Creating your personalized itinerary..."):
        # Pass research results to planner
        prompt = f"""
        Destination: {destination}
        Duration: {num_days} days
        Research Results: {research_results}
        
        Please create a detailed itinerary based on this research.
        """
        travel_itinerary_response=travel_planner(st.session_state.session_id,prompt)
        st.write(travel_itinerary_response)    
    
