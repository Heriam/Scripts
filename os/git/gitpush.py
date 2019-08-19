import subprocess, os, sys
ROOT_DIR = 'C:\\Users\\j16492\\PycharmProjects\\Scripts'
sys.path.append(ROOT_DIR)
from doc.ics.InterviewICSGenerator import InterviewICSGenerator

os.chdir(ROOT_DIR)
subprocess.call("git pull", shell=True)
InterviewICSGenerator().run()
subprocess.call("git add .", shell=True)
subprocess.call('git commit -m "auto-updated by Outlook mail"')
subprocess.call("git push", shell=True)


