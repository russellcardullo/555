# 555

## About
555 is a simulation of the 555 timer in python.  As of now this can simulate astable and monostable modes.

The simulation is configured with values for resistance and capacitance.  Output of the timer is given just in values of 0 or 1.

The simulation represents a 555 under ideal conditions.  In the real world operation can be much different depending on component tolerances, input voltage and environmental factors.  Output is also seldom exactly 0 or 1.


## Usage 

The module fivefivefive contains two classes:

* Astable - continuously produces a pulse wave
* Monostable - produces a single pulse for a finite duration

Both classes are initialized with values for resistance and capacitance.  Check [here](http://www.kpsec.freeuk.com/555timer.htm) for a good overview of how the different types of circuits work.

You can get output of a circuit for a given time T in seconds.  For example, to continuously output values over time for a 555 running in astable mode:

    timer = Astable(1000,1000,0.0001)   # initialize a timer with given resistance/capacitance values
    for t in arange(0.0,2.0,0.01):      # run the simulation for 2 seconds using 0.01 second steps
        print t,timer.output(t)         # print value of output for time t

Note that when simulating output over time for higher frequencies accuracy will be low if the step size is too large.  To accurately plot output use a sampling rate at least [twice the frequency](http://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem).

For more examples see example.py.


