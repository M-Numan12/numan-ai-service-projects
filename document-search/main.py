import re

DOCUMENTS = {'handbook':'Support hours are 9am to 5pm on weekdays. Refunds need a receipt.',
             'services':'We develop websites, mobile apps and internal software.'}

def search(question):
    query = set(re.findall(r'[a-z]{3,}',question.lower()))
    matches = []
    for title,body in DOCUMENTS.items():
        score = len(query & set(re.findall(r'[a-z]{3,}',body.lower())))
        if score: matches.append({'source':title,'excerpt':body,'score':score})
    return sorted(matches,key=lambda x:-x['score'])

def run(): return search('What are the support hours?')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
