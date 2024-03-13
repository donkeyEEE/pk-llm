from langchain.prompts import PromptTemplate

summary_prompt = PromptTemplate(
    input_variables=["text", "citation", "question", "summary_length"],
    template="""
    Read the following text carefully. 
    Your task is to summarize this text, 
    focusing specifically on extracting information that is directly relevant to a posed question. 
    This summary will be used as input for another Large Language Model (LLM), 
    so it's crucial that your summary is clear, concise, and accurately 
    highlights the most pertinent points related to the question. 
    When summarizing, please structure your response in a manner that organizes the information logically, 
    possibly through bullet points or a structured paragraph, 
    ensuring that the essence of the text and its relevance to the question are captured effectively. 
    Exclude any information that is not directly relevant to the question to maintain focus and clarity.
    """
    'Reply "Not applicable" if text is irrelevant. '
    "Use {summary_length}. At the end of your response, provide a score from 1-10 on a newline "
    "indicating relevance to question. Do not explain your score. "
    "\n\n"
    "{text}\n\n"
    "Excerpt from {citation}\n"
    "Question: {question}\n"
    "Relevant Information Summary:",
)

qa_prompt = PromptTemplate(
    input_variables=["context", "answer_length", "question"],
    template=
    """
    You are an environmental engineering scholar 
    with expertise in emerging pollutants and pharmacokinetics and toxicology. 
    Your task is to write an answer ({answer_length}) for the question below based on the provided context."""
    "If the context provides insufficient information and the question cannot be directly answered, "
    'reply "I cannot answer". '
    "For each part of your answer, indicate which sources most support it "
    "via valid citation markers at the end of sentences, like (Example2012). \n"
    "Context (with relevance scores):\n {context}\n"
    "Question: {question}\n"
    "Answer: ",
)

select_paper_prompt = PromptTemplate(
    input_variables=["question", "papers"],
    template="Select papers that may help answer the question below. "
    "Papers are listed as $KEY: $PAPER_INFO. "
    "Return a list of keys, separated by commas. "
    'Return "None", if no papers are applicable. '
    "Choose papers that are relevant, from reputable sources, and timely "
    "(if the question requires timely information). \n\n"
    "Question: {question}\n\n"
    "Papers: {papers}\n\n"
    "Selected keys:",
)

# We are unable to serialize with partial variables
# so TODO: update year next year
citation_prompt = PromptTemplate(
    input_variables=["text"],
    template="Provide the citation for the following text in MLA Format. The year is 2023\n"
    "{text}\n\n"
    "Citation:",
)

default_system_prompt = (
    "Answer in a direct and concise tone. "
    "Your audience is an expert, so be highly specific. "
    "If there are ambiguous terms or acronyms, first define them. "
)

completation_prompt = PromptTemplate(
    input_variables=["query"],
    template="Please expand on this question; if the question is not in English, then translate it into English.\n"
    "{query}\n\n"
    "Citation:",
)