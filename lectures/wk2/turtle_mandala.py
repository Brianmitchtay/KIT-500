# This AI Generated program attempted to create a fractal pattern by creating concentric cricles of simple flowers

import turtle as t
import math

# One lotus flower: several curved petals in a ring
def lotus_flower(petals=6, petal_radius=15, petal_extent=50):
    angle = 360 / petals
    for _ in range(petals):
        t.down()
        t.circle(petal_radius, petal_extent)
        t.left(180 - petal_extent)
        t.circle(petal_radius, petal_extent)
        t.left(180 - petal_extent)
        t.up()
        t.left(angle)


def main():
    t.speed(0)
    t.hideturtle()
    t.bgcolor("midnight blue")
    t.pensize(1)

    # Fractal-style: concentric rings. Each ring has N flowers at radius R.
    # Spacing so flowers don't overlap: arc length = 2*pi*R/N >= 4*petal_radius
    # So petal_radius <= pi*R/(2*N). We use 0.4 * pi*R/N for a small gap.
    rings = [
        (42, 6),   # (radius, number of flowers)
        (84, 12),
        (126, 18),
        (168, 24),
        (280, 40),
    ]
    # Total: 6+12+18+24+40 = 100 flowers

    colors = ["#ffb7c5", "#ff9eb5", "#ff85a5", "#e8a0bf", "#d4a5a5", "#c9a0b5"]
    flower_index = 0

    for ring_idx, (R, N) in enumerate(rings):
        # Petal size so flowers don't overlap on this ring
        petal_radius = 0.4 * math.pi * R / N
        petal_radius = max(4, min(petal_radius, 18))  # clamp for visibility
        step = 360 / N
        # Offset each ring by half a step so rings don't line up (fractal look)
        start_angle = (ring_idx % 2) * (step / 2)

        for i in range(N):
            t.color(colors[flower_index % len(colors)])
            angle = start_angle + i * step
            t.setheading(angle)
            t.forward(R)
            lotus_flower(petals=6, petal_radius=petal_radius, petal_extent=45)
            t.home()
            flower_index += 1

    t.mainloop()


if __name__ == "__main__":
    main()
