# Настройка проекта AMD

Этот гайд поможет вам настроить и запустить лабораторную работу #1

## Предварительные условия

- Python 3.12 или выше
- pip

## Установка

1. **Клонирование репозитория**

   ```bash
   git clone git@github.com:gshjis/AMD_BSUIR.git
   cd AMD_BSUIR
   ```

2. **Создание виртуального окружения**

   ```bash
   python3 -m venv venv
   ```

3. **Активация виртуального окружения**

   - На Windows:

     ```bash
     venv\Scripts\activate
     ```

   - На macOS и Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Установка зависимостей**

   ```bash
   pip install -r requirements.txt
   ```

## Лабораторные работы

<details>
<summary>Лабораторная работа 1</summary>

**Расположение файла:** amd/Lab1.ipynb  
**Метод запуска:**  
```bash
cd amd
jupyter notebook Lab1.ipynb
```

**Видео:** [plot_lab1.mp4](amd/plot_lab1.mp4)  

Основные задачи лабораторной работы 1 включают анализ данных и построение графиков с использованием Python. Работа выполняется в Jupyter Notebook и демонстрирует базовые методы обработки данных.
</details>

<details>
<summary>Лабораторная работа 2</summary>

**Расположение файла:** amd/Lab2.ipynb  
**Метод запуска:**  
```bash
cd amd
jupyter notebook Lab2.ipynb
```

**Видео:** [plot_lab2.mp4](amd/plot_lab2.mp4)  

Лабораторная работа 2 посвящена более сложным методам анализа данных. Включает работу с многомерными массивами и построение сложных визуализаций.
</details>

## Дополнительная информация

- Убедитесь, что у вас установлены необходимые библиотеки, как указано в `requirements.txt`.
