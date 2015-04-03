from os import path

from shell import shell

from cli import cli

BROC_ROOT_DIR = path.dirname(path.realpath(__file__))
BROC_HOOKS_ROOT_DIR = BROC_ROOT_DIR + '/git-hooks'

BROC_HOOKS_PATHS = {
    'post-commit': BROC_HOOKS_ROOT_DIR + '/post_commit_hook.py'
}

GIT_CONFIG = {
    'email': (lambda: shell('git config --global --get user.email').output()[0])(),
    'author': (lambda: shell('git config --global --get user.name').output()[0])()
}

get_global_git_email = lambda: shell('git config --global --get user.email').output()[0]

is_in_git_repo = lambda : len(shell('git rev-parse').errors()) == 0
get_git_root = lambda : shell('git rev-parse --show-toplevel').output()[0] if is_in_git_repo() else False
get_git_hooks_dir = lambda : get_git_root() + '/.git/hooks' if get_git_root() else False

def link_file_in_dir_as(hook_name, dir_path, link_name):
    hook_path = BROC_HOOKS_PATHS[hook_name]
    link_path = dir_path + '/' + link_name

    ln = shell('ln -s {0} {1}'.format(hook_path, link_path))
    chmod = shell('chmod +x {0}'.format(hook_path))
    return ln.code

def calculate_brownie_points(commit_msg_length, num_files_changed, additions, deletions):
    commit_score = 1 + int(commit_msg_length/20)
    additions_score = int(additions/50)
    deletions_score = int(deletions/100)

    return commit_score + additions_score + deletions_score + int(num_files_changed)
