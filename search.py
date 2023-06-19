# Import the Github class from the pygithub library
# https://pygithub.readthedocs.io/en/latest/introduction.html
from github import Github

# Create a GitHub token that has read access to public repos
# https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
GITHUB_TOKEN = "YOUR_TOKEN_HERE"

# Create a search query to find all Python repos that use HuggingFace
# https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-code
MODULE_SEARCH_QUERY = "import huggingface_hub language:python"
API_SEARCH_QUERY = "huggingface.co language:python"

# Create a Github instance using an access token
gh = Github(GITHUB_TOKEN)

# Search code, returns a paginated list of github.ContentFile.ContentFile objects
# https://pygithub.readthedocs.io/en/latest/github.html#github.Github.search_code
# https://pygithub.readthedocs.io/en/latest/github_objects/ContentFile.html
def signature_search(gh, query, output_file="results.txt"):

    results = gh.search_code(query=query)

    # Print the total number of results
    # !!! IMPORTANT !!! Unsure what this is actually counting
    print(f"Total results: {results.totalCount}")

    # Get the first 100 results using pagination, write to a file
    # https://pygithub.readthedocs.io/en/latest/utilities.html#github.PaginatedList.PaginatedList
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
    i = 0
    with open(output_file, "w") as OUTPUT_FILE:
        OUTPUT_FILE.write(f"Total results: {results.totalCount}\n")
        for file in results:
            if i > 100:
                break
            i += 1
            OUTPUT_FILE.write(f"{file.repository.git_url}: {file.path}\n")

if __name__ == "__main__":
    signature_search(gh, MODULE_SEARCH_QUERY, "module_results.txt")
    signature_search(gh, API_SEARCH_QUERY, "api_results.txt")