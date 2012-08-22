#!/usr/bin/python

"""
Example script showing how to use the fivefivefive class.  This uses the matplotlib library
to graph the output of the simulation.
"""

from fivefivefive import *
from pylab import *

r1 = 10000
r2 = 100000
c1 = 0.0000001

timer = Astable(r1,r2,c1)
print 'Astable:'
print 'Frequency: %f' %(timer.frequency())
print 'Duty cycle: %f' %(timer.duty_cycle())

print
print 'Monostable:'
one_shot = Monostable(r1,c1)
print 'Time period: %f' %(one_shot.time_period())


# render values
x = arange(0.0,0.05,1.0 / 44100)
y = []
z = []

triggered = False
trigger_after = 0.02

for t in x:
    y.append(timer.output(t))
    if t > trigger_after and not triggered:
        one_shot.set_trigger(t)
        triggered = True
    z.append(one_shot.output(t))

# plot values
plot(x,y,linewidth=1.0)
plot(x,z,linewidth=1.0)
xlabel('time (s)')
ylabel('voltage (?)')
title('555 astable+monostable output')
grid(True)
show()

    


