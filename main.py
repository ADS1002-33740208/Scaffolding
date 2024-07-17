from scaffold_job import ScaffoldJob
from job_dict import JobDictionary
from excel_handler import ExcelHandler

jobs = JobDictionary()
excel_handler = ExcelHandler("Sunline_Scaffolding_Database.xlsx", jobs)

def main_menu():
    print("\nMain Menu")
    print("1. Select Job")
    print("2. Create New Job")
    print("3. Delete Job")
    print("4. Save to Excel")
    print("5. Quit")
    choice = input("Enter your choice: ").strip()
    return choice

def job_menu():
    print("\nCurrent Jobs")
    job_names = list(jobs.jobs.keys())
    if not job_names:
        print("No jobs available.")
    for index, job_name in enumerate(job_names):
        print(f"{index}. {job_name}")
    job_choice = input("Enter your job number: ").strip()
    return job_choice

def create_new_job():
    job_name = input("Enter new job name: ").strip()
    if job_name in jobs.jobs:
        print(f"Job '{job_name}' already exists.")
    else:
        new_job = ScaffoldJob(job_name)
        jobs.jobs[job_name] = new_job
        print(f"Created new job '{job_name}'.")

def delete_job():
    job_name = input("Enter job name to delete: ").strip()
    if job_name in jobs.jobs:
        jobs.delete_job(job_name)
        print(f"Deleted job '{job_name}'.")
    else:
        print(f"Job '{job_name}' not found.")

def edit_menu(job_choice):
    job_name = list(jobs.jobs.keys())[int(job_choice)]
    job = jobs.jobs[job_name]
    while True:
        print(f"\nEditing Job: {job_name}")
        print("1. Add Scaffold")
        print("2. Delete Scaffold")
        print("3. Display Current Scaffold")
        print("4. Clear All Scaffold")
        print("5. Return to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            job.add_scaffold()
        elif choice == '2':
            job.delete_scaffold()
        elif choice == '3':
            print(job)
        elif choice == '4':
            job.clear_scaffold()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    excel_handler.load_from_excel()
    while True:
        choice = main_menu()
        if choice == '1':
            job_choice = job_menu()
            if job_choice.isdigit() and int(job_choice) < len(jobs.jobs):
                edit_menu(job_choice)
            else:
                print("Invalid job number.")
        elif choice == '2':
            create_new_job()
        elif choice == '3':
            delete_job()
        elif choice == '4':
            excel_handler.save_to_excel()
        elif choice == '5':
            print("Session ended.")
            break
        else:
            print("Invalid choice.")

