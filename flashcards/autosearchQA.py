
def findQA():
    # 1-ый вариант поиска строк-вопросов
    # прочитали файл
    with open('questions.txt') as f:
        content = f.read()


    # посчитали количество вопросов
    amount = content.count('## Q')
    list_answer = []
    for i in range(amount): 

        # 1-ая граница - начало вопроса

        # 2-ая - конец вопроса/начало ответа
        snd = content.find('\n') + 2

        # 3-ая - конец ответа
        thd = content.find('\n## Q') + 6 

        list_answer.append(content[snd:thd])
        content = content[thd:]



    # 2-ой вариант поиска строк-вопросов

    import re
    f = open('questions.txt', 'r')
    s = f.read()
    content_question = re.findall(r'## Q.*\n', s)

    return (zip(content_question, list_answer))

print(list(findQA()))
# python3 manage.py shell
#
# In [1]: from flashcards.models import FlashCard, Cateogry
#
# In [2]: from flashcards.autosearchQA import findQA
#
# In [3]: from django.contrib.auth.models import User
# 
# In [4]: for x, y in findQA():
#   ...:     FlashCard.objects.create(question = x, answer = y, user = User.objects.get(id=1), category = Category.objects.get(id=1))
#   ...: 