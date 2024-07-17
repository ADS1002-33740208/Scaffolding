from datetime import datetime
from typing import Dict

class ScaffoldJob:
    def __init__(self, name: str):
        self.name = name
        self.scaffold = {}  # Use a dictionary to store items and quantities
        self.dates = {}  # Use a dictionary to store the dates when items are added
        self.deletions = {}  # Use a dictionary to store deletions and their dates

    def get_name(self) -> str:
        return self.name

    def add_scaffold(self):
        print(f"Adding scaffold for job '{self.name}'")
        print("Paste scaffold items (item, quantity) separated by new lines (empty line to finish):")
        lines = []
        while True:
            line = input().strip()
            if not line:
                break
            lines.append(line)
        date_added = input("Enter date for all items (DD/MM/YYYY): ")
        try:
            date_added = datetime.strptime(date_added, '%d/%m/%Y').date()
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY format.")
            return
        for line in lines:
            parts = line.rsplit(' ', 1)
            if len(parts) >= 2:
                item = parts[0].strip()
                try:
                    quantity = float(parts[1]) if '.' in parts[1] else int(parts[1])
                    self.scaffold[item] = quantity
                    self.dates[item] = date_added
                except ValueError:
                    print(f"Warning: Could not parse quantity for line: '{line}'")
            else:
                print(f"Warning: Could not parse line: '{line}'")
        return self

    def delete_scaffold(self):
        if self.scaffold:
            print(f"Scaffold items in job '{self.name}':")
            for item, quantity in self.scaffold.items():
                print(f"{item}: {quantity} (Added on {self.dates[item].strftime('%d/%m/%Y')})")
            print("Paste scaffold items to delete (item, quantity) separated by new lines (empty line to finish):")
            lines = []
            while True:
                line = input().strip()
                if not line:
                    break
                lines.append(line)
            date_deleted = input("Enter deletion date (DD/MM/YYYY): ")
            try:
                date_deleted = datetime.strptime(date_deleted, '%d/%m/%Y').date()
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY format.")
                return
            for line in lines:
                parts = line.strip().rsplit(' ', 1)
                if len(parts) == 2:
                    item, quantity = parts
                    item = item.strip()
                    try:
                        quantity = float(quantity) if '.' in quantity else int(quantity)
                        if item in self.scaffold:
                            if self.scaffold[item] > quantity:
                                self.scaffold[item] -= quantity
                                print(f"Reduced scaffold item '{item}' by {quantity} from job '{self.name}'")
                            elif self.scaffold[item] == quantity:
                                del self.scaffold[item]
                                del self.dates[item]
                                print(f"Deleted scaffold item '{item}' from job '{self.name}'")
                            else:
                                print(f"Cannot delete {quantity} of '{item}', only {self.scaffold[item]} available")
                            if item in self.deletions:
                                self.deletions[item].append((quantity, date_deleted))
                            else:
                                self.deletions[item] = [(quantity, date_deleted)]
                        else:
                            print(f"Scaffold item '{item}' not found in job '{self.name}'")
                    except ValueError:
                        print(f"Warning: Could not parse quantity for line: '{line}'")
                else:
                    print(f"Warning: Could not parse line: '{line}'")
        else:
            print(f"No scaffold found for job '{self.name}'")

    def to_dict(self) -> Dict[str, float]:
        """
        Returns a dictionary representation of the ScaffoldJob instance.
        """
        return self.scaffold

    def to_dates_dict(self) -> Dict[str, datetime]:
        """
        Returns a dictionary of scaffold items and their added dates.
        """
        return self.dates

    def __str__(self) -> str:
        output = f"Job name: {self.name}\n"
        if self.scaffold:
            output += "Scaffold items:\n"
            for item, quantity in self.scaffold.items():
                output += f"- {item}: {quantity} (Added on {self.dates[item].strftime('%d/%m/%Y')})\n"
        else:
            output += "No scaffold items found\n"
        return output
    
    def clear_scaffold(self):
        self.scaffold.clear()
        self.dates.clear()
        self.deletions.clear()
        print(f"All scaffold items for job '{self.name}' have been cleared.")
