# Everyday Privacy (draft)

A 72-second 1080p30 motion explainer: everyday data collection (shopping, AI chats, breaches) -> transparent ledgers -> shielded ZEC -> wallets -> use cases -> call to action (zechub.wiki/wallets).

- Watch: `everyday-privacy-draft.mp4`
- Shapes are original and drawn in Python (Pillow). Scenes are rendered to frames and joined with ffmpeg. The audio is a synthesized ambient pad.
- The wallet images (S7) and the ZecHub mark (S9) come from zechub.wiki (`/content-images/wallets/*.webp`, `/ZecHubBlue.png`). Download them into `assets/` before rendering.
- Scenes: `proto.py` (S1 title), `s2.py`, `s3.py shop|ai` (S3/S4), `s5.py`...`s9.py`. Plan in `storyboard.md`.

Render: `pip install pillow`, run each script, then `ffmpeg -framerate 30 -i frames_sN/f%04d.png -c:v libx264 -pix_fmt yuv420p sN.mp4` and concat.

Status: draft for review. Wallet images and the ZecHub mark are in. Voiceover is optional; it can be added on request.
