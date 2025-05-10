from datetime import datetime
from auth import load_data, save_data



# ===============create project ====================== 

def create_project(user):
    data = load_data()
    projects = data['projects']
    
    print("\n=== Create New Project ===")
    project = {
        'id': len(projects) + 1,
        'owner_id': user['id'],
        'title': input("Project Title: ").strip(),
        'details': input("Project Details: ").strip(),
        'total_target': float(input("Total Target (EGP): ")),
        'start_date': input("Start Date (YYYY-MM-DD): ").strip(),
        'end_date': input("End Date (YYYY-MM-DD): ").strip(),
        'created_at': datetime.now().isoformat()
    }
    
    # Basic date validation
    try:
        start = datetime.fromisoformat(project['start_date'])
        end = datetime.fromisoformat(project['end_date'])
        if end <= start:
            print("End date must be after start date!")
            return
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD")
        return
    
    projects.append(project)
    data['projects'] = projects
    save_data(data)
    print("Project created successfully!")



# =============== View project ====================== 
def view_all_projects():
    data = load_data()
    projects = data['projects']
    
    print("\n=== All Projects ===")
    if not projects:
        print("No projects found.")
        return
    
    for idx, project in enumerate(projects, 1):
        print(f"\nProject {idx}:")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['total_target']} EGP")
        print(f"Dates: {project['start_date']} to {project['end_date']}")

# =============== Edit project ====================== 
def edit_project(user):
    data = load_data()
    projects = data['projects']
    
    # Show only user's projects
    user_projects = [p for p in projects if p['owner_id'] == user['id']]
    if not user_projects:
        print("You have no projects to edit.")
        return
    
    print("\n=== Your Projects ===")
    for idx, project in enumerate(user_projects, 1):
        print(f"{idx}. {project['title']} (Target: {project['total_target']} EGP)")
    
    try:
        choice = int(input("Select project to edit (number): ")) - 1
        if 0 <= choice < len(user_projects):
            project = user_projects[choice]
            print(f"\nEditing: {project['title']}")
            
            # Get updated values (keep old if empty)
            title = input(f"Title [{project['title']}]: ").strip() or project['title']
            details = input(f"Details [{project['details']}]: ").strip() or project['details']
            total_target = input(f"Target [{project['total_target']}]: ").strip()
            total_target = float(total_target) if total_target else project['total_target']
            
            # Update the project
            project['title'] = title
            project['details'] = details
            project['total_target'] = total_target
            
            save_data(data)
            print("Project updated successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")        



# =============== Delete project ====================== 
def delete_project(user):
    data = load_data()
    projects = data['projects']
    
    user_projects = [p for p in projects if p['owner_id'] == user['id']]
    if not user_projects:
        print("You have no projects to delete.")
        return
    
    print("\n=== Your Projects ===")
    for idx, project in enumerate(user_projects, 1):
        print(f"{idx}. {project['title']}")
    
    try:
        choice = int(input("Select project to delete (number): ")) - 1
        if 0 <= choice < len(user_projects):
            project = user_projects[choice]
            print(f"\nDeleting: {project['title']}")
            confirm = input("Are you sure? (y/n): ").lower()
            
            if confirm == 'y':
                projects.remove(project)
                save_data(data)
                print("Project deleted successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")    


#=============== Search for project ====================
def search_by_date():
    data = load_data()
    projects = data['projects']
    
    if not projects:
        print("No projects available to search.")
        return
    
    date_str = input("Enter date to search (YYYY-MM-DD): ").strip()
    try:
        search_date = datetime.fromisoformat(date_str).date()
        print(f"\nProjects active on {date_str}:")
        
        found = False
        for project in projects:
            start = datetime.fromisoformat(project['start_date']).date()
            end = datetime.fromisoformat(project['end_date']).date()
            
            if start <= search_date <= end:
                print(f"\nTitle: {project['title']}")
                print(f"Details: {project['details']}")
                print(f"Active: {project['start_date']} to {project['end_date']}")
                found = True
        
        if not found:
            print("No projects found for this date.")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD")