<h1>Experiment Report: Basic Code and Arduino Binary-to-Voltage Conversion</h1>

<h2>Objective of the Experiment</h2>
<p>
  The objective of this experiment was to write a script to send a message, i.e., translate a binary message into voltage variations. This experiment will specifically focus on the issues I encountered with the C++ code and the Arduino hardware.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Basic code issues</h3>
<p>
    I initially struggled with my code. Since I was working away from an Arduino, I couldn't test it until now. Naturally, I encountered many bugs, but, after many tries, I managed to get my code working. After successful tests, the LED was turning on and off as expected.
</p>
<p>
  Note: The LED briefly lights up when the code is uploaded to the board.
</p>

<h3>2.1 Arduino Code to Convert Binary to Voltage</h3>
<ul>
  <li>Sending the message from the Arduino Serial Monitor</li>
  <li>We connected an oscilloscope to the Arduino to check if the voltage is present.</li>
  <li>Successful test: example (1)</li>
</ul>
<p>
  Note: Voltage spikes were observed when the code was uploaded.
</p>

<h3>2.2 Problem Identified</h3>
<p>
  We observed two sets of spikes: one when the board receives the uploaded code and another when the upload is completed.
</p>
<p>
  This phenomenon can be seen in result (2) and result (3).
</p>

<h3>3. Test of Sending a Message from Python</h3>
<p>
    It failed... Since I did not have enough time to retry, I decided to leave it as is. Sending the message from the Arduino Console instead of from Python doesn't make a significant difference for my experiment.
</p>

<h3>Details</h3>
<p>
  Here are some clues to understand what you can see on the files result (1), result (2) and result (3).
</p>
<ul>
  <li>(1) Result of the command 11001100001111</li>
  <li>(2) Observation of spike packets before our signal</li>
  <li>(3) Zoom in on the spike packets</li>
</ul>

<h2>Results</h2>
<p>
  The experiment successfully demonstrated that a binary message can be converted into voltage variations using Arduino. The tests with the oscilloscope confirmed the presence of voltage spikes during message transmission, as expected. While the attempt to send a message from Python was unsuccessful, sending it via the Arduino Serial Monitor produced the desired results. The LED blinking confirmed the accuracy of the binary-to-voltage conversion. Despite the initial challenges with coding and hardware synchronization, the overall goal was achieved.
</p>
