class TaskManager:
    tasks = []

    def create_task(self,name,description):
        self.tasks.append({"name" : name,"description" : description}) # slovar

    def get_str_tasks(self): # смысл (назначение) заключается в преобразовании списка задач в единую читаемую строку.
        str_tasks = "" # Инициализирует пустую строку str_tasks
        for i in self.tasks: # Перебирает каждую задачу (i) в списке self.tasks
            str_tasks += f"{i['name']}: {i['description']}\n" """Форматирует каждую задачу в строку вида "Название 
            задачи:Описание задачи", добавляет перевод строки (\n) и присоединяет результат к общей строке str_tasks"""
        return str_tasks


