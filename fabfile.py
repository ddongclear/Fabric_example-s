from fabric.api import run,local,env
#env.hosts = [ '173.254.28.78', 'localhost' ]
env.hosts = ['101.200.###.']
env.user = 'root'
#env.use_ssh_config = True
#env.key_filename = "/home/myusername/.ssh/id_rsa"
env.password = "######"
#env.port = 22
def host_type():
    run('uname -s')
def uptime():
    run('uptime')
    #local('uptime')

def hello(who="world"):
    print "Hello {who}!".format(who=who)

def test():
    local('ls -al')

def commit():
    local('ls -al')


def push():
    local('ls -al')
    local('uname -s')

def test_remote():
    run('cd ..')
    run('ls -al')

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    test_remote()

