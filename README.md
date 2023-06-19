# signature code search
This is a demo of [Github Code Search](https://github.com/search) using [Anaconda](https://www.anaconda.com/download) as a virtual environment
and [PyGithub](https://github.com/PyGithub/PyGithub) to abstract the API calls

Activate the Anaconda environment using:

``` conda activate ./env```

Run [demo](query.py) once the environment is activated with:

```python3 search.py```

The [demo](query.py) performs 2 queries that look for HuggingFace signatures using the GitHub code search API.
The **MODULE_SEARCH_QUERY** searches for the huggingface_hub api being included as a module within any projects,
while the **API_SEARCH_QUERY** looks for any calls to the huggingface website.
These queries were constructed using the help of the [REST API search endpoint](https://docs.github.com/en/rest/search?apiVersion=2022-11-28)
and [GitHub Code Search Syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax)

# IMPORTANT
It is worth noting that there is a discrepancy in results returned by each query.
Each query when performed through the github website returns 50k+ files, but only seems to return around 800 when running the [demo](query.py).
We are unsure why, but a good place to start might be in what is actually indicated by ```results.totalCount```.
It may that this returns the number of pages, and that the actually number of files is consistent regardles of how the query is made.

Here is the [module query](https://github.com/search?type=code&auto_enroll=true&q=import+huggingface_hub+language%3Apython+) when made through the website

Here is the [api_query](https://github.com/search?type=code&auto_enroll=true&q=huggingface.co+language%3Apython) when made through the website