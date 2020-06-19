# coding=UTF-8
import os
import sys
import platform
import logging
import json
import subprocess

# 常量定义 ====
PROJECT_NAME = 'CMDExecutor'

# 工具对象 ====
# Python版本
python_version = sys.version_info[:3]
python_version_str = '.'.join(str(i) for i in sys.version_info[:3])

# 系统信息
system_info = platform.uname()

# 绝对路径
env_absolute_path = os.path.abspath(__file__).replace(os.path.basename(__file__),'')

# 初始化日志工具
logger = logging.getLogger(PROJECT_NAME)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh = logging.FileHandler(filename=env_absolute_path + '%s.log' % PROJECT_NAME, encoding='utf-8', mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)


# 工具方法 ====
def info(info):
    print('\n[INFO] %s' % info)
    logger.info(info)


def error(error):
    print('\n[ERROR] %s' % error)
    logger.error(error)


def shell(cmd, exit4fail=True):
    info(cmd)
    succeeded = True
    # 父进程等待子进程完成。返回退出信息(return code，相当于Linux exit code)
    p = subprocess.Popen(cmd, shell=True)
    p.communicate()
    if p.returncode != 0:
        error('failed to execute command "%s"' % cmd)
        succeeded = False
        if exit4fail:
            sys.exit(0)
    return succeeded