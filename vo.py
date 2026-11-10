import sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro('tts/kokoro-v1.0.int8.onnx', 'tts/voices-v1.0.bin')
lines = [
 (0.6, "Everyday privacy."),
 (6.2, "Your day is logged. Every purchase, chat and location ping is sent to someone else's server."),
 (14.2, "Shopping builds a profile: what you buy, where you live, your habits."),
 (22.2, "Talk to an AI, and your prompts may be stored and used for training."),
 (30.2, "And servers get breached. Billions of records spill out."),
 (38.2, "Money is no different. Most blockchains show every address and amount. Shielded Zcash hides them."),
 (48.4, "Pick a wallet that supports shielded Zcash: on your phone, your desktop, or a hardware device."),
 (66.0, "Pay, donate, save, and tip, privately."),
 (70.6, "Take your privacy back."),
]
sr = 24000; total = float(sys.argv[1]); out = np.zeros(int(total*sr)+sr, dtype=np.float32)
for t, txt in lines:
    a, sr2 = k.create(txt, voice='af_heart', speed=1.08, lang='en-us'); assert sr2 == sr
    i = int(t*sr); end = min(len(out), i+len(a)); out[i:end] += a[:end-i]
    print(f"{t:5.1f}s +{len(a)/sr:4.1f}s {txt[:40]}")
sf.write('out/vo.wav', out[:int(total*sr)], sr)
