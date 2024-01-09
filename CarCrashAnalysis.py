import pandas
from matplotlib import pyplot as plt

#names = ["Year", "Month", "Day", "Weekend", "Hour", "Collision Type", "Injury Type", "Primary Factor", "Reported_Location", "Latitude", "Longitude"]

df = pandas.read_excel("new dataset.xlsx")
df_size = df.shape[0]

grouped_injury = df.groupby("Injury Type")
fatal_injury_count = grouped_injury.get_group("Fatal")
incapacitating_injury_count = grouped_injury.get_group("Incapacitating")
non_incapacitating_injury_count = grouped_injury.get_group("Non-incapacitating")
no_injury_unknown_injury_count = grouped_injury.get_group("No injury/unknown")


def crash_col_type(type):
    if type == "1":
        fatal_injury_by_col_type = fatal_injury_count.groupby('Collision Type').size()
        fatal_injury_by_col_type.plot(kind = "bar")
        plt.title("Collision Type vs Number of fatal injuries")
        plt.xlabel("Collision Type")
        plt.ylabel("Number of fatal injuries")
    elif type == "2":
        incapacitating_injury_type = incapacitating_injury_count.groupby('Collision Type').size()
        incapacitating_injury_type.plot(kind = "bar")
        plt.title("Collision Type vs Number of Incapacitating Injuries")
        plt.xlabel("Collision Type")
        plt.ylabel("Number of Incapacitating Injuries")
    elif type == "3":
        non_incapacitating_injury_type = non_incapacitating_injury_count.groupby('Collision Type').size()
        non_incapacitating_injury_type.plot(kind = "bar")
        plt.title("Collision Type vs Number of Non-Incapacitating Injuries")
        plt.xlabel("Collision Type")
        plt.ylabel("Number of Non-Incapacitating Injuries")
    elif type == "4":
        no_injury_unknown_injury_type = no_injury_unknown_injury_count.groupby('Collision Type').size()
        no_injury_unknown_injury_type.plot(kind = "bar")
        plt.title("Collision Type vs Number of No injury/unknown")
        plt.xlabel("Collision Type")
        plt.ylabel("Number of No injury/unknown")
    else:
        raise KeyError("type of injury not found...")
    return plt.show()      

def crash_factor(type):
    if type == "1":
        fatal_common_factor_type = fatal_injury_count.groupby("Primary Factor").size()
        fatal_common_factor_type.plot(kind = "bar")
        plt.title("Primary Factor vs Number of fatal injuries")
        plt.xlabel("Primary Factor")
        plt.ylabel("Number of fatal injuries")
    elif type == "2":
        incapacitating_injury_type = incapacitating_injury_count.groupby("Primary Factor").size()
        incapacitating_injury_type.plot(kind = "bar")
        plt.title("Primary Factor vs Number of Incapacitating Injuries")
        plt.xlabel("Primary Factor")
        plt.ylabel("Number of Incapacitating Injuries")
    elif type == "3":
        non_incapacitating_injury_type = non_incapacitating_injury_count.groupby("Primary Factor").size()
        non_incapacitating_injury_type.plot(kind = "bar")
        plt.title("Primary Factor vs Number of Non-Incapacitating Injuries")
        plt.xlabel("Primary Factor")
        plt.ylabel("Number of Non-Incapacitating Injuries")
    elif type == "4":
        no_injury_unknown_injury_type = no_injury_unknown_injury_count.groupby("Primary Factor").size()
        no_injury_unknown_injury_type.plot(kind = "bar")
        plt.title("Primary Factor vs Number of No injury/unknown")
        plt.xlabel("Primary Factor")
        plt.ylabel("Number of No injury/unknown")
    else:
        raise KeyError("type of injury not found...")
    return plt.show()

def crash_hour(type):
    if type == "1":
        fatal_time = fatal_injury_count.groupby("Hour").size()
        fatal_time.plot(kind = "bar")
        plt.title("Hour vs Number of fatal injuries")
        plt.xlabel("Hour")
        plt.ylabel("Number of fatal injuries")
    elif type == "2":
        incapacitating_injury_type = incapacitating_injury_count.groupby("Hour").size()
        incapacitating_injury_type.plot(kind = "bar")
        plt.title("Hour of Day vs Number of Incapacitating Injuries")
        plt.xlabel("Hour of Day")
        plt.ylabel("Number of Incapacitating Injuries")
    elif type == "3":
        non_incapacitating_injury_type = non_incapacitating_injury_count.groupby("Hour").size()
        non_incapacitating_injury_type.plot(kind = "bar")
        plt.title("Hour of Day vs Number of Non-Incapacitating Injuries")
        plt.xlabel("Hour of Day")
        plt.ylabel("Number of Non-Incapacitating Injuries")
    elif type == "4":
        no_injury_unknown_injury_type = no_injury_unknown_injury_count.groupby("Hour").size()
        no_injury_unknown_injury_type.plot(kind = "bar")
        plt.title("Hour of Day vs Number of No injury/unknown")
        plt.xlabel("Hour of Dayr")
        plt.ylabel("Number of No injury/unknown")
    else:
        raise KeyError("type of injury not found...")
    return plt.show()

def crash_percentage(type):
    if type == "1":
        return round((fatal_injury_count.shape[0] / df_size * 100), 6)
    elif type == "2":
        return round((incapacitating_injury_count.shape[0] / df_size * 100), 6)
    elif type == "3":
         return round((non_incapacitating_injury_count.shape[0] / df_size * 100), 6)
    elif type == "4":
         return round((no_injury_unknown_injury_count.shape[0] / df_size * 100), 6)
    else:
        raise KeyError("type of injury not found...")

if __name__ == "__main__":
    print("Car Crash Data Analysis\n")
    print(f"{df_size} total crashes in dataset\n")
    print("-"*30)
    print("1: Fatal crash data\n")
    print("2: Incapacitating crash data\n")
    print("3: Non-incapacitating crash data\n")
    print("4: No injury/unknown crash data\n")
    print("-"*30)
    values = ["1","2","3","4"]
    while True:
        injury_selection = input("select 1-4: ")
        if injury_selection in values:
            break
        else:
            print("Invalid input, please try again.")
    print("1: Collision Type\n")
    print("2: Primary Factor\n")
    print("3: Hour of Crash\n")
    print("4: Crash Percentage\n")
    print("-"*30)
    while True:
        type_of_data = input("select 1-4: ")
        if type_of_data in values:
            break
        else:
            print("Invalid input, please try again.")
    if type_of_data == "1":
        print("Returning crash collision data...")
        crash_col_type(injury_selection)
    elif type_of_data == "2":
        print("Returning crash factor data...")
        crash_factor(injury_selection)
    elif type_of_data == "3":
        print("Returning hour of crash data...")
        crash_hour(injury_selection)
    elif type_of_data == "4":
        print("Return percentage of crash data...")
        crash_percentage(injury_selection)
    else:
        raise KeyError("Type of data not found...")