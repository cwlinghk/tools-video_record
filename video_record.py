import threading
import time
import cv2

class Vout:
    '''
    Real time record opencv imshow

    v = Vout()
    v.start()
    sadf   
    for i in range(100):
        v.frame = img[i]
        time.sleep(0.2)
    v.stop() 
    
    '''
    def __init__(self, vpath = 'out.mp4', size = (720,480), fps = 15.0):
        self.fps = fps
        self.dt = 1./self.fps
        self.size = size
        self.vpath = vpath

        self.frame = None
        #self.fourcc = cv2.VideoWriter_fourcc('a','c','v','1')
        #self.fourcc = cv2.VideoWriter_fourcc(*'h260')
        self.vout = cv2.VideoWriter( self.vpath, -1, self.fps, self.size)
    
    def start(self):
        threading.Thread(target=self._start, daemon=False, args=()).start()

    def write(self, img):
        self.frame = img.copy()

    def _start(self):
        print ('Recording started.')
        self.record = True
        while self.record:
            if self.frame is not None:
                frame = cv2.resize(self.frame, self.size)
                self.vout.write(frame)
                time.sleep(self.dt)
        self.vout.release()
    
    def release(self):
        self.record = False
        self.vout.release()
        print ('Recording is stopped.')

'''
class Sout:
    def __init__(self):
        import argparse
        import tempfile
        import queue
        import sys

        import sounddevice as sd
        import soundfile as sf
        import numpy  # Make sure NumPy is loaded before it is used in the callback
        assert numpy  # avoid "imported but unused" message (W0611)


        def int_or_str(text):
            """Helper function for argument parsing."""
            try:
                return int(text)
            except ValueError:
                return text


        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        args, remaining = parser.parse_known_args()
        if args.list_devices:
            print(sd.query_devices())
            parser.exit(0)
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[parser])
        parser.add_argument(
            'filename', nargs='?', metavar='FILENAME',
            help='audio file to store recording to')
        parser.add_argument(
            '-d', '--device', type=int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-r', '--samplerate', type=int, help='sampling rate')
        parser.add_argument(
            '-c', '--channels', type=int, default=1, help='number of input channels')
        parser.add_argument(
            '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
        args = parser.parse_args(remaining)

        args.filename = "test.wav"
        args.device = 1
        args.samplerate = 44100
        args.channels = 2
        args.subtype = "PCM_24"
        q = queue.Queue()


        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)
            q.put(indata.copy())


        try:
            if args.samplerate is None:
                device_info = sd.query_devices(args.device, 'input')
                # soundfile expects an int, sounddevice provides a float:
                args.samplerate = int(device_info['default_samplerate'])
            if args.filename is None:
                args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
                                                suffix='.wav', dir='')

            # Make sure the file is opened before recording anything:
            with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                            channels=args.channels, subtype=args.subtype) as file:
                with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                    channels=args.channels, callback=callback):
                    print('#' * 80)
                    print('press Ctrl+C to stop the recording')
                    print('#' * 80)
                    while True:
                        file.write(q.get())
        except KeyboardInterrupt:
            print('\nRecording finished: ' + repr(args.filename))
            parser.exit(0)
        except Exception as e:
            parser.exit(type(e).__name__ + ': ' + str(e))

x = Sout()

'''
