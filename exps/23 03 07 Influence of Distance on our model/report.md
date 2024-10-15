<h1>Experiment Report: Influence of Distance on our model</h1>

<h2>Objective of the Experiment</h2>
<p>
  In a previous experiment, I highlighted the significant effect of distance between the two coils on the induction effect. The objective of this experiment is closely related to the one of the previous experiment; I aim to investigate the influence of distance on our model and determine its limit distance for effective use. Since no message is conveyed when the card is not in front of the reader, the distance between the two coils must greatly influence the quality of message transmission. Therefore, defining a limit distance for effective operation is important.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the card-reader model</h3>
<p>
    I assembled the card and reader circuits. 
</p>
<p>
<strong>Parameters used:</strong>
</p>
<ul>
    <li>Inductance of coils: L1 = L2 = 9 mH</li>
    <li>Capacity of capacitors: C1 = C2 = 0.22 µF</li>
    <li>Resistance in the card: {0Ω, 1kΩ} (no significant influence when increasing resistance)</li>
    <li>Follower system (OpAmp)</li>
    <li>Low-Frequency Generator: amplitude of 5 V peak-to-peak, frequency not fixed</li>
    <li>Distance between coils: 0 cm (adjusted for optimal reception)</li>
</ul>

<h3>2. Data Collecting</h3>
<p>
    To investigate the extent of the impact of distance between the coils, I decided to plot the amplitude of the voltage measured in the capacitor (inside the reader) as a function of distance. I measured the amplitude of the voltage for each distance value between the two coils.
</p>

<h3>3. Observations</h3>
<p>
    By plotting all the values I gathered and analyzing the curves, I deduced the following information:
</p>
<ul>
  <li>The distance significantly influences the amplitude of the voltage, as expected.</li>
  <li>At distances of 2 to 3 cm, the amplitude is insufficient to transmit complex signals. This is our distance limit.</li>
</ul>

<h2>Results</h2>
<p>
  The experiment demonstrated a clear relationship between distance and voltage amplitude. As expected, increasing the distance between the coils led to a decrease in the amplitude of the voltage measured in the capacitor. The results confirmed that at distances of 2 to 3 cm, the voltage amplitude became inadequate for transmitting complex signals, establishing this range as the effective distance limit for our model. This information is crucial for future experiments, as it provides a guideline for optimizing the design and functionality of the card-reader system.
</p>
