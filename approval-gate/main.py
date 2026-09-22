def submit(action):
    if action['type'] in ('payment','send_external','delete'):
        return {**action,'status':'pending approval'}
    return {**action,'status':'ready'}

def approve(action, reviewer):
    if action['status'] != 'pending approval': return {'error':'not pending'}
    if reviewer == action.get('requested_by'): return {'error':'independent reviewer required'}
    return {**action, 'status':'approved', 'approved_by':reviewer}

def run():
    item = submit({'type':'send_external','requested_by':'alex','payload':'Example email'})
    return approve(item,'sam')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
