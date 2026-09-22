from collections import Counter
import re

def brief(notes):
    combined = ' '.join(item['text'] for item in notes)
    terms = Counter(w.lower() for w in re.findall(r'[a-z]{5,}', combined, re.I))
    return {'sources':[item['source'] for item in notes],
            'themes':[w for w,_ in terms.most_common(5)],
            'review_required':True}

def run():
    return brief([{'source':'Interview 1','text':'Customers want faster support and clear pricing.'},
                  {'source':'Interview 2','text':'Clear pricing and faster checkout matter.'}])

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
