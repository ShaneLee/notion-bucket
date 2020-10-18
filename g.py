import os, sys
from notion.client import NotionClient

with open(os.path.join(sys.path[0], 'token.txt')) as file:
  token = file.read().strip('\n')
  client = NotionClient(token_v2=token)
  cv = client.get_collection_view('https://www.notion.so/bbd582fdb6f5402398b1ee027d0f4f1b?v=47520541bc754613ab375d5430f89704')

  row = cv.collection.add_row()
  row.goal = input('Idea: ')
  row.category = input('Category: ')
  row.week = input('Week: ')
