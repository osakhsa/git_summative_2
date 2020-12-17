def hanoi(ring, sp, d):
    if ring > 0:
        hanoi(ring - 1, sp, -d)
        print(sp, "->", (sp + d) % 3, "  (", ring, ")")
        hanoi(ring-1, (sp-d) % 3, -d)

