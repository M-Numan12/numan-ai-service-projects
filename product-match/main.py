CATALOG = [{'name':'Starter Website','price':1200,'tags':{'website','small-business'}},
           {'name':'Booking Platform','price':3200,'tags':{'website','booking'}},
           {'name':'Mobile App','price':7000,'tags':{'app','mobile'}}]

def recommend(budget, needs):
    choices = [p for p in CATALOG if p['price'] <= budget]
    ranked = sorted(choices, key=lambda p:(-len(p['tags'] & set(needs)), p['price']))
    return [{'name':p['name'], 'price':p['price']} for p in ranked]

def run(): return recommend(4000, ['website','booking'])

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
