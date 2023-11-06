import funciones_parcial_2

dna_cod=[]
for _ in range(6):
        rows=[]

for _ in range(6):
        rows.append("")
        dna_cod.append(rows)

funciones_parcial_2.fill_matriz(dna_cod)

print("Código genético ingresado: ")
for i in dna_cod:
        print(i)

mutant_gene_validator=["AAAA","TTTT", "GGGG", "CCCC"]

counter=funciones_parcial_2.is_mutant(dna_cod, mutant_gene_validator)

if counter:
        print("Eres un mutante, un dios entre los insectos")
else:
        print("No eres mutante. Tu destino es la extinción")