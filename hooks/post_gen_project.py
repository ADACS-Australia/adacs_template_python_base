import subprocess

def git():
    pass
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit of template code'])

if __name__ == '__main__':
    git()
