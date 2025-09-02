# AMD Project Setup

This guide will help you set up and run the AMD project without using Poetry.

## Prerequisites

- Python 3.8 or higher
- pip

## Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:gshjis/AMD_BSUIR.git
   cd AMD_BSUIR
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Run the process.py script**

   ```bash
   python process.py
   ```

2. **View the Jupyter Notebook**

   Navigate to the `amd` directory and open `Lab1.ipynb` with Jupyter Notebook.

   ```bash
   cd amd
   jupyter notebook Lab1.ipynb
   ```

## Additional Information

- The project includes a video `plot_lab1.mp4` in the `amd` directory.
- Ensure you have the required libraries installed as specified in `requirements.txt`.
