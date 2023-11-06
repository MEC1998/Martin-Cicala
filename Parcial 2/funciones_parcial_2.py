def fill_matriz(dna_cod):
    for i in range(6):
        while True:
            dna_sequency= input("Ingrese una secuencia de ADN, 6 caracteres (A, T, G, C): ").upper()
            if len(dna_sequency)!=6:
                print("La cadena debe contener exactamente 6 caracteres.")
            else:
                validator=True
                for element in dna_sequency:
                    if element not in "ATGC":
                        print("¡ERROR! Ingrese un dato válido (A, T, G, C)")    
                        validator=False
                        break
                if validator:
                    dna_cod[i]=list(dna_sequency)
                    break
    return dna_cod

def is_mutant(dna_code, mutant_gene_validator):
    counter=0

    for i in dna_code:
        actual_row=""
        for j in i:
            actual_row+=j
        for element in mutant_gene_validator:
            if element in actual_row:
                counter+=1

    for i in range(6):
        actual_column=""
        for j in range(6):
            actual_column+=dna_code[i][j]
        for element in mutant_gene_validator:
            if element in actual_column:
                counter+=1
    
    principal_diagonal=""
    secondary_diagonal=""
    for i in range(6):
        principal_diagonal+=dna_code[i][i]
        secondary_diagonal+=dna_code[i][5 - i]
    for element in mutant_gene_validator:
        if element in principal_diagonal or element in secondary_diagonal:
            counter += 1

    print (f"Secuencias mutantes encontradas: {counter}")

    if counter>=2:
        return True
    else:
        return False
        