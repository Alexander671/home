
import re

with open('questions.txt') as f:
    content = f.read()

f = open('questions.txt', 'r')
s = f.read()
content_question = re.findall(r'## Q.*\n', s)
print(content_question)
print(len(content_question))
