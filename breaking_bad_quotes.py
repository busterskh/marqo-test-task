import json
import marqo
import pprint
import requests

# Connect to marqo client
mq = marqo.Client(url='http://localhost:8882')

# Take API from serial Breaking Bad
quotes = requests.get('https://www.breakingbadapi.com/api/quotes')

# Create index and add documents in .json
mq.index("breaking-bad-quotes").add_documents(json.loads(quotes.text))

# Search some quotes you need and take result
results = mq.index("breaking-bad-quotes").search(
    q="Ooooooh, Wire."
)

# Print best match
pprint.pprint(results['hits'][0])

