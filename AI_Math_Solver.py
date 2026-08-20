import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import Tool,initialize_agent
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.chains import LLMChain, LLMMathChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import re
from dotenv import load_dotenv
load_dotenv()

st.title("Text to Math Problem Solver")

groq_api=st.sidebar.text_input('Please enter your Groq API Key',type='password')
if not groq_api:
    st.info('Please Provide Groq API key')
    st.stop()

model=ChatGroq(model='qwen/qwen3.6-27b',groq_api_key=groq_api,reasoning_format="hidden")

######----------- INITIALIZING AGENTS -----------###############

search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="Search",
    func=search.run,
    description="Useful for answering current events, history, people, science and general knowledge questions."
)

math_chain=LLMMathChain.from_llm(llm=model)

def math_tool_func(question):
    math_expr=''.join(re.findall(r'[\d\.\+\-\*\/\^\(\)]+',question))
    return math_chain.run(math_expr)

calculator_tool=Tool(
    name='calculator',
    func=math_tool_func,
    description='A tool used for answering math related questions. Only input mathematical expression needed'
)

prompt=''' You are an expert agent tasked with solving user mathematical problems.
If the question doesn't related to mathematics in any way reply with 
"The given question is not from mathematics and I am a mathematics Bot. So, kindly ask me Maths related questions."
Logically arrive at the solution and display it point wise for the question below:
Question :{question}
Answer: '''

prompt_template=PromptTemplate(template=prompt,input_variables=['question'])

chain=LLMChain(prompt=prompt_template,llm=model)

reasoning_tool=Tool(
    name='Reasoning Tool',
    func=chain.run,
    description='A tool used for answering logic based and reasoning questions'
)
######-------- Build The AGENT --------########
assistant_agent=initialize_agent(
    tools=[search_tool,calculator_tool,reasoning_tool],
    llm=model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not  in st.session_state:
    st.session_state['messages']=[
        {'role':'assistant','content':'Hi, I am a Math Chatbot, who can answer all of your questions'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

question=st.text_area('Please ask your Question: ')

if st.button('Generate Answer'):
    if question:
        with st.spinner("Generating Response..."):
            st.session_state.messages.append({'role':'user','content':question})
            st.chat_message('user').write(question)

        if re.search(r'[\d\+\-\*\/\^]',question):
            response=calculator_tool.run(question)
        else:
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(question,callbacks=[st_cb])

        st.session_state.messages.append({'role':'assistant','content':response})
        st.chat_message('assistant').write(response)
    else:
        st.warning('Please Enter the Question ')
