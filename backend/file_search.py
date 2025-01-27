import os

def search_files(query, root_dir="C:/"):
    if not os.path.isdir(root_dir):
        return "Invalid root directory"
    
    results = []
    try:
        for dirpath, _, filenames in os.walk(root_dir):
            for file in filenames:
                if query.lower() in file.lower():
                    results.append(os.path.join(dirpath, file))
                    if len(results) >= 5:  # Limit to 5 results
                        return results
    except Exception as e:
        return f"An error occurred: {e}"
    
    return results
