from prettytable import PrettyTable

def print_table(data):
    table = PrettyTable()
    table.field_names = ["S.No", "Plans", "Duration", "Price"]

    for sno, membership_info in data.items():
        table.add_row([sno, membership_info["plan"],
                      membership_info["duration"], membership_info["price"]])

    print(table)