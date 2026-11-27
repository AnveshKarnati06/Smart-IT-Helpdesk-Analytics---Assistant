import json

# D1 - JSON Ticket Request
print("----- D1 : JSON Ticket Request -----")

json_string = '''
{
    "employee_id": 101,
    "department": "HR",
    "question": "My laptop is connected to Wi-Fi but internet is not working"
}
'''

ticket = json.loads(json_string)

print("Employee ID:", ticket["employee_id"])
print("Department:", ticket["department"])
print("Question:", ticket["question"])

response = {
    "employee_id": ticket["employee_id"],
    "detected_category": "Network",
    "suggested_action": "Check Wi-Fi connection, reconnect to the approved network and restart the network adapter."
}

print("\nResponse JSON:")
print(json.dumps(response, indent=4))

# D2 - FAQ Knowledge Base
print("\n----- D2 : FAQ Retrieval Exercise -----")

faq = {
    "password reset":
    "Use the company password reset portal. Never share your password with anyone.",

    "wifi internet":
    "Check whether Wi-Fi is enabled, reconnect to the approved network, and restart the network adapter. Contact IT if the issue continues.",

    "software access":
    "Raise an access request through the approved company service desk and include the business reason.",

    "laptop overheating":
    "Save your work, close unnecessary applications, keep ventilation areas clear and contact IT support if overheating continues.",

    "locked account":
    "Use the approved account unlock process or contact the IT service desk. Do not share passwords or one-time codes."
}

user_question = input("\nEnter FAQ Question: ").lower()

found = False

for keyword, answer in faq.items():
    if keyword in user_question:
        print("\nApproved Guidance:")
        print(answer)
        found = True
        break

if not found:
    print("\nI could not find a verified answer. Please contact the IT service desk.")

print("\nWhy Retrieval Is Safer?")
print(
    "Retrieving approved answers is safer because responses come from verified company knowledge. "
    "This reduces incorrect information and avoids AI hallucinations."
)

# D3 - Rule Based Agent
print("\n----- D3 : Rule-Based Agent Workflow -----")

def helpdesk_agent(question):

    question = question.lower()

    # Step 1 - Categorization
    if ("wifi" in question or
        "internet" in question or
        "network" in question):
        category = "Network"

    elif ("password" in question or
          "account" in question or
          "access" in question):
        category = "Access"

    elif ("laptop" in question or
          "hardware" in question or
          "overheating" in question):
        category = "Hardware"

    else:
        category = "Software"

    # Step 2 & 3 - FAQ Search
    action = "Please contact the IT service desk."
    for keyword, answer in faq.items():
        if keyword in question:
            action = answer
            break

    # Step 4 & 5 - JSON Response
    result = {
        "category": category,
        "action": action,
        "status": "Completed"
    }

    return json.dumps(result, indent=4)

agent_question = input("\nAsk the Helpdesk Agent: ")
print("\nAgent Response:")
print(helpdesk_agent(agent_question))
print("\nRule-Based Automation Used:")
print("- Keyword matching")
print("- If-else classification")
print("- FAQ lookup")
print("- JSON response generation")
print("\nComponents Needed for a Real LLM Agent:")
print("- Large Language Model (GPT, Gemini, Claude, Llama)")
print("- Vector Database (FAISS, Pinecone, ChromaDB)")
print("- Embedding Model")
print("- Retrieval-Augmented Generation (RAG)")
print("- Tool/API Calling")
print("- Memory Management")
print("- Access Control and Security")
print("- Agent Frameworks (LangChain, CrewAI, Semantic Kernel)")