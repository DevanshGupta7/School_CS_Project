from prettytable import PrettyTable

def print_table_plan(data):
    table = PrettyTable()
    table.field_names = ["S.No", "Plans", "Duration", "Price"]

    for sno, membership_info in data.items():
        table.add_row([sno, membership_info["plan"], membership_info["duration"], membership_info["price"]])

    print(table)
    
    
def print_table_costumer(data):
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Address", "Contact no."]
    
    table.add_row([data[id], data[id]["name"], data[id]["address"], data[id]["contact"]])

    print(table)