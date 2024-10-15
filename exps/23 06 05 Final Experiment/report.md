<h1>Experiment Report: Building our model and using it to communicate</h1>

<h2>Objective of the Experiment</h2>
<p>
    The objective of this final experiment was to combine all the other experiment to finally transmiss a message via RFID. I built the system capable of reading and decoding signals transmitted by the card using a reader, by employing a demodulation circuit (peak detector) to extract a square signal. 
    The extracted signal was then decoded using a Python program.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the card-reader model</h3>
<p>
    I assembled the card and reader circuits. 
</p>

<ul>
    <li><strong>Parameters used:</strong></li>
    <li>Inductance of coils: L1 = L2 = 36 mH</li>
    <li>Low-Frequency Generator: amplitude of 5 V peak-to-peak, frequency of 1 kHz</li>
    <li>Distance between coils : 0cm (adjusted for optimal reception)</li>
</ul>

<h3>2. Demodulation Circuit Setup (Peak Detector)</h3>
<p>
    Next, I set up the demodulation circuit to convert the RF signal into a readable square wave. A peak detector was integrated into the circuit to capture the peaks of the incoming signals, helping to isolate the significant data points.
</p>

<h3>3. Signal Reception and Python Decoding</h3>
<p>
    After successfully detecting the signal, I used an Arduino to relay the signal to a Python script for decoding. The script analyzed the incoming binary data and converted it into a meaningful message.
</p>

<h3>Results</h3>
<p>
    By fine-tuning the system, we achieved stable transmission and decoding of the binary message. The signal could be detected reliably using the peak detector, and the Python code successfully decoded the message from the RFID card.
</p>
