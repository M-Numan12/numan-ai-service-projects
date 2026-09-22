def draft_brief(company, service, audience, benefit):
    if not all((company,service,audience,benefit)):
        raise ValueError('all brief fields are required')
    return {'headline':f'{service} for {audience}',
            'intro':f'{company} helps {audience} {benefit} with {service}.',
            'review_note':'Check claims, tone and facts before publishing.'}

def run(): return draft_brief('North Studio','web development','local businesses',
                              'take more enquiries online')

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
