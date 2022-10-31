import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))
# print(BASEDIR)
TOOLSDIR = os.path.join(BASEDIR, "tools")
# print(TOOLSDIR)
LOGDIR = os.path.join(BASEDIR, "log")
# print(LOGDIR)
TESTLOGDIR = os.path.join(LOGDIR, "test.log")
# print(TESTLOGDIR)
CONFIGYAMLDIR = os.path.join(BASEDIR, "config.yml")
# print(CONFIGYAMLDIR)
CASEYAML = os.path.join(BASEDIR, "testcase_api_yaml")