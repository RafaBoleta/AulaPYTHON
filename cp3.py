# salas e temperaturas
temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]


# impor os limites de temperatura
LIMITE_CRITICO = 33

maior_criticos = 0
sala_maior_risco = 0


#calculo das medias e ordem das salas
for i, sala in enumerate(temperaturas):
    numero_sala = i + 1
    media = sum(sala) / len(sala)
    registros_criticos = sum(1 for temp in sala if temp >= LIMITE_CRITICO)

    print(f"Sala {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros Críticos: {registros_criticos}")
    print()

    if registros_criticos > maior_criticos:
        maior_criticos = registros_criticos
        sala_maior_risco = numero_sala

print(f"Sala Com Maior Risco: Sala {sala_maior_risco}")
