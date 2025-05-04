import re


from collections import Counter
text = 'Data science is an exciting field. Science helps us understand data better.'
tokens = re.findall(r'\b\w+\b', text.lower())
trigrams = list(zip(tokens, tokens[1:], tokens[2:]))
trigram_counts = Counter(trigrams)
print("Top 3 Trigrams:", trigram_counts.most_common(3))
