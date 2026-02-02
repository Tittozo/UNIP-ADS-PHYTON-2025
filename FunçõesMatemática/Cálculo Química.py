def molaridade_por_massa(massa, massa_molar, volume):
    # n = massa / massa_molar
    # M = n / volume
    return massa / (massa_molar * volume)

m = float(input("Massa do soluto (g): "))
mm = float(input("Massa Molar do soluto (g/mol): "))
vol = float(input("Volume da solução (L): "))

res = molaridade_por_massa(m, mm, vol)
print(f"Resultado: {res:.3f} mol/L")
