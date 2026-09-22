from collections import Counter
import re

DOCS = [{'id':'returns','text':'Returns are accepted within 14 days with a receipt.'},
        {'id':'shipping','text':'Shipping takes three to five business days.'}]

def tokens(text): return set(re.findall(r'[a-z0-9]+',text.lower()))

def answer(question):
    ranked = sorted(DOCS, key=lambda d:len(tokens(question) & tokens(d['text'])), reverse=True)
    match = ranked[0]
    if not tokens(question) & tokens(match['text']):
        return {'answer':'No matching policy found.', 'source':None}
    return {'answer':match['text'], 'source':match['id']}

def run(): return answer('When can I make returns?')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
