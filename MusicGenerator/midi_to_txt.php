open( 'output.txt', 'w' ).write( __import__( 'binascii' ).hexlify( open( 'input.midi' ).read() ) )  