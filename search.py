# Import the Github class from the pygithub library
# https://pygithub.readthedocs.io/en/latest/introduction.html
from github import Github

# Create a GitHub token that has read access to public repos
# https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
GITHUB_TOKEN = "YOUR_TOKEN_HERE"

# Create a search query to find all Python repos that use HuggingFace
# https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-code
SEARCH_QUERY = "import huggingface_hub language:python"

# Create a Github instance using an access token
gh = Github(GITHUB_TOKEN)

# Search code, returns a paginated list of github.ContentFile.ContentFile objects
# https://pygithub.readthedocs.io/en/latest/github.html#github.Github.search_code
# https://pygithub.readthedocs.io/en/latest/github_objects/ContentFile.html
results = gh.search_code(query=SEARCH_QUERY)

print(results.totalCount)

# Print the first 100 results using pagination, write to a file
# https://pygithub.readthedocs.io/en/latest/utilities.html#github.PaginatedList.PaginatedList
# https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
i = 0
with open("results.txt", "w") as output_file:
    output_file.write(f"Total results: {results.totalCount}\n")
    for file in results:
        if i > 100:
            break
        i += 1
        output_file.write(f"{file.repository.git_url}: {file.path}\n")
