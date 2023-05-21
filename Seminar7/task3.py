values = [0, 2, 10, 6, 9]

def same_by(f, values):
    list_of_nosame = [i for i in map(f, values) if i != 0]
    return len(list_of_nosame) == 0

if same_by(lambda x: x%2, values):
    print("same")
else:
    print("different")