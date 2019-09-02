# Flask API

## Usage

Clone the repo:

```git clone https://github.com/build-week-072019-clinical-trial-finder/clinical-trial-finder-DS```

Create virtualenv:

```virtualenv virt``` <br>
```source virt/bin/activate``` <br>
```pip install -r requirements.txt``` <br>

Run the server locally:

```python application.py```

Try the endpoints:

```Post Request```
```
{
  "user_search": "lung cancer trial new york"
}
```

## Files
### trial_ranker.py
trial_ranker contains the search engine logic and returns a dataframe ranked in order of relevance to the user's search.

### tokenize_lemmatize.py
tokenize_lemmatize takes a user's search query and performs basic natural language processing for comparison to clinical trials in the dataframe.
