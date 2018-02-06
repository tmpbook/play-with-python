import subprocess


def run_cmd(cmd):
    return subprocess.Popen(cmd,
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)


p = run_cmd(['ping', 'zhihu.com'])
for i in iter(p.stdout.readline, ''):
    print(i.strip())
