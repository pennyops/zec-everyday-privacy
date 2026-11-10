# Everyday Privacy (draft)

A 72-second 1080p30 motion explainer: everyday data collection (shopping, AI chats, breaches) -> transparent ledgers -> shielded ZEC -> wallets -> use cases -> call to action (zechub.wiki/wallets).

- Watch: `everyday-privacy-draft.mp4`
- All shapes are original and drawn in Python (Pillow). Scenes are rendered to frames and joined with ffmpeg. The audio is a synthesized ambient pad.
- Scenes: `proto.py` (S1 title), `s2.py`, `s3.py shop|ai` (S3/S4), `s5.py`...`s9.py`. Plan in `storyboard.md`.

Render: `pip install pillow`, run each script, then `ffmpeg -framerate 30 -i frames_sN/f%04d.png -c:v libx264 -pix_fmt yuv420p sN.mp4` and concat.

Status: draft for review. Wallet logos and voiceover are still to come.
