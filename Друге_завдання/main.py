

def get_cats_info(path: str)-> list[dict]:
    cats_list =[]
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts)==3:
                    cat_id, name, age = parts
                    cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age":age
                    }
                    cats_list.append(cat_dict)
    
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено")
        
    return cats_list
    


cats_info = get_cats_info("cats.txt")
print(cats_info)
