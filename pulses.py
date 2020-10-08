import numpy as np

from waveforms import Waveform, ConstantWaveform
from utils import validate_duration


class Pulse:
    """A generic pulse.

    Args:
        duration (int): The pulse duration (in ns).
        amplitude (float, Waveform): The pulse amplitude. Can be a float (MHz),
            in which case it's kept constant throught the entire pulse, or a
            waveform.
        detuning (float, Waveform): The pulse detuning. Can be a float (MHz),
            in which case it's kept constant throught the entire pulse, or a
            waveform.
        phase (float): The pulse phase (in radians).
    """

    def __init__(self, duration, amplitude, detuning, phase):

        self.duration = validate_duration(duration)

        if isinstance(amplitude, Waveform):
            if amplitude.duration != self.duration:
                raise ValueError("The amplitude waveform's duration doesn't"
                                 " match the pulses' duration.")
            if np.any(self.samples < 0):
                raise ValueError("An amplitude waveform has always to be "
                                 "non-negative.")
            self.amplitude = amplitude
        elif amplitude > 0:
            self.amplitude = ConstantWaveform(self.duration, amplitude)

        else:
            raise ValueError("Negative amplitudes are invalid.")

        if isinstance(detuning, Waveform):
            if detuning.duration != self.duration:
                raise ValueError("The detuning waveform's duration doesn't"
                                 " match the pulses' duration.")
            self.detuning = detuning
        else:
            self.detuning = ConstantWaveform(self.duration, detuning)

        self.phase = float(phase) % (2 * np.pi)
