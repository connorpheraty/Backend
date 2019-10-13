from flask import Flask, request, render_template
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
def fetch_data():
  """
  API route that receives search query and returns clinical trials that match search
  """

  data = request.get_json(force=True)

  user_search = data['user_search'] 

  tokenized_search = tokenizer(user_search)

  index = search_freq(tokenized_search, df)

  sorted_df = score_docs(index, df)  

  return sorted_df.to_json(orient='records')
  
if __name__ == '__main__':
        application.run(debug=True)