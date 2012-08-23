#!/usr/bin/python

"""
Simulation of an Atari Punk Console using the fivefivefive class.
"""
from fivefivefive import *
from pylab import *
import sys

if len(sys.argv) < 2:
    print "Usage: ./atari_punk_console.py [R1 value]"
    sys.exit(1)

r1 = float(sys.argv[1])
r2 = 1000.0
c1 = 0.0000001

timer = Astable(r1,r2,c1)
print 'Astable:'
print 'Frequency: %f' %(timer.frequency())
print 'Duty cycle: %f' %(timer.duty_cycle())

r3 = 100000.0
c2 = 0.0000001

print
print 'Monostable:'
one_shot = Monostable(r3,c2)
print 'Time period: %f' %(one_shot.time_period())


# render values
x = arange(0.0,0.05,1.0 / 44100)
y = []
z = []


for t in x:
    y.append(timer.output(t))
    if timer.output(t) <= 0.0:
        one_shot.set_trigger(t)
    z.append(one_shot.output(t))

# plot values
plot(x,z,linewidth=1.0)
xlabel('time (s)')
ylabel('voltage (?)')
title('atari punk console output')
grid(True)
show()

    


