import sys
import os
from faster_whisper import WhisperModel

audio_file = sys.argv[1]
print(f"Loading model... (base)")
model = WhisperModel("base", device="cpu", compute_type="float32", cpu_threads=4)
print(f"Transcribing {audio_file}...")
segments, info = model.transcribe(audio_file, beam_size=5)

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
