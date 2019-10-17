from flask import Flask, request, render_template, Blueprint
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from flask_cors import CORS
import json

#Local Imports
from dataFrameLoader import df
from indexHelper import search_freq, score_docs, tokenizer

# Elastic Beanstalk initalization
application = app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)

@app.route('/')
def root():
    """
    Testing
    """
    return "Test Successful"

@app.route('/fetch_data', methods=['POST'])
def fetch_data_old():
  """
  API route that receives search query and returns clinical trials that match search
  """
  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  sorted_df = sorted_df[:15] 

  return json_response(brief_summary=sorted_df['brief_summary'], city=sorted_df['city'],
                       condition=sorted_df['condition'], country=sorted_df['country'],
                       official_title = sorted_df['official_title'], url = sorted_df['url'],
                       state=sorted_df['state'])

@app.route('/fetch_data_1', methods=['POST'])
def fetch_data():
  """
  API route that receives search query and returns clinical trials that match search
  """
  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[:12]  

  return page.to_json(orient='records')

@app.route('/fetch_data_2', methods=['POST'])
def fetch_page2():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[12:24]  

  return page.to_json(orient='records')

@app.route('/fetch_data_3', methods=['POST'])
def fetch_page3():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[24:36]  

  return page.to_json(orient='records')

@app.route('/fetch_data_4', methods=['POST'])
def fetch_page4():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[36:48]  

  return page.to_json(orient='records')

@app.route('/fetch_data_5', methods=['POST'])
def fetch_page5():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[48:60]  

  return page.to_json(orient='records')

@app.route('/fetch_data_6', methods=['POST'])
def fetch_page6():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[60:72]  

  return page.to_json(orient='records')

@app.route('/fetch_data_7', methods=['POST'])
def fetch_page7():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[72:84]  

  return page.to_json(orient='records')

@app.route('/fetch_data_8', methods=['POST'])
def fetch_page8():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[84:96]  

  return page.to_json(orient='records')

@app.route('/fetch_data_9', methods=['POST'])
def fetch_page9():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[96:108]  

  return page.to_json(orient='records')

@app.route('/fetch_data_10', methods=['POST'])
def fetch_page10():

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  sorted_df = score_docs(search_freq(tokenizer(user_search), df), df)

  page = sorted_df[108:120]  

  return page.to_json(orient='records')

if __name__ == '__main__':
    application.run()