from auth import register, login
from projects import create_project, view_all_projects, edit_project, delete_project, search_by_date

def main():
    current_user = None
    
    while True:
        print("\n==== Crowd-Funding Console App ====")
        
        if not current_user:
            # Authentication Menu
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                register()
            elif choice == "2":
                current_user = login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again")
        else:
            # Main Application Menu (logged in)
            print(f"\nWelcome, {current_user['first_name']}!")
            print("1. Create Project")
            print("2. View All Projects")
            print("3. Edit Your Projects")
            print("4. Delete Your Projects")
            print("5. Search Projects by Date")
            print("6. Logout")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                create_project(current_user)
            elif choice == "2":
                view_all_projects()
            elif choice == "3":
                edit_project(current_user)
            elif choice == "4":
                delete_project(current_user)
            elif choice == "5":
                search_by_date()
            elif choice == "6":
                current_user = None
                print("Logged out successfully!")
            else:
                print("Invalid choice, please try again")

if __name__ == "__main__":
    main()