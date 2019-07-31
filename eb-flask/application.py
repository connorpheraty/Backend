import json
import os
import requests
from .schema import DB
from flask import Flask, request
from flask_cors import CORS
from flask_json import FlaskJSON, JsonError, json_response

application = app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)
DB.init_app(app)


@app.route('/')
def root():
    """
    Testing
    """
    return "Test Successful"


@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # Get Json request
    # Tokenize request
    # Match tokens with keywords in dataframe
    # Isolate relevant results
    # Return relevant information pertaining to isolated results
    db_request = RetrieveData(DB, ['query_params_from_request']).get_data()
    return json_response(agency=db_request.data.agency,
                         brief_title=db_request.data.brief_title,
                         official_title=db_request.data.official_title,
                         brief_summary=db_request.data.brief_summary,
                         city=db_request.data.city,
                         state=db_request.data.state,
                         country=db_request.data.country,
                         detailed_description=db_request.data.detailed_description,
                         eligibility=db_request.data.eligibility,
                         condition=db_request.data.condition,
                         keyword=db_request.data.keyword,
                         mesh_term=db_request.data.mesh_term,
                         overall_status=db_request.data.overall_status,
                         phase=db_request.data.phase,
                         url=db_request.data.url,)

    # data = request.get_json(force=True)

    # query = data['query']
    # print(query)
    # Unpacking string query


class RetrieveData:
    def __init__(self, database, *args):
        # TODO add query parameters.
        self.session = database.session()
        self.data = self.session.query(DB.Study).limit(20)
        self.agency = self.data.agency
        self.brief_title = self.data.brief_title
        self.official_title = self.data.official_title
        self.brief_summary = self.data.brief_summary
        self.city = self.data.city
        self.state = self.data.state
        self.country = self.data.country
        self.detailed_description = self.data.detailed_description
        self.eligibility = self.data.eligibility
        self.condition = self.data.condition
        self.keyword = self.data.keyword
        self.mesh_term = self.data.mesh_term
        self.overall_status = self.data.overall_status
        self.phase = self.data.phase
        self.url = self.data.url

    def get_data(self):
        return self


if __name__ == '__main__':
    application.run()
