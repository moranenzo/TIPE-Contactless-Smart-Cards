# These Python scripts implement Hamming Error-Correcting Codes.
# They allowed us to detect and correct specific transmission errors.
# This was essential to ensure the integrity of the messages transmitted over the RFID link,
# especially during our custom message experiments.
# This approach helped us understand the fundamentals of error correction in digital communication.


def parity(bits):
    "Function that returns the parity bit of a binary word given as a list of 0s and 1s"
    bit_sum = 0
    for i in range(len(bits)):  # calculate the sum of the bits
        bit_sum += bits[i]
        if bit_sum % 2 == 0:  # check the parity of the bit sum
            return 0
        else:
            return 1


def encode_hamming(data):
    "Function that returns a message encoded using the 7-bit Hamming code from an argument named 'data', which is a 4-bit message given as a list of 0s and 1s"
    d1, d2, d3, d4 = [data[i] for i in range(len(data))]
    p1 = parity([d1, d2, d4])  # parity calculation for triplet 1
    p2 = parity([d1, d3, d4])  # parity calculation for triplet 2
    p3 = parity([d2, d3, d4])  # parity calculation for triplet 3
    return [p1, p2, d1, p3, d2, d3, d4]


def decode_hamming(message):
    "Function that returns the decoded message, corrected in case of a detected error using the Hamming technique. We assume there is at most one error"
    m1, m2, m3, m4, m5, m6, m7 = [message[i] for i in range(len(message))]
    c1 = parity([m4, m5, m6, m7])
    c2 = parity([m2, m3, m6, m7])
    c3 = parity([m1, m3, m5, m7])
    decoded_message = [message[2], message[4], message[5], message[6]]
    if c1 == 0 and c2 == 0 and c3 == 0:
        return decoded_message  # return the decoded message if no error
    else:
        error_position = c1 * 4 + c2 * 2 + c3  # compute the error position in the decoded message
        print("A transmission error was detected at bit position", error_position)
        if decoded_message[error_position - 1] == 1:  # flip the erroneous bit value
            decoded_message[error_position - 1] = 0
        else:
            decoded_message[error_position - 1] = 1
        return decoded_message  # return the corrected decoded message
