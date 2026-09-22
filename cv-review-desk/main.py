import re

def evidence(cv_text, required_skills):
    tokens = set(re.findall(r'[a-z+#.]+', cv_text.lower()))
    matched = [skill for skill in required_skills if skill.lower() in tokens]
    missing = [skill for skill in required_skills if skill not in matched]
    return {'matched':matched, 'not_found':missing, 'decision':'manual review required'}

def run():
    return evidence('Built React interfaces and Python APIs for a school.',
                    ['React','Python','PostgreSQL'])

if __name__ == '__main__':
    import json
    import sys
    if len(sys.argv) > 1 and 'extract' in globals():
        result = extract(sys.argv[1])
    else:
        result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
