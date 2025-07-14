def total_salary(path: str) ->tuple:
    try:
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
        
        total = 0
        count = 0       
        
        for line in lines:
            line = line.strip()
            parts = line.split(',')
            name = parts[0]
            salary = int(parts[1])
            total += salary
            count += 1
            
            
        average = total // count
        return(total, average)
    


    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return(0, 0)



def main():
    total, average = total_salary('./Перше_завдання/salary.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


main()



