from prettytable import PrettyTable

table = PrettyTable()
table.add_column("S/N", ["1", "2"])
table.add_column("Name", ["Abeeb Olatunji", "Rayan"])
table.add_column("Age", ["20", "7"])
table.add_row(["3", "Almas", "4"])

table.align = "r"

print(table)