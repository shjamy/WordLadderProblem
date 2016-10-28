import json
import os
from collections import defaultdict
from collections import deque
from itertools import product

def main():
 readWords()
 fword = input("Enter word1: ")
 sword = input("Enter word2: ")
 wordlength = len(fword)
 dictionary = os.path.join(os.path.dirname(__file__), 'len'+str(wordlength)+'.txt')
 with open('dictionary.json') as file:
  jdata = json.loads(file.read())
 wgraph = create_graph(jdata)
 print('The chain is: ')
 for node, arc in traverse(wgraph, fword):
  if node == fword:
   print (' --> '.join(arc))
 
def readWords():
 with open('dictionary.json') as file:
  json_data = json.loads(file.read())
  for keyword in json_data:
   if(len(keyword) == 1):
    f1 = open('len1.txt', 'a')
    f1.write(keyword)
    f1.write('\n')
    f1.close()
   elif(len(keyword) == 2):
    f2 = open('len2.txt', 'a')
    f2.write(keyword)
    f2.write('\n')
    f2.close()
   elif(len(keyword) == 3):
    f3 = open('len3.txt', 'a')
    f3.write(keyword)
    f3.write('\n')
    f3.close()
   elif(len(keyword) == 4):
    f4 = open('len4.txt', 'a')
    f4.write(keyword)
    f4.write('\n')
    f4.close()
   elif(len(keyword) == 5):
    f5 = open('len5.txt', 'a')
    f5.write(keyword)
    f5.write('\n')
    f5.close()
   elif(len(keyword) == 6):
    f6 = open('len6.txt', 'a')
    f6.write(keyword)
    f6.write('\n')
    f6.close()   
   elif(len(keyword) == 7):
    f7 = open('len7.txt', 'a')
    f7.write(keyword)
    f7.write('\n')
    f7.close()  
   elif(len(keyword) == 8):
    f8 = open('len8.txt', 'a')
    f8.write(keyword)
    f8.write('\n')
    f8.close() 
   elif(len(keyword) == 9):
    f9 = open('len9.txt', 'a')
    f9.write(keyword)
    f9.write('\n')
    f9.close()  
   elif(len(keyword) == 10):
    f10 = open('len10.txt', 'a')
    f10.write(keyword)
    f10.write('\n')
    f10.close()                  

def create_graph(words):
 graph = defaultdict(set)
 buckets = defaultdict(list)
 for x in words:
  for i in range(len(x)):
   bucket = '{}_{}'.format(x[:i], x[i + 1:])
   buckets[bucket].append(x)
   for bucket, neigh in buckets.items():  
    for x1, x2 in product(neigh, repeat=2):
     if x1 != x2:
      graph[x1].add(x2)
      graph[x2].add(x1)
 return graph

def traverse(graph, snode):
 visited = set()
 queue = deque([[snode]])
 while queue:
  arc = queue.popleft()
  vertex = path[-1]
  yield node, arc
  for neighbor in graph[node] - visited:
   visited.add(neighbor)
   queue.append(arc + [neighbor])

 


if __name__ == "__main__":
    main() 