from prettytable import PrettyTable
from variables import memberships
from datetime import datetime

def print_table_plan(data):
    table = PrettyTable()
    table.field_names = ["ID", "Plans", "Duration", "Price"]

    for sno, membership_info in data.items():
        table.add_row([sno, membership_info["plan"], membership_info["duration"], membership_info["price"]])

    print(table)
    
    
def print_table_costumer(data, id):
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Address", "Contact no."]
    
    table.add_row([id, data[id]["name"], data[id]["address"], data[id]["contact"]])

    print(table)
    
    
def print_table_costumer_details(data_customer):
    table = PrettyTable()
    table.field_names = ["S.No", "ID", "Name", "Address", "Contact", "Membership", "Plan", "Start Date", "End Date"]
    sno = 1
        
    for id in data_customer:
        customer_info = data_customer[id]
        if id in memberships:
            membership_info = memberships[id]
            
            start_date_str = membership_info["start_date"]
            start_date_strp = datetime.strptime(start_date_str, "%Y%m%d").date()
            formatted_start_date_str = start_date_strp.strftime("%d-%m-%Y")
            
            end_date_str = membership_info["end_date"]
            end_date_strp = datetime.strptime(end_date_str, "%Y%m%d").date()
            formatted_end_date_str = end_date_strp.strftime("%d-%m-%Y")
            
            table.add_row([sno, id, customer_info["name"], customer_info["address"], customer_info["contact"], membership_info["Membership"],
                        membership_info["plan"], formatted_start_date_str, formatted_end_date_str])
        else:
            membership_info = {'Membership': '--', 'plan': '--', 'start_date': '--', 'end_date': '--'}

            table.add_row([sno, id, customer_info["name"], customer_info["address"], customer_info["contact"], membership_info["Membership"],
                        membership_info["plan"], membership_info["start_date"], membership_info["end_date"]])
        
        sno += 1
        
    print(table)


