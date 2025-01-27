import os

def search_files(query, root_dir="C:/"):
    results = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if query.lower() in file.lower():
                results.append(os.path.join(dirpath, file))
                if len(results) >= 5:  # Limit to 5 results
                    return results
    return results
