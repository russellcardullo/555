#!/usr/bin/python
"""
This module contains classes that can simulate a 555 in various modes.  Currently this
supports the following modes:

    * Monostable (one-shot): Triggers a single pulse
    * Astable (oscillator): Produces a pulse wave

Units of measurement in this module are specified in:

    Resistance: Ohms
    Capacitance: Farads
    Voltage: Volts
    Time: Seconds
    Frequency: Hertz

"""

class Monostable:
    """Simulates a monostable circuit (one shot).  Initialize the class with values for R1 and C1.
       Get the time period of the pulse for particular resistor/capacitor values.
       You can also simulate the output for given time T (seconds) which returns the state
       as 0 or 1.  This requires you to trigger the timer at a start time T0.  The output will
       be high for the time period with respect to the resistor/capacitor values."""

    def __init__(self,r1,c1):
        self.trigger = False
        self.r1 = float(r1)
        self.c1 = float(c1)
        self.last_trigger = 0.0

    def time_period(self):
        """Return the time period of the pulse for the configured resistor/capacitor values."""
        return 1.1 * self.r1 * self.c1

    def set_trigger(self,t):
        """Set the trigger if not already set and sets last trigger time.
           Ignore if the trigger is already set"""
        if not self.trigger:
            #print 'trigger %f' %(t)
            self.trigger = True
            self.last_trigger = t

    def reset_trigger(self):
        """Resets the trigger to False"""
        self.trigger = False

    def output(self,t):
        """Returns the output of the timer with respect to time t.
           If triggered and (t - last_trigger) < time_period return 1.0, else 0.0.
           Also if triggered by time has been exceeded reset the trigger to False."""
        if self.trigger:
            if (t - self.last_trigger) < self.time_period():
                return 1.0
            else:
                self.trigger = False
                return 0.0
        else:
            return 0.0

class Astable:
    """Simulates an astable circuit (oscillator).  Initialize the class with values for R1, R2 and C1.
       Get the frequency and duty cycle for particular resistor/capacitor values.
       You can also simulate the output for given time T (seconds) which returns the state
       as 0 or 1."""

    def __init__(self,r1,r2,c1):
        self.r1 = float(r1)
        self.r2 = float(r2)
        self.c1 = float(c1)

    def frequency(self):
        """Returns the frequency of the signal output given the configured resistors and capacitors."""
        return 1.4 / ((self.r1 + (2 * self.r2)) * self.c1)

    def mark_time(self):
        """Returns the duration in seconds that the output will be high."""
        return 0.7 * (self.r1 + self.r2) * self.c1

    def space_time(self):
        """Returns the duration in seconds that the output will be low."""
        return 0.7 * self.r2 * self.c1

    def duty_cycle(self):
        """Returns the duty cycle as a value between 0 and 1."""
        return (self.r1 + self.r2) / (self.r1 + (2.0 * self.r2))

    def output(self,t):
        """Returns the output of the timer given the time t in seconds.
           Currently phase=0.0 but for other phases calculate using (t - phase)"""
        period = 1.0 / self.frequency()
        value = (t % period) / period
        if value < self.duty_cycle():
            return 1.0
        else:
            return 0.0

