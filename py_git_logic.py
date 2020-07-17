#!/usr/bin/env python3
import os, sys, socket, traceback, json, yaml, getpass
from dulwich.repo import Repo

repo_path = os.path.realpath(os.path.expanduser('~/.myrepo'))
if not os.path.exists(repo_path):
    os.mkdir(repo_path)
if not os.path.exists('{}/.git'.format(repo_path)):
    repo = Repo.init(repo_path)
else:
    repo = Repo(repo_path)

yaml.dump(repo, sys.stdout)
index = repo.open_index()
MSG = f'  repo index path={index.path}, index list={list(index)}, '
yaml.dump(MSG, sys.stdout)

f = open(f'{repo_path}/foo', 'wb')
_ = f.write(b"monty1")
f.close()
repo.stage([b"foo"])

print(",".join([f.decode(sys.getfilesystemencoding()) for f in repo.open_index()]))

commit_id = repo.do_commit(b"The first commit") #, committer=getpass.getuser().encode())
print(f'    commit_id={commit_id},     repo_head = {repo.head()}   ')

#repo = Repo("myrepo")
