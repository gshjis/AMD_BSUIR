# Настройка проекта AMD

Этот гайд поможет вам настроить и запустить лабораторные работы

## Предварительные условия

- Python 3.12 или выше
- pip
- Jupyter Notebook

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

Исследование разложения функции в ряд Тейлора. Включает аналитическое вычисление производных и визуализацию приближения.
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

Векторно-матричный подход к разложению функции в ряд Тейлора второго и третьего порядка. Работа с многомерными массивами.
</details>

<details>
<summary>Лабораторная работа 3</summary>

**Расположение файла:** amd/Lab3.ipynb  
**Метод запуска:**  
```bash
cd amd
jupyter notebook Lab3.ipynb
```

Исследование тензорных операций:
- Тензорное транспонирование
- Тензорное умножение с параметрами λ и μ
- Создание единичных тензоров
</details>

## Дополнительная информация

- Убедитесь, что у вас установлены все зависимости из `requirements.txt`
- Для визуализации результатов требуется библиотека matplotlib
- Видео результатов доступны в папке amd
