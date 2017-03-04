from collections import Counter
words = ['Wow', 'Is', 'this', 'true', 'Really', 'This', 'is', 'crazy']
lower_words = {}
for word in words:
  if word.lower() in lower_words:
    lower_words[word.lower()] += 1
  else:
    lower_words[word.lower()] = 1 
  
print(lower_words)