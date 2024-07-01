from pyOpenBCI import OpenBCICyton

def print_raw(sample):
    print(sample.channels_data)

board = OpenBCICyton(port='COM4', daisy=False) # COM4 correct input

board.start_stream(print_raw)


