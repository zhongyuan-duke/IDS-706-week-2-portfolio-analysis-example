### This project will:

- Use a dev container, Makefile, and GitHub Actions
- Load historical stock prices, calculate daily returns, compute portfolio statistics: mean return, volatility, Sharpe ratio, visualize portfolio performance
- Include unit tests

### Project structure:
```
portfolio-analysis-example/
├── portfolio.py
├── test_portfolio.py
├── portfolio_oop.py (object oriented programming)
├── portfolio_risk_analysis.ipynb (more pandas examples)
├── requirements.txt
├── Makefile
├── .devcontainer/
│   └── devcontainer.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
```

#### create a requirements.txt file with:
```txt
pandas
numpy
matplotlib
yfinance
pytest
flake8
seaborn
jupyter
scipy
```

### Add VS Code Dev Containers (recommended)

A **development container** is a running container with a well-defined tool/runtime stack and its prerequisites. You can try out development containers with **[GitHub Codespaces](https://github.com/features/codespaces)** or **[Visual Studio Code Dev Containers](https://aka.ms/vscode-remote/containers)**.

#### VS Code Dev Containers
Option 1: Use the Dev Containers extension in VS Code to create a dev container. Open a sample in a container by pressing shift+command+P, then select `Dev Containers: Add Development Container Configuration Files...`. Choose the Python template, and it will create the necessary files for you.

Option 2: Manually create the dev container files. In the project root, create a .devcontainer directory and inside it, create a .devcontainer/devcontainer.json file.

#### GitHub Codespaces
Follow these steps:
1. Select your branch.
2. Click the **Code** drop-down menu.
3. Click on the **Codespaces** tab, and create.

For more information on creating your codespace, visit the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/developing-online-with-codespaces/creating-a-codespace#creating-a-codespace).

#### Rebuild or update your container
after you make changes to your container, such as installing a packages, you'll rebuild your container for your changes to take effect. by pressing shift+command+P, then select `Dev Containers: Rebuild Container` or `Codespaces: Rebuild Container` command so the modifications are picked up.  


### create a Makefile with:
```makefile
install:
    pip install -r requirements.txt 
format:
    black *.py
lint:
    flake8 --ignore=E501,N8,C portfolio.py
test:
    pytest
``` 

Run the following commands to install dependencies in the Dev Container:
```bash
make install
```


#### create portfolio.py. This script loads stock data, calculates returns, and computes portfolio stats.

#### create test_portfolio.py – Unit Tests

Run the following commands to format code, lint, and run tests:
```bash
make format
make lint
make test
```

## Commit and push your changes
```bash
git add .
git commit -m "updated XY branch"   
git push
``` 
 
### Enable GitHub Actions
Option 1: 
Go to your repository on GitHub.
Click on the "Actions" tab.
Click on "New workflow".
Select "Set up a workflow yourself".
Replace the content with the following YAML configuration.

Option 2: in the project root, create a .github/workflows directory and inside it,
create a .github/workflows/main.yml file 

### Object-Oriented Programming (OOP) vs Procedural Example

Below is a simple example to illustrate the difference between procedural programming and object-oriented programming (OOP) using a rectangle's area calculation:

**Procedural:**
```python
def area(length, width):
	return length * width

print(area(5, 3))
```

**OOP:**
```python
class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())
```