<h2>Experiment Report: Basic Code and Arduino Binary-to-Voltage Conversion</h2>

<h3>Basic Code:</h3>
<p>
  We spent some time fixing the code. After successful tests:
</p>
<ul>
  <li>The LED turns on and off as expected.</li>
</ul>
<p>
  Note: The LED briefly lights up when the code is uploaded to the board.
</p>

<h3>Arduino Code to Convert Binary to Voltage:</h3>
<ul>
  <li>Sending the message from the Arduino Serial Monitor</li>
  <li>We connected an oscilloscope to the Arduino to check if the voltage is present.</li>
  <li>Successful test: example (1)</li>
</ul>
<p>
  Note: Voltage spikes were observed when the code was uploaded.
</p>

<h3>Problem Identified:</h3>
<p>
  We observed two sets of spikes: one when the board receives the uploaded code and another when the upload is completed.
</p>
<p>
  This phenomenon can be seen in photos (2) and (3).
</p>

<h3>Test of Sending a Message from Python:</h3>
<p>Failed.</p>

<h3>Details:</h3>
<ul>
  <li>(1) Result of the command 11001100001111</li>
  <li>(2) Observation of spike packets before our signal</li>
  <li>(3) Zoom in on the spike packets</li>
</ul>
