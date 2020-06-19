import platform
import shutil
import os, sys
import subprocess

version = int(sys.version_info[0])
system = platform.system()
path = os.path.abspath(__file__).replace(os.path.basename(__file__),"")
args = sys.argv


# pre-installation
def console_info(info):
    print("[INFO]%s" % info)


console_info("testing nexus server connectivity")
if 0 != subprocess.call("ping -c 1 10.153.3.130", shell=True):
    console_info("yum repo server(10.153.3.130) is unreachable")
    sys.exit(0)

if "--install-python3" in args:
    console_info("updating yum packages")
    subprocess.call("sudo yum -y update", shell=True)
    if 0 == subprocess.call("pip3 -V", shell=True):
        console_info("python3 already installed")
        sys.exit(0)
    if os.path.exists("/etc/yum.repos.d.backup"):
        console_info("removing old backup repo files")
        shutil.rmtree("/etc/yum.repos.d.backup")
    console_info("setting yum repos")
    subprocess.call("mkdir /etc/yum.repos.d.backup", shell=True)
    subprocess.call("mv /etc/yum.repos.d/* /etc/yum.repos.d.backup", shell=True)
    shutil.copy2(os.path.join(path, "lib", "h3c_mirror.repo"), "/etc/yum.repos.d")
    console_info("cleaning yum caches")
    subprocess.call("yum clean all && rm -rf /var/cache/yum", shell=True)
    console_info("installing development tools")
    if 0 != subprocess.call("sudo yum -y groupinstall 'Development Tools'", shell=True):
        sys.exit(-1)
    if 0 != subprocess.call("sudo yum -y install zlib zlib-devel libffi-devel maven openssl-devel", shell=True):
        sys.exit(-1)
    console_info("installing Python 3.7.0")
    if 0 != subprocess.call("tar -xf %s" % os.path.join(path, "lib", "Python-3.7.0.tar.xz"), shell=True):
        sys.exit(-1)
    if 0 != subprocess.call("cd Python-3.7.0 && ./configure && make && make install", shell=True):
        sys.exit(-1)
    if not os.path.exists("/root/.pip"):
        os.mkdir("/root/.pip")
    with open("/root/.pip/pip.conf", "w+") as f:
        f.write('''
        [global]
        trusted-host = 10.153.3.130
        index = http://10.153.3.130:8080/repository/pypi-central/pypi
        index-url = http://10.153.3.130:8080/repository/pypi-central/simple
        ''')

# python version check
if version == 2:
    console_info("you need to run 'python3 setup.py' to further install app generator")
    sys.exit(0)


# installation
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

INSTALL_PATH = "/opt/seerengine/app/generator"
BASH_FILE = "/usr/bin/seerengine"
if os.path.exists(INSTALL_PATH):
    console_info("updating generator ...")
    shutil.rmtree(INSTALL_PATH)
os.makedirs(INSTALL_PATH)
copytree(os.path.join(path, "api"), INSTALL_PATH)
with open(BASH_FILE, "w+") as f:
    f.write('''
    #!/bin/bash
    python3 /opt/seerengine/app/generator/AppGenerator.py
    ''')
subprocess.call("sudo chmod 777 %s" % BASH_FILE, shell=True)

if 0 != subprocess.call("pip3 install jinja2", shell=True):
    sys.exit(-1)

# finished
console_info("installed successfully")
console_info("run 'seerengine' to start app generator")