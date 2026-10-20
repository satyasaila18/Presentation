import periodic_table
def element_info(s):
    e=getattr(periodic_table,s,None)
    if e is None:
        print("Element not found")
        return
    info={
        "Name":e.name,
        "Atomic Number":e.number,
        "Atomic Mass":e.mass,
        "Density":e.density

    }
    for i,j in info.items():
        print(f'{i} : {j}')

s=input("Enter the element: ").capitalize()
element_info(s)