import os, sys
from datetime import datetime
from notion.client import NotionClient

with open(os.path.join(sys.path[0], 'token.txt')) as file:
  token = file.read().strip('\n')
  client = NotionClient(token_v2=token)
  cv = client.get_collection_view('https://www.notion.so/11a0b8664bda493ab7ad0a44a49407c8?v=bd86c444659248da97d158d20ceef6d4')

  row = cv.collection.add_row()
  row.win = input('Win: ')
  row.year = datetime.now().year 
