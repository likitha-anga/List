magic_square = [[8, 3, 4],
                [1, 7, 9],
                [6, 7, 2]]
i=0
while i<len(magic_square):
    j=0
    row=0
    column=0
    decimal=0
    while j<len(magic_square[i]):
        row+=magic_square[i][j]
        column+=magic_square[j][i]
        decimal+=magic_square[j][j]
        j+=1
    i+=1
print("row",row)
print("column",column)
print("decimal",decimal)
if row==column==decimal:
    print("magic_square")
else:
    print("not a magic square")
