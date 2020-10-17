from notion.client import NotionClient

with open('token.txt') as file:
  token = file.read().strip('\n')
  client = NotionClient(token_v2=token)
  cv = client.get_collection_view('https://www.notion.so/1824799b019e44e3a5a98a655f4e9d49?v=27b099ae037f4907b6f55f0f73242c98')

  row = cv.collection.add_row()
  row.idea = input('Idea: ')
  row.category = input('Category: ')
