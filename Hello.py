import streamlit as st
from langchain.llms import OpenAI
st.set_page_config(page_title="🦜🔗 PK_LLM")
st.title('🦜🔗 PK_LLM for doing question and answering from literatures')
openai_api_key = st.sidebar.text_input('OpenAI API Key')
import os

#os.environ['OPENAI_API_BASE'] = "https://api.openai-forward.com/v1"
# os.environ['OPENAI_PROXY'] = "http://localhost:33210"

import time
from langchain_community.callbacks import get_openai_callback


# load
import pickle
from pathlib import Path
pkl_path = Path("docs_demo.pkl")



def generate_response(input_text):
    start_time = time.time()
    with get_openai_callback() as cb:
        st.info(docs.query(input_text,k=5))
    # 记录结束时间
    end_time = time.time()
    # 计算运行时间
    execution_time = end_time - start_time
    stats = {
        'execution_time_minutes': round(execution_time / 60, 3),
        'total_tokens_used': cb.total_tokens,
        'total_cost_USD': round(cb.total_cost, 4),
    }
    st.info(f'时间花费 {stats.get("execution_time_minutes")}')
    st.info(f'本次问答总花费的tokens {stats.get("total_tokens_used")}')
    st.info(f'本次问答总花费的tokens成本 {stats.get("total_cost_USD")}')
    
    

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    os.environ['OPENAI_API_KEY'] = openai_api_key
    from paperqa import Docs
    with pkl_path.open("rb") as f:
        docs = pickle.load(f)
    docs.embeddings.openai_api_key = openai_api_key
    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo", openai_api_key =openai_api_key )
    docs.update_llm(llm)
    generate_response(text)