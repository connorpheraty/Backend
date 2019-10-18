from flask import Flask, request, render_template
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from flask_cors import CORS
import json

#Local Imports


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

  lemmatized_user_search = tokenize_lemmatize(user_search)

  sorted_df = trial_ranker(lemmatized_user_search) 
          

  return json_response(brief_summary=sorted_df['brief_summary'], city=sorted_df['city'],
                       condition=sorted_df['condition'], country=sorted_df['country'],
                       official_title = sorted_df['official_title'], url = sorted_df['url'],
                       state=sorted_df['state'], probability=sorted_df['Probability Completed'])
  
if __name__ == '__main__':
        application.run()