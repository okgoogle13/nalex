import sys
from faster_whisper import WhisperModel

print("Loading model...")
model = WhisperModel("base", device="cpu", compute_type="float32", cpu_threads=4)
print("Transcribing...")
segments, info = model.transcribe("data/heated_talk_2m.wav", beam_size=5)

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
