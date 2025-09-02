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

## Запуск проекта

1. **Просмотр Jupyter Notebook**

   Перейдите в директорию `amd` и откройте `Lab1.ipynb` с помощью Jupyter Notebook.

   ```bash
   cd amd
   jupyter notebook Lab1.ipynb
   ```

## Дополнительная информация

- В проекте включено видео `plot_lab1.mp4` в директории `amd`.
- Убедитесь, что у вас установлены необходимые библиотеки, как указано в `requirements.txt`.
