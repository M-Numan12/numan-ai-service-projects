from datetime import date

def qualify(lead):
    score = 0
    if lead.get('budget', 0) >= 3000: score += 35
    if lead.get('timeline_days', 999) <= 30: score += 25
    if lead.get('decision_maker'): score += 25
    if lead.get('need') in {'website', 'software', 'app'}: score += 15
    return {'company': lead['company'], 'score': score,
            'next_step': 'personal outreach' if score >= 65 else 'nurture'}

def run():
    leads = [{'company':'Harbor Studio','budget':4500,'timeline_days':21,'decision_maker':True,'need':'website'},
             {'company':'Elm Bakery','budget':800,'timeline_days':90,'decision_maker':False,'need':'website'}]
    return sorted(map(qualify, leads), key=lambda x: -x['score'])

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
