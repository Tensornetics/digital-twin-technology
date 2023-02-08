import nvidia_nemo


class NemoASR:
    def __init__(self, model_path):
        self.model = nvidia_nemo.ASRModel(model_path)

    def transcribe(self, audio):
        return self.model.transcribe(audio)
