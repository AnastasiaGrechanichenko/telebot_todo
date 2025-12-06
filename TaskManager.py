class TaskManager:
    tasks = []
    path = "cache.csv"

    def __init__(self):
        self.load_data()

    def save_data(self):
        with open(self.path,"w",encoding ="utf-8") as file:
            for task in self.tasks:
                file.write(f"{task['name']}:{task['description']}\n")
                '''Каждая task — это словарь вида: {'name': 'Купить молоко', 'description': 'Из магазина'}
                '''

    def load_data(self):
        try:
            with open(self.path,"r", encoding="utf-8")as file:
                contents = file.readlines()
                if contents =="":
                    return
                for task in contents:
                    values = task.split(":")
                    self.create_task(values[0],values[1])
        except FileNotFoundError:
            print("файл не найден")




    def create_task(self,name,description):
        self.tasks.append({"name" : name,"description" : description}) # slovar
        self.save_data()


    def get_str_tasks(self):
        if not self.tasks:# смысл (назначение) заключается в преобразовании списка задач в единую читаемую строку.
            return "нет задач"

        str_tasks = "" # Инициализирует пустую строку str_tasks
        for task in self.tasks: # Перебирает каждую задачу (i) в списке self.tasks
            str_tasks += f"{task['name']}: {task['description']}\n"
        return str_tasks


