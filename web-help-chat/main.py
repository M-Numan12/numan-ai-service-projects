from difflib import SequenceMatcher

FAQ = {'What are your hours?':'We are open Monday to Friday, 9am to 5pm.',
       'How can I request a quote?':'Use the contact form to share your requirements.'}

def answer(question):
    scores = [(SequenceMatcher(None, question.lower(), q.lower()).ratio(), q)
              for q in FAQ]
    confidence, best = max(scores)
    if confidence < .45: return {'answer':'Please contact our team for a precise answer.', 'source':None}
    return {'answer':FAQ[best], 'source':best}

def run(): return answer('How do I request a quote?')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
