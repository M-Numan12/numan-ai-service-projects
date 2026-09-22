def route(lead):
    if not lead.get('consent'): return {'status':'hold', 'reason':'consent missing'}
    if lead.get('budget',0) < 1000: return {'status':'nurture', 'owner':'general inbox'}
    owners = {'website':'web team','app':'mobile team','software':'software team'}
    return {'status':'assigned', 'owner':owners.get(lead.get('service'),'general inbox')}

def run(): return [route(x) for x in [{'service':'app','budget':5000,'consent':True},
                                       {'service':'website','budget':300,'consent':True}]]

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
