# @author: Gautam Patel
# Program to transfer all solutions from HackerRank.com to github
# Step1 - Download json export (with all code submissions) from hackerrank
# Step2 - Ensure export file path and github repository location below
# Step3 - Run the program
# Step4 - Commit to github repository

import json
import pathlib

rep_base_folder = 'C:/development/training/HackerRank/'
my_hackerrank_export_json = 'c:/users/gauta/desktop/gautambp_data.json'
hr_base_url = 'https://www.hackerrank.com/'

file_exts = {
        'python': '.py',
        'python3': '.py',
        'java': '.java',
        'java8': '.java',
        'c': '.c',
        'c++': '.c++',
        'scala': '.sc',
        'ruby': '.ruby',
        'oracle': '.sql',
        'javascript': '.js',
        'text': '.txt',
}

def getFileNameAndProblemURL(submission):
    fName = submission['challenge'].lower().replace(' ', '-')
    for ch in '".,:#()?!/\'':
        fName = fName.replace(ch, '')
    problem_url = hr_base_url
    if submission['contest'] == 'Master':
        problem_url += 'challenges/{}/problem'.format(fName)
    else:
        c = submission['contest'].replace(' ', '-')
        problem_url += '{}/{}/problem'.format(c, fName)
    fName += file_exts[submission['language']]
    return fName, problem_url
    
def writeSubmission(s):
    if s['language'] not in file_exts: 
        print('UNKNOWN LANG for submission - ')
        print(s)
        return
    contest = s['contest']
    fileName, problem_url = getFileNameAndProblemURL(s)
    code_path = rep_base_folder + contest.replace(' ', '-')
    if contest == 'Master':
        code_path += '/' + s['language']
    pathlib.Path(code_path).mkdir(parents=True, exist_ok=True) 
    f = open(code_path+'/'+fileName, 'w')
    if s['language'].startswith('python'):
        f.write('# @author: Gautam Patel\n')
        f.write('# Problem Description URL: ' + problem_url)
        f.write('\n')
    elif s['language'].startswith('java') or s['language'] == 'scala':
        f.write('// @author: Gautam Patel\n')
        f.write('// Problem Description URL: ' + problem_url)
        f.write('\n')
    elif s['language'] in ['oracle', 'sql']:
        f.write('-- @author: Gautam Patel\n')
        f.write('-- Problem Description URL: ' + problem_url)
        f.write('\n')
    f.write(s['code'])
    f.close()

with open(my_hackerrank_export_json, 'r') as master_sub:
    data = json.load(master_sub)
    subs = data['submissions']
    chal_max_sub = {}
	# no need to write all submissions to a problem.. select the one with max score
    for s in subs:
        challenge = s['challenge']
        contest = s['contest']
        k = contest + ':' + challenge
        if k not in chal_max_sub:
            chal_max_sub[k] = s
        else:
            if s['score'] > chal_max_sub[k]['score']:
                chal_max_sub[k] = s
    for k in chal_max_sub:
        s = chal_max_sub[k]
        writeSubmission(s)
        #print('{} - {} {} {}'.format(s['language'], s['contest'], s['challenge'], s['score']))
