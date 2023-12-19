import random
produtos = (
'Produto1',
92,
'Produto2',
85,
'Produto3',
95,
'Produto4',
99,
'Produto5',
71,
'Produto6',
10,
'Produto7',
42,
'Produto8',
22,
'Produto9',
30,
'Produto10',
90,
)
print('=' * 34)
for c in range(0, len(produtos), 2):
    print(f' {produtos[c]:.<15}{produtos[c+1]:.>13}R$')
print('=' * 34)