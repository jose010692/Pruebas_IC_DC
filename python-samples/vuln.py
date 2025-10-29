import os
def run_cmd(cmd):
    os.system(cmd)  # inseguro
if __name__ == "__main__":
    run_cmd("ls -la " + input("dir: "))
