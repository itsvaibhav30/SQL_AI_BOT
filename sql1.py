from dotenv import load_dotenv
load_dotenv() #load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
 #Configure genai key
genai.configure(api_key=os.getenv("Google_API_KEY"))

# Function to load Google gemini model and provide sql queries as response
def get_gemini_response(question,prompt):
    
    model=genai.GenerativeModel('gemini-pro')#gemini pro is used for text 
    response = model.generate_content([prompt[0],question])
    # print(response.text)
    return response.text
    

#Function to retrive queries from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define your prompt
prompt=[
    
"""
You are an expert in converting English questions to SQL query! 
The SQL database has the name STUDENT and has the following columns - Name, Class, 
Sec \n\nFor example,\nExample 1 - How many entries of records are present?, 
the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; 
\nExample 2 - Tell me all the students studying in BCA class?, 
the SQL command will be something like this SELECT * FROM STUDENT where CLASS="BCA"; 
also the sql code should not have ``` in beginning or end and sql word in output

"""

]

#Setting the streamlit app
st.set_page_config(page_title="I can retrive any sql query")
st.header("Gemini app to retrive any sql data")
question=st.text_input("Input:",key="input")
submit=st.button("submit")


#If submit is called then
if submit:
    response=get_gemini_response(question,prompt)
    response=read_sql_query(response,"student.db")

    st.subheader("The response is: ")
    for row in response:
        print(row)
        st.header(row)

