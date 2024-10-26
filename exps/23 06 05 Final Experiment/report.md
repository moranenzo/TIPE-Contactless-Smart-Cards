<h1>Experiment Report: Building Our Model and Enabling Communication via RFID</h1>

<h2>Objective of the Experiment</h2>
<p>
    The objective of this final experiment was to integrate previous experiments and successfully transmit a message via RFID. I constructed a system capable of reading and decoding signals transmitted by the card using a reader, which employed a demodulation circuit (peak detector) to extract a square wave signal. The extracted signal was then decoded using a Python program.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the Card-Reader Model</h3>
<p>
    I assembled the card and reader circuits.
</p>

<ul>
    <li><strong>Parameters used:</strong></li>
    <ul>
        <li>Inductance of coils: L1 = L2 = 36 mH</li>
        <li>Low-Frequency Generator: amplitude of 5 V peak-to-peak, frequency of 1 kHz</li>
        <li>Distance between coils: 0 cm (optimized for maximum reception)</li>
    </ul>
</ul>

<h3>2. Demodulation Circuit Setup (Peak Detector)</h3>
<p>
    I set up the demodulation circuit to convert the RF signal into a readable square wave. A peak detector was integrated into the circuit to capture the peaks of the incoming signals, effectively isolating the critical data points for transmission.
</p>

<h3>3. Signal Reception and Python Decoding</h3>
<p>
    After successful signal detection, I used an Arduino to relay the signal to a Python script for decoding. The script analyzed the incoming binary data and accurately converted it into a readable message.
</p>

<h2>Results</h2>
<p>
    Fine-tuning the system allowed for stable transmission and reliable decoding of the binary message. The signal was detected effectively using the peak detector, and the Python code successfully interpreted the message transmitted from the RFID card.
</p>
