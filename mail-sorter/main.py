RULES = [('billing',('invoice','payment')),
         ('support',('error','broken','help')),
         ('sales',('quote','pricing','proposal'))]

def classify(subject, body):
    text = (subject+' '+body).lower()
    category = next((label for label,terms in RULES if any(t in text for t in terms)), 'general')
    draft = f'Thank you for contacting us about {subject.strip()}. Our {category} team will review your message.'
    return {'category':category, 'draft':draft, 'send_automatically':False}

def run(): return classify('Request for a quote','Could you share your pricing?')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
