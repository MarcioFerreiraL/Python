import random
n1 = random.randint(0, 10)
n2 = random.randint(0, 10)
n3 = random.randint(0, 10)
n4 = random.randint(0, 10)
media = float((n1 + n2 + n3 + n4) / 4)
if media < 5:
    print(f'Sua media foi {media} e está REPROVADO')
    print(f"""
          Primeira nota: {n1}
          Segunda nota: {n2}
          Terceira nota: {n3}
          Quarta nota: {n4}
          """)
elif 5 < media < 6.9:
    print(f'Sua media foi {media} e está de RECUPERAÇÃO')
    print(f"""
          Primeira nota: {n1}
          Segunda nota: {n2}
          Terceira nota: {n3}
          Quarta nota: {n4}
          """)
elif 7 < media:
    print(f'Sua media foi {media} e está APROVADO')
    print(f"""
          Primeira nota: {n1}
          Segunda nota: {n2}
          Terceira nota: {n3}
          Quarta nota: {n4}
          """)