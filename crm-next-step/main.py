from datetime import date, timedelta

def update(lead, event, today):
    states = {'new':{'contacted':'contacted'},'contacted':{'proposal':'proposal sent'},
              'proposal sent':{'won':'won','lost':'lost'}}
    next_state = states.get(lead['stage'],{}).get(event)
    if next_state is None: return {'error':'invalid stage transition'}
    return {**lead, 'stage':next_state,
            'follow_up_on':None if next_state in ('won','lost') else str(today+timedelta(days=3))}

def run(): return update({'company':'Sample Ltd','stage':'contacted'}, 'proposal', date(2026,10,5))

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
