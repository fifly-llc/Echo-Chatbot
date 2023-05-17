import wikipedia

def wiki(query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query

while(True):
  question=input(">> ")
  answer=wiki(question)
  print(answer)
