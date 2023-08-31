import subprocess


def git():
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", "Initial commit of template code"])


def print_instructions():
    with open("README.1st.config_services", "r") as file:
        lines = []
        line_in = file.readline()
        while line_in:
            if line_in[0:3] != "***":
                lines.append(line_in.rstrip())
            line_in = file.readline()


if __name__ == "__main__":
    git()
    print_instructions()
