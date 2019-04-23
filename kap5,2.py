
SH = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5, 8]

ålder_a = int(input("Hur gammal är du bitch?"))

if (ålder_a >17):
    ålderLen=16
else:
    ålderLen = ålder_a - 1

print("Du behöver sova", SH[ålderLen], "timmar")
