#!/usr/bin/env python2

"""
Run the tests against the linux tree using pygit2 and python2.
"""

import datetime

import pygit2


def browse_history():
    repo = pygit2.Repository('linux')
    head = repo.head.target

    for commit in repo.walk(head, pygit2.GIT_SORT_TIME):
        commit.message.encode('utf-8') != ''


def get_commit(commithash):
    repo = pygit2.Repository('linux')
    commit = repo[commithash]


def get_repo_length():
    repo = pygit2.Repository('linux')
    head = repo.head.target
    cnt = 0
    for commit in repo.walk(head, pygit2.GIT_SORT_TIME):
        cnt += 1
    print(cnt)


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
