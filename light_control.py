import DmxPy
import time

class light_ctl_c(DmxPy.DmxPy):

    def send_val(self,chan,val):
        self.setChannel(chan,val)
        self.render()

    def ramp(self,chan,val,dur,res):
        """
        Ramp from previous value at chan to val in dur seconds, incrementing
        each res seconds.
        if res > dur, the light will suddenly be at the value after dur
        """
        old_val=self.dmxData[chan]
        inc=(val-old_val)/(dur/res)
        while (dur > 0):
            if res > dur:
                res = dur
                inc = val - old_val
            time.sleep(res)
            old_val+=inc
            self.send_val(chan,old_val)
            dur -= res

    def pulse(self,chan,val,dur,ramp=0.1,ramp_res=0.01):
        """
            chan: channel to send on
            val: the value at the peak of the pulse
            dur: the total duration of the pulse including the ramps
            ramp: a ramp up / down at the beginning or end of the pulse (can
            be 0) in seconds. If 2*ramp>dur, we just force ramp to dur/2 and
            have no hold in the middle
            ramp_res: duration of the increments in seconds
        """
        if (2*ramp > dur):
            ramp=dur*0.5
        dur-=2*ramp
        old_val=self.dmxData[chan]
        self.ramp(chan,val,ramp,ramp_res)
        time.sleep(dur)
        self.ramp(chan,old_val,ramp,ramp_res)

