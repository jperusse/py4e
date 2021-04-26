

import subprocess as sbp
import pip
pkgs = eval(str(sbp.run("pip3 list -o --format=json", shell=True,
                        stdout=sbp.PIPE).stdout, encoding='utf-8'))
if len(pkgs) == 0:
    print('Nothing to update')
    quit()

print(str(len(pkgs)) + ' modules to update found. Beginning update proess...')
for pkg in pkgs:
    print(pkg)
    sbp.run("pip3 install --upgrade " + pkg['name'], shell=True)
