import json

with open('dados.json', 'r') as file:
    faturamento = json.load(file)

faturamento_dict = {}
for item in faturamento:
    faturamento_dict[item['dia']] = item['valor']

dias = len(faturamento_dict)
soma = sum(faturamento_dict.values())
media = soma / dias

menor = min(faturamento_dict.values())
maior = max(faturamento_dict.values())

superior_media = 0
for valor in faturamento_dict.values():
    if valor > media:
        superior_media += 1

print("Menor faturamento diário:", menor)
print("Maior faturamento diário:", maior)
print("Dias com faturamento diário superior à média mensal:", superior_media)
