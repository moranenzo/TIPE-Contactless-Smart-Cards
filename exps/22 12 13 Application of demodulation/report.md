<h1>Experiment Report: Application of the Demodulation System to Our Setup</h1>

<h2>Objective of the Experiment</h2>
<p>
  The objective of this experiment was to apply the knowledge about demodulation I gained in a previous experiment. I used the demodulation device to recover the modulating signal hidden in the voltage across the capacitor of the reader.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the Card-Reader Model</h3>
<p>
    I assembled the card and reader circuits.
</p>
<p>
<strong>Parameters used:</strong>
</p>
<ul>
    <li>Inductance of coils: L1 = L2 = 9 mH</li>
    <li>Capacity of capacitors: C1 = C2 = 0.22 µF</li>
    <li>Resistance in the card: {0Ω, 1kΩ} (no significant effect when increasing resistance)</li>
    <li>Follower system (OpAmp)</li>
    <li>Low-Frequency Generator: 1 V peak-to-peak amplitude, frequency not fixed</li>
    <li>Distance between coils: 0 cm (adjusted for optimal reception)</li>
</ul>

<h3>2. Building the Demodulation Device</h3>
<p>
    I chose to use an amplitude demodulation device for this experiment since I had already used one in a previous experiment, and it was perfectly suited to my needs.
</p>
<p>
<strong>Devices used:</strong>
</p>
<ul>
    <li>Multiplier</li>
    <li>Diode</li>
    <li>Capacitor: Cd = 0.22 µF</li>
    <li>Resistance: Rd = 10kΩ</li>
</ul>

<h3>3. Observations</h3>
<p>
    I plotted the voltage recovered after the demodulator as well as the input voltage to the demodulator as a function of time. It can be observed that the former accurately corresponds to the demodulation of the latter, with negligible time delay.
</p>

<h2>Results</h2>
<p>
    The demodulation system perfectly demodulated the voltage across the reader’s capacitor. We successfully retrieved the modulating signal, which indicates that this card-reader + demodulator system can be used for our future experiments.
</p>
