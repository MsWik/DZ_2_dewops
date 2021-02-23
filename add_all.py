from subprocess import check_call
import shlex

git_cmd=['https://gitlab.com/MsWik/DZ_2_dewops.git','https://gitlab.com/MsWik/DZ_2_dewops.git','https://github.com/MsWik/DZ_2_dewops.git']
def add(git_cmd):
    branch_main_cmd='git branch -M main'
    check_call(shlex.split(branch_main_cmd))
    for i in git_cmd:
            add_remote_cmd='git remote add origin '+i
            check_call(shlex.split(add_remote_cmd))
            push_cmd='git push -u origin main'
            check_call(shlex.split(push_cmd))
            delete_remote_cmd='git remote rm origin'
            check_call(shlex.split(delete_remote_cmd))




