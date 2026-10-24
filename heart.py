import math
import random
import tkinter as tk

# Initialize window
root = tk.Tk()
root.title("I Love You Heart")
root.geometry("900x750")
root.configure(bg="black")

# Bring window to front
root.attributes("-topmost", True)
root.update()
root.attributes("-topmost", False)

canvas = tk.Canvas(root, width=900, height=750, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)   

phrases = [
    "I love you",
    "Te amo",
    "Je t'aime",
    "Ich liebe dich",
    "Ti amo",
    "Te quiero",
    "Eu te amo",
    "Я тебя люблю",
    "사랑해",
    "愛してる",
    "Wǒ ài nǐ",
    "Mahal kita",
    "Seni seviyorum",
    "Aloha wau ia oe",
    "Jeg elsker dig",
    "Kocham Cię",
    "Σ' αγαπώ",
    "אני אוהב אותך",
    "أحبك",
    "मैं तुमसे प्यार करता हूँ",
]

# Generate points with dense center layers and refined edge scaling
target_points = []
for scale in [0.9, 0.78, 0.65, 0.52, 0.38, 0.25, 0.12]:
  t = 0
  while t < 2 * math.pi:
    x = 16 * (math.sin(t) ** 3)
    y = -(
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

    px = 450 + x * 22 * scale
    py = 375 + y * 22 * scale - 12

    # Tighter distance filter for the center core to pack it solid, wider at edges for clarity
    min_dist = 35 if scale < 0.4 else 46

    too_close = False
    for ex, ey in target_points:
      if math.hypot(px - ex, py - ey) < min_dist:
        too_close = True
        break

    if not too_close:
      target_points.append((px, py))

    t += 0.14

# Sort points to reveal smoothly from the center outwards
target_points.sort(key=lambda p: (p[1] - 375) ** 2 + (p[0] - 450) ** 2)

current_index = 0  


def draw_next_phrases():
  global current_index
  if current_index < len(target_points):
    # Reveal phrases progressively for smooth animation
    for _ in range(2):
      if current_index >= len(target_points):
        break
      x, y = target_points[current_index]
      text = phrases[current_index % len(phrases)]

      # Vibrant glowing red tones
      color = random.choice(["#ff1e50", "#ff3366", "#ff4d79", "#ff0033"])

      canvas.create_text(
          x,
          y,
          text=text,
          fill=color,
          font=("Arial", 8, "bold"),
          anchor="center",
      )
      current_index += 1

    root.after(30, draw_next_phrases)


# Start the animation loop
root.after(300, draw_next_phrases)

root.mainloop()