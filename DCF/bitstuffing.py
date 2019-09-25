
#!/usr/bin/env python

def stringbits(bits):
    n_bits = ''
    for bit in bits:
        n_bits += str(bit)
    return n_bits


def bitstuffing(bits):
    counter = 0
    for bit in range(len(bits)):
        if counter == 5:
            counter = 0
            bits.insert(bit, 0)
        if bits[bit] == 1:
           counter += 1
        if bits[bit] == 0:
            counter = 0
    return bits

def framing(stuffed):
    frame = '01111110'
    for bit in stuffed:
        frame+= str(bit)
    return frame + '01111110'


if __name__ == '__main__':
    bits = [0,1,1,1,1,1,1,0,1,1,1,1,1,1,0]
    print('Before Stuffing: {} -- {} characters'.format(stringbits(bits), len(bits)))
    stuffed = bitstuffing(bits)
    print('After Stuffing: {} -- {} characters'.format(stringbits(stuffed), len(stuffed)))
    frame = framing(stuffed)
    print('After Framing: {}'.format(frame))


