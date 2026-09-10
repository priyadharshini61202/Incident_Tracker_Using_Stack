class Incident_Tracker:

    def __init__(self):
        self.stack = []

    # PUSH
    def push_incidents(self, machine, problem, severity):
        incident = {
            "Machine": machine,
            "Problem": problem,
            "Severity": severity
        }

        self.stack.append(incident)

        print("\nIncident added successfully!")
        print(f"Machine: {machine}")
        print(f"Problem: {problem}")
        print(f"Severity: {severity}")

    # POP
    def handle_incident(self):
        if self.is_empty():
            print("\nNo incidents to handle")
            return

        incident = self.stack.pop()

        print("\nHandling Incident")
        print(f"Machine: {incident['Machine']}")
        print(f"Problem: {incident['Problem']}")
        print(f"Severity: {incident['Severity']}")

    # PEEK
    def next_incident(self):
        if self.is_empty():
            print("\nNo pending incidents.")
            return

        incident = self.stack[-1]

        print("\nNext Incident")
        print(f"Machine: {incident['Machine']}")
        print(f"Problem: {incident['Problem']}")
        print(f"Severity: {incident['Severity']}")

    # IS EMPTY
    def is_empty(self):
        return len(self.stack) == 0

    # SIZE
    def size(self):
        return len(self.stack)

    # DISPLAY
    def display(self):
        if self.is_empty():
            print("\nNo pending incidents")
            return

        print(f"\n{'-' * 15} Pending Incidents {'-' * 15}")

        for i, incident in enumerate(reversed(self.stack), start=1):
            print(
                f"{i}. "
                f"{incident['Machine']} | "
                f"{incident['Problem']} | "
                f"{incident['Severity']}"
            )

        print("-" * 50)


# ==========================================
# MAIN PROGRAM
# ==========================================

manager = Incident_Tracker()

while True:

    print("\n========== INCIDENT MANAGER ==========")
    print("1. Add Incident")
    print("2. Handle Incident")
    print("3. View Next Incident")
    print("4. View All Incidents")
    print("5. Number of Incidents")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        machine = input("Enter machine name: ")
        problem = input("Enter problem: ")
        severity = input("Enter severity (LOW/MEDIUM/HIGH): ")

        manager.push_incidents(machine, problem, severity)

    elif choice == "2":

        manager.handle_incident()

    elif choice == "3":

        manager.next_incident()

    elif choice == "4":

        manager.display()

    elif choice == "5":

        print(f"\nPending incidents: {manager.size()}")

    elif choice == "6":

        print("\nExiting Incident Manager...")
        break

    else:

        print("\nInvalid choice. Try again.")
