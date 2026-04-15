import sys

def variable_explorer():
    print("\n🔍 VARIABLE EXPLORER\n")

    value = input("Enter any value: ")

    # Try type casting
    try:
        value = int(value)
    except:
        try:
            value = float(value)
        except:
            pass  # keep as string

    print("\n📊 Analysis:")
    print(f"Value       : {value}")
    print(f"Type        : {type(value)}")
    print(f"Is Integer? : {isinstance(value, int)}")
    print(f"Memory ID   : {id(value)}")
    print(f"Size (bytes): {sys.getsizeof(value)}")
    print(f"Truthy?     : {bool(value)}")


# Stretch: mutable vs immutable
def compare_ids():
    print("\n⚡ Mutable vs Immutable Demo\n")

    x = 10
    print(f"Original int ID: {id(x)}")
    x += 1
    print(f"After change ID: {id(x)} (immutable)\n")

    lst = [1, 2, 3]
    print(f"Original list ID: {id(lst)}")
    lst.append(4)
    print(f"After change ID: {id(lst)} (mutable)")


variable_explorer()
compare_ids()