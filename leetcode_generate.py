import configparser
import datetime
import html
import json
import os
import re
import sys
import time
from collections import OrderedDict, namedtuple

import requests

BASE_URL = 'https://leetcode-cn.com'
HEADERS = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)", 'Connection': 'keep-alive',
           'Referer': BASE_URL + '/accounts/login/', "origin": BASE_URL}
HOME = os.getcwd()
SOLUTION_DIR = os.path.join(HOME, 'solutions')
ProgLang = namedtuple('ProgLang', ['language', 'ext', 'annotation'])
ProgLangList = [
    ProgLang('cpp', 'cpp', '//'),
    ProgLang('java', 'java', '//'),
    ProgLang('python', 'py', '#'),
    ProgLang('python3', 'py', '#'),
    ProgLang('c', 'c', '//'),
    ProgLang('csharp', 'cs', '//'),
    ProgLang('javascript', 'js', '//'),
    ProgLang('ruby', 'rb', '#'),
    ProgLang('kotlin', 'kt', '//'),
    ProgLang('swift', 'swift', '//'),
    ProgLang('golang', 'go', '//'),
    ProgLang('scala', 'scala', '//'),
    ProgLang('rust', 'rs', '//'),
]
ProgLangDict = dict((item.language, item) for item in ProgLangList)


def get_config_from_file():
    config = configparser.ConfigParser()
    config.read(os.path.join(HOME, 'config.cfg'))
    if 'leetcode' not in config.sections():
        raise Exception('Please create config.cfg first.')

    username = config.get('leetcode', 'username')
    password = config.get('leetcode', 'password')
    if not username or not password:  # username and password not none
        raise Exception(
            'Please input your username and password in config.cfg.'
        )

    language = config.get('leetcode', 'language')
    if not language:
        language = 'python'  # language default python

    repo = config.get('leetcode', 'repo')
    if not repo:
        raise Exception('Please input your Github repo address')

    return dict(
        username=username,
        password=password,
        language=language,
        repo=repo)


def rep_unicode_in_code(code):
    """
    Replace unicode to str in the code
    like '\u003D' to '='
    :param code: type str
    :return: type str
    """
    pattern = re.compile('(\\\\u[0-9a-zA-Z]{4})')
    m = pattern.findall(code)
    for item in set(m):
        code = code.replace(item, chr(int(item[2:], 16)))  # item[2:]去掉\u
    return code


class QuizItem:
    """ QuizItem """
    base_url = BASE_URL

    def __init__(self, **data):
        self.__dict__.update(data)
        self.solutions = []

    def __str__(self):
        return '<Quiz: {question_id}-{question__title_slug}({difficulty})-{is_pass}>'.format(
            question_id=self.question_id,
            question__title_slug=self.question__title_slug,
            difficulty=self.difficulty,
            is_pass=self.is_pass,
        )

    def __repr__(self):
        return self.__str__()

    @property
    def json_object(self):
        addition_properties = [
            'is_pass', 'difficulty', 'is_lock', 'url', 'acceptance'
        ]
        dct = self.__dict__
        for prop in addition_properties:
            dct[prop] = getattr(self, prop)
        return dct

    @property
    def is_pass(self):
        return True if self.status == 'ac' else False

    @property
    def difficulty(self):
        difficulty = {1: "Easy", 2: "Medium", 3: "Hard"}
        return difficulty[self.level]

    @property
    def is_lock(self):
        return not self.is_favor and self.paid_only

    @property
    def url(self):
        return '{base_url}/problems/{question__title_slug}'.format(
            base_url=BASE_URL,
            question__title_slug=self.question__title_slug,
        )

    @property
    def acceptance(self):
        return '%.1f%%' % (
                float(self.total_acs) * 100 / float(self.total_submitted)
        )


