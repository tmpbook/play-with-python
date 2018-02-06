import subprocess


def run_cmd(cmd):
    return subprocess.Popen(cmd,
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).communicate()


so = run_cmd(['ls', '-a'])
print so
