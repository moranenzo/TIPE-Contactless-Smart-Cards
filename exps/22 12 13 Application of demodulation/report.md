<h1>Experiment Report: Application of the Demodulation System to Our Setup</h1>

<h2>Objective of the Experiment</h2>
<p>
  The objective of this experiment was to apply the demodulation knowledge gained in a previous experiment. I used the demodulation device to retrieve the modulating signal embedded in the voltage across the reader’s capacitor.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the Card-Reader Model</h3>
<p>
    I assembled the card and reader circuits.
</p>
<p>
<strong>Parameters Used:</strong>
</p>
<ul>
    <li>Inductance of coils: L1 = L2 = 9 mH</li>
    <li>Capacitance of capacitors: C1 = C2 = 0.22 µF</li>
    <li>Resistance in the card: {0 Ω, 1 kΩ} (no significant effect observed with higher resistance)</li>
    <li>Follower system (OpAmp)</li>
    <li>Low-Frequency Generator: 1 V peak-to-peak amplitude, frequency not fixed</li>
    <li>Distance between coils: 0 cm (adjusted for optimal reception)</li>
</ul>

<h3>2. Building the Demodulation Device</h3>
<p>
    I chose to use an amplitude demodulation device for this experiment, as it proved effective in a previous experiment.
</p>
<p>
<strong>Devices Used:</strong>
</p>
<ul>
    <li>Multiplier</li>
    <li>Diode</li>
    <li>Capacitor: Cd = 0.22 µF</li>
    <li>Resistor: Rd = 10 kΩ</li>
</ul>

<h3>3. Observations</h3>
<p>
    I plotted the voltage recovered after the demodulator, as well as the input voltage to the demodulator, over time. It was observed that the former accurately corresponds to the demodulation of the latter, with negligible time delay.
</p>

<h2>Results</h2>
<p>
    The demodulation system successfully demodulated the voltage across the reader’s capacitor, allowing us to retrieve the modulating signal. This confirms that our card-reader and demodulator setup is suitable for future experiments.
</p>
