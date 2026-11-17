# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
# Deterministic: same bytes on every run. No network.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The kettle has stopped singing.",
        "On the counter it ticks once, cooling, and then is quiet.",
        "",
        "Afternoon light comes in low through the kitchen window. It lies across the floorboards in one long pale strip, and dust moves in it, slow as anything.",
        "",
        "Outside, a sparrow lands on the fence. It looks around, and decides to stay.",
        "",
        "The light is not in a hurry. It will take its time crossing the floor. When it reaches the far wall, it will rest there a while, and the room will hold it.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
