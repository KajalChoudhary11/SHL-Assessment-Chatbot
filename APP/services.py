from groq import Groq
from APP.settings import GROQ_API_KEY
from APP.vectorstore.faiss_store import search


client = Groq(api_key=GROQ_API_KEY)                                #Initialize Groq client

VAGUE_QUERIES = [                                                   #list of queries that are considered generic and require clarification from the user
    "need assessment",
    "suggest assessment",
    "recommend test","assessment",
    "Want hiring test","recommend assessment"]

off_topickeywords = ["football", "weather",                         #list of keywords to detect non-SHL related queries
                    "news", "politics",
                    "entertainment", "sports",
                    "music", "movies", "travel", "food"]


# MAIN CHAT SERVICE
def process_chat(messages):                                         #main function of chat service

    latest_user_message = messages[-1].content.strip()              #get the latest user message
    lower_query = latest_user_message.lower()                       #convert to lowercase for easier matching   

    if lower_query in VAGUE_QUERIES:                                #check if the query is vague and requires clarification
        return {
            "reply": "Could you please provide more details about the type of assessment you're looking for? For example, the job role, skills, or specific requirements you have in mind.",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    if "vs" in lower_query:                                         #check if the user is trying to compare two assessments, which is currently not supported and requires clarification
        return {
            "reply": "It seems like you're trying to compare two assessments. Could you please specify the names of the assessments you'd like to compare?",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    # Retrieve relevant assessments
    retrieved_docs = search(latest_user_message, top_k=5)          #checks the query against the FAISS vector store and retrieves the top 5 assessments using embedding similarity search

    # Build context
    context = ""

    for doc in retrieved_docs:                                     #Loop through the retrieved assessments
        
        context += f"""                                            
        Assessment Name:{doc['name']}
        Description:{doc['description']}
        Job Levels:{doc['job_levels']}
        Duration:{doc['duration']}
        URL:{doc['link']}"""                                        #context building for the LLM

    # Prompt engineering
    prompt = f"""
        You are an SHL assessment recommendation assistant.
        ONLY recommend assessments from the provided SHL catalog.
        If the query is vague, ask clarification questions.
        Otherwise provide relevant recommendations.
        
        CONTEXT:{context}
        USER QUERY:{latest_user_message}"""

    # Generate response (LLM inference)
    completion = client.chat.completions.create(
        model ="llama-3.1-8b-instant",
        messages=[
            {"role":"user",
            "content": prompt}
        ]
    )

    reply = completion.choices[0].message.content                   #generated response from the LLM    
    formatted_recommendations = []
    for doc in retrieved_docs:
        formatted_recommendations.append({
            "name": doc['name'],
            "url": doc['link'],
            "duration": doc['duration'],
        })
    return{
        "reply": reply,
        "recommendations": formatted_recommendations,
        "end_of_conversation": False
    }