#!/usr/bin/env python2

"""
Run the tests against the linux tree using GitPython and python2.
"""

import datetime

import git


def browse_history():
    repo = git.Repo('./linux')

    for commit in repo.iter_commits('master'):
        commit.message != ''


def get_commit(commithash):
    repo = git.Repo('linux')
    commit = repo.commit(commithash)


def get_repo_length():
    repo = git.Repo('linux')
    master = repo.head.reference
    
    print(len(list(repo.iter_commits('master'))))


if __name__ == '__main__':
    print('Browse entire history')
    st = datetime.datetime.utcnow()
    for x in range(10):
       browse_history()
    print('    Ran for %s' % (datetime.datetime.utcnow() - st))
    print('Get commit by hash')
    st = datetime.datetime.utcnow()
    for x in range(10):
        get_commit('1da177e4c3f41524e886b7f1b8a0c1fc7321cac2')
        get_commit('e37e112de3ac64032df45c2db0dbe1e8f1af86b4')
    print('    Ran for %s' % (datetime.datetime.utcnow() - st))

    print('Number of commits:')
    st = datetime.datetime.utcnow()
    get_repo_length()
    print('    Ran for %s' % (datetime.datetime.utcnow() - st))