class LeetCode:
    def __init__(self):
        self.session = requests.Session()
        self.config = get_config_from_file()
        self.cookies = None
        self.items = []
        self.id_map = {}
        self.submissions = []
        self.languages = [x.strip() for x in self.config['language'].split(',')]
        proglangs = [
            ProgLangDict[x.strip()] for x in self.config['language'].split(',')
        ]
        self.proglangdict = dict(zip(self.languages, proglangs))
        self.repo = self.config['repo']
        self.num_solved = 0
        self.num_total = 0
        self.num_lock = 0
        self.ac_easy = 0
        self.ac_medium = 0
        self.ac_hard = 0

    def _generate_items_from_api(self, json_data):
        stat_status_pairs = json_data['stat_status_pairs']
        for quiz in stat_status_pairs:
            if quiz['stat']['question__hide']:
                continue

            data = {}
            data['question__title'] = quiz['stat']['question__title']
            data['question__title_slug'] = quiz['stat']['question__title_slug']
            data['paid_only'] = quiz['paid_only']
            data['level'] = quiz['difficulty']['level']
            data['is_favor'] = quiz['is_favor']
            data['total_acs'] = quiz['stat']['total_acs']
            data['total_submitted'] = quiz['stat']['total_submitted']
            data['question_id'] = quiz['stat']['question_id']
            data['status'] = quiz['status']
            item = QuizItem(**data)
            yield item

    def login(self):
        self.session.post('{}/accounts/login'.format(BASE_URL), headers=HEADERS,
                          data={'login': self.config['username'], 'password': self.config['password']}, timeout=10,
                          allow_redirects=False)
        self.cookies = self.session.cookies.get_dict()
        if self.cookies.get('LEETCODE_SESSION') is None:
            raise Exception('Login failed, please check your config or your network.')
        print('Login successfully')

    @property
    def is_login(self):
        test_url = BASE_URL + '/api/submissions/?format=json&limit=20&offset=0'

        resp = self.session.get(test_url, timeout=10)
        if resp.status_code != 200:
            return False
        return True

    def load_question_id_map(self):
        payload = {"operationName": "getQuestionTranslation", "variables": {},
                   "query": "query getQuestionTranslation($lang: String) {\n  translations: allAppliedQuestionTranslations(lang: $lang) {\n    title\n    questionId\n    __typename\n  }\n}\n"}

        resp = self.session.post(BASE_URL + '/graphql', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        assert resp.status_code == 200
        data = resp.json()
        for d in data['data']['translations']:
            self.id_map[d['title']] = int(d['questionId'])

        print('Load question id map successfully')
        print(self.id_map)

    def load_items_from_api(self):
        """ load items from api"""
        resp = self.session.get('{}/api/problems/all'.format(BASE_URL))
        assert resp.status_code == 200
        data = resp.json()
        if not data['user_name']:
            raise Exception("Something wrong with your personal info.")

        self.num_solved = data['num_solved']
        self.num_total = data['num_total']
        self.ac_easy = data['ac_easy']
        self.ac_medium = data['ac_medium']
        self.ac_hard = data['ac_hard']
        self.items = list(self._generate_items_from_api(data))
        self.num_lock = len([i for i in self.items if i.is_lock])
        self.items.reverse()

    def load_submissions(self):
        """ load all submissions from leetcode """
        print('API load submissions request 3 seconds per request')
        print('Please wait ...')
        limit = 20
        offset = 0
        last_key = ''
        while True:
            print('try to load submissions from ', offset, ' to ', offset + limit)
            submissions_url = '{}/api/submissions/?format=json&limit={}&offset={}&last_key={}'.format(
                BASE_URL, limit, offset, last_key
            )

            resp = self.session.get(submissions_url)
            assert resp.status_code == 200
            data = resp.json()
            if 'has_next' not in data.keys():
                raise Exception('Get submissions wrong, Check network\n')

            self.submissions += data['submissions_dump']
            if data['has_next']:
                offset += limit
                last_key = data['last_key']
                time.sleep(3)
            else:
                break

    def load_solutions_to_items(self):
        """
        load all solutions to items
        combine submission's `runtime` `title` `lang` `submission_url` to items
        """
        ids = [i.question_id for i in self.items]
        item_dict = OrderedDict(zip(ids, self.items))

        def make_sub(sub):
            return dict(
                runtime=int(sub['runtime'][:-3]),
                title=sub['title'],
                lang=sub['lang'].lower(),
                timestamp=sub['timestamp'],
                submission_url=BASE_URL + sub['url'],
            )

        ac_subs = [make_sub(sub) for sub in self.submissions if sub['status_display'] == 'Accepted']

        def remain_shortesttime_submissions(submissions):
            submissions_dict = {}
            for item in submissions:
                k = '{}-{}'.format(item['lang'], item['title'])
                if k not in submissions_dict.keys():
                    submissions_dict[k] = item
                else:
                    old = submissions_dict[k]
                    if item['timestamp'] > old['timestamp']:  # 保留最后一次提交的
                        submissions_dict[k] = item
            return list(submissions_dict.values())

        shortest_subs = remain_shortesttime_submissions(ac_subs)
        for solution in shortest_subs:
            title_id = self.id_map[solution['title']]
            if title_id in item_dict.keys():
                item_dict[title_id].solutions.append(solution)

    def download_by_id(self, qid):
        quiz = self._find_item_by_quiz_id(qid)
        if quiz:
            self._download_code_by_quiz(quiz)

    def download(self):
        """ download all solutions with single thread """
        ac_items = [i for i in self.items if i.is_pass]
        for quiz in ac_items:
            time.sleep(1)
            self._download_code_by_quiz(quiz)

    def _download_code_by_quiz(self, quiz):
        """
        Download code by quiz
        quiz: type QuizItem
        """
        qid = quiz.question_id
        qtitle = quiz.question__title_slug
        print(self.languages, quiz.solutions)
        slts = list(
            filter(lambda i: i['lang'] in self.languages, quiz.solutions)
        )
        if not slts:
            print(
                'No solution with the set languages in question:{}-{}'.format(
                    qid, qtitle
                )
            )
            return

        qname = '{id}-{title}'.format(id=str(qid), title=qtitle)
        print('begin download ' + qname)
        path = os.path.join(SOLUTION_DIR, qname)
        os.makedirs(path, exist_ok=True)
        for slt in slts:
            fname = '{title}.{ext}'.format(
                title=qtitle, ext=self.proglangdict[slt['lang']].ext
            )
            filename = os.path.join(path, fname)
            content = self._get_code_with_anno(slt)

            with open(filename, 'w', encoding='utf-8') as f:
                print('write to file ->', fname)
                f.write(content)

    def _get_code_with_anno(self, solution):
        question, code = self._get_code_by_solution(solution)
        language = solution['lang']
        # generate question with anno
        lines = []
        for line in question.split('\n'):
            if line.strip() == '':
                lines.append(self.proglangdict[language].annotation)
            else:
                lines.append(
                    '{anno} {line}'.format(
                        anno=self.proglangdict[language].annotation,
                        line=html.unescape(line),
                    )
                )
        quote_question = '\n'.join(lines)
        # generate content
        content = '# -*- coding:utf-8 -*-' + '\n' * 3 if language == 'python' else ''
        content += quote_question
        content += '\n' * 3
        content += code
        content += '\n'
        return content

    def _get_code_by_solution(self, solution):
        """
        get code by solution
        solution: type dict
        """
        solution_url = solution['submission_url']
        print(solution_url)
        r = self.session.get(solution_url)
        assert r.status_code == 200
        # pattern = re.compile(
        #     r'<meta name=\"description\" content=\"(?P<question>.*)\" />\n    \n    <meta property=\"og:image\"',
        #     re.S,
        # )
        pattern = re.compile(
            r'<meta name=\"description\" content=\"(?P<question>.*)\" />\n    \n    <meta name=\"keywords\"',
            re.S,
        )
        m1 = pattern.search(r.text)
        question = m1.groupdict()['question'] if m1 else None
        if not question:
            raise Exception(
                'Can not find question descript in question:{title}'.format(
                    title=solution['title']
                )
            )

        # html.unescape to remove &quot; &#39;
        question = html.unescape(question)
        pattern = re.compile(
            r'submissionCode: \'(?P<code>.*)\',\n  editCodeUrl', re.S
        )
        m1 = pattern.search(r.text)
        code = m1.groupdict()['code'] if m1 else None
        if not code:
            raise Exception(
                'Can not find solution code in question:{title}'.format(
                    title=solution['title']
                )
            )

        code = rep_unicode_in_code(code)
        return question, code

    def write_readme(self):
        """Write Readme to current folder"""
        languages_readme = ', '.join([x.capitalize() for x in self.languages])
        md = '''# :pencil2: Leetcode Solutions with {language}

<p>
<img src="https://img.shields.io/badge/User-raojingpeng-purple.svg?" alt="">
<img src="https://img.shields.io/badge/Solved-{num_solved}/{num_total}-blue.svg?" alt="">
<img src="https://img.shields.io/badge/Easy-{ac_easy}-yellow.svg?" alt="">
<img src="https://img.shields.io/badge/Medium-{ac_medium}-green.svg?" alt="">
<img src="https://img.shields.io/badge/Hard-{ac_hard}-red.svg?" alt="">
</p>

:heart: Update time:  {tm}

:heart: Auto created by [leetcode_generate](https://github.com/raojingpeng/LeetCode/blob/master/leetcode_generate.py)

:heart: If you have any question, please give me an [issue]({repo}/issues)

| # | Title | Source Code | Article | Difficulty |
|:---:|:---:|:---:|:---:|:---:|'''.format(
            language=languages_readme,
            tm=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            num_solved=self.num_solved,
            num_total=self.num_total,
            ac_easy=self.ac_easy,
            ac_medium=self.ac_medium,
            ac_hard=self.ac_hard,
            repo=self.repo
        )
        md += '\n'
        for item in self.items:
            # article = '[:memo:](%s/)' % os.path.join(self.base_url, 'problems', item.question__title_slug)
            # if item.question__article__slug:
            #     article = '[:memo:](https://leetcode.com/articles/{article}/)'.format(
            #         article=item.question__article__slug
            #     )
            if item.question__title_slug:
                article = '[:memo:](https://leetcode-cn.com/articles/{article}/)'.format(
                    article=item.question__title_slug
                )
            if item.is_lock:
                language = ':lock:'
            else:
                if item.solutions:
                    dirname = '{folder}/{id}-{title}'.format(
                        folder='solutions',
                        id=str(item.question_id),
                        title=item.question__title_slug,
                    )
                    language = ''
                    language_lst = [
                        i['lang']
                        for i in item.solutions
                        if i['lang'] in self.languages
                    ]
                    while language_lst:
                        lan = language_lst.pop()
                        language += '[{language}]({repo}/blob/master/{dirname}/{title}.{ext})'.format(
                            language=lan.capitalize(),
                            repo=self.repo,
                            dirname=dirname,
                            title=item.question__title_slug,
                            ext=ProgLangDict[lan].ext,
                        )
                        language += ' '
                else:
                    language = ''
            language = language.strip()
            md += '|{id}|[{title}]({url})|{language}|{article}|{difficulty}|\n'.format(
                id=item.question_id,
                title=item.question__title_slug,
                url=item.url,
                language=language,
                article=article,
                difficulty=item.difficulty,
            )
        with open('README.md', 'w') as f:
            f.write(md)

    def _find_item_by_quiz_id(self, qid):
        """
        find the item by quiz id
        """
        lst = list(filter(lambda x: x.question_id == qid, self.items))
        if len(lst) == 1:
            return lst[0]

        print('No exits quiz id:', qid)

    def push_to_github(self):
        strdate = datetime.datetime.now().strftime('%Y-%m-%d')
        cmd_git_add = 'git add .'
        cmd_git_commit = 'git commit -m "update at {date}"'.format(
            date=strdate
        )
        cmd_git_push = 'git push -u origin master'
        os.system(cmd_git_add)
        os.system(cmd_git_commit)
        os.system(cmd_git_push)

    def start(self):
        if not self.is_login:
            self.login()
        self.load_question_id_map()
        self.load_items_from_api()
        self.load_submissions()
        self.load_solutions_to_items()


def do_job(leetcode):
    leetcode.start()
    print('Leetcode load self info')
    if len(sys.argv) == 1:
        # simple download
        # leetcode.dowload()
        # we use multi thread
        print('download all leetcode solutions')
        # leetcode.download_with_thread_pool()
        leetcode.download()
    else:
        for qid in sys.argv[1:]:
            print('begin leetcode by id: {id}'.format(id=qid))
            leetcode.download_by_id(int(qid))
    print('Leetcode finish dowload')
    leetcode.write_readme()
    print('Leetcode finish write readme')
    leetcode.push_to_github()
    print('push to github')


if __name__ == '__main__':
    leetcode = LeetCode()
    while True:
        do_job(leetcode)
        time.sleep(24*60*60)
