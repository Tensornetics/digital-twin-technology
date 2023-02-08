import riva


class RivaASR:
    def __init__(self):
        # initialize the ASR system and load any required models or configurations
        self.asr = riva.ASR()

    def speech_to_text(self, audio_path):
        try:
            # pass in audio input and return the resulting text
            text = self.asr.convert(audio_path)
            return text
        except Exception as e:
            # handle any errors that occur during speech-to-text conversion
            print("Error during speech-to-text conversion:", e)

    def main(self, audio_path):
        # test the ASR functionality
        text = self.speech_to_text(audio_path)
        print("Recognized Text:", text)


if __name__ == '__main__':
    # test the code by passing in an audio sample
    asr = RivaASR()
    asr.main("sample_audio.wav")
