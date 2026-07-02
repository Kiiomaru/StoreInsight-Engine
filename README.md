# 📊 StoreInsight Engine

> **Automated Sales Reporting & Performance Monitoring System built with Python**

StoreInsight Engine is a Python automation project designed to transform raw sales data into actionable business insights. The application processes sales records, calculates key performance indicators (KPIs), generates store-specific reports, creates daily and annual rankings, automatically organizes backup files, and delivers personalized HTML reports via email to managers and executives.

The project was developed with a modular architecture, following separation of responsibilities to improve readability, maintainability, and scalability.

---

## 🚀 Features

- 📥 Load data from Excel and CSV files
- 📊 Calculate sales KPIs automatically
- 🏪 Generate reports for each store
- 📈 Create daily and annual sales rankings
- 📂 Automatically organize backup folders and spreadsheets
- 📧 Send personalized HTML emails with performance indicators
- 🎯 Compare results against predefined business goals
- 🟢 Visual performance indicators (goal achieved/not achieved)
- 🧩 Modular and maintainable architecture

---

# Workflow

The automation follows the pipeline below.

<p align="center">
  <img src="https://raw.githubusercontent.com/Kiiomaru/StoreInsight-Engine/refs/heads/main/images/fluxo.png" width="45%">
</p>

1. Load sales, stores and managers data.
2. Merge datasets.
3. Separate sales by store.
4. Calculate KPIs.
5. Generate reports.
6. Create ranking spreadsheets.
7. Save backups automatically.
8. Send personalized emails to each manager.
9. Send executive ranking report to the board.

---

# Project Architecture

The project is organized into independent modules, each responsible for a specific part of the business logic.

<p align="center">
  <img src="https://raw.githubusercontent.com/Kiiomaru/StoreInsight-Engine/refs/heads/main/images/arquitetura.png" width="45%">
</p>

```text
StoreInsight-Engine/

├── app.py
├── .gitignore
├── README.md
├── Backup Arquivos Loja/
├── Base de Dados/
├── images/
├── services/
│   ├── email_service.py
│   ├── backup.py
│   ├── data_loader.py
│   ├── utils.py
├── indicators/
│   ├── indicators.py
├── templates/
│   ├── email_template.html
```

---

# Technologies

- Python
- Pandas
- Jinja2
- SMTP
- pathlib
- dotenv
- Excel
- CSV

---

# Project Structure

| Module | Responsibility |
|---------|----------------|
| **app.py** | Main application flow |
| **data_loader.py** | Reads Excel and CSV files |
| **indicators.py** | Calculates business metrics |
| **backup.py** | Generates spreadsheets and backup folders |
| **email_service.py** | Creates and sends HTML emails |
| **utils.py** | Utility functions |
| **email_template.html** | HTML email template |

---

# Business Indicators

The system automatically calculates:

- Daily Revenue
- Annual Revenue
- Daily Product Diversity
- Annual Product Diversity
- Daily Average Ticket
- Annual Average Ticket

Each indicator is compared against predefined business goals.

---

# Automated Email Report

Each store manager receives an individualized HTML report containing:

- Daily KPIs
- Annual KPIs
- Goal comparison
- Visual indicators (green/red)
- Store spreadsheet attached automatically



---

# Daily Ranking

The application automatically generates a spreadsheet containing the ranking of all stores for the selected day.

<p align="center">
  <img src="https://github.com/Kiiomaru/StoreInsight-Engine/blob/main/images/relatorio_dia.png" width="45%">
</p>

---

# Annual Ranking

The system also generates the annual performance ranking.

<p align="center">
  <img src="https://github.com/Kiiomaru/StoreInsight-Engine/blob/main/images/relatorio_ano.png" width="45%">
</p>

---

# Automatic Backup System

For every execution, StoreInsight Engine creates organized backup folders and exports the generated spreadsheets automatically.

<p align="center">
  <img src="https://github.com/Kiiomaru/StoreInsight-Engine/blob/main/images/pastas.png" widht="45%">
</p>

---

# Application Execution

During execution the application:

- Loads datasets
- Processes all stores
- Calculates KPIs
- Generates spreadsheets
- Sends emails
- Generates executive rankings

<p align="center">
  <img src="https://github.com/Kiiomaru/StoreInsight-Engine/blob/main/images/terminal.png" widht="45%">
</p>

---

# Main Business Flow

```text
Sales Data
      │
      ▼
Data Loading
      │
      ▼
Store Separation
      │
      ▼
KPI Calculation
      │
      ▼
Report Generation
      │
      ▼
Backup Generation
      │
      ▼
HTML Email Creation
      │
      ▼
Automatic Email Delivery
```

---

# Future Improvements

- Dashboard with Streamlit
- Database integration
- Scheduling with APScheduler
- Docker support
- Logging system
- Unit tests with Pytest
- CI/CD with GitHub Actions
- Configuration through YAML
- Interactive KPI dashboard

---

# Skills Demonstrated

- Python Automation
- Data Analysis
- Business Intelligence
- Pandas
- Data Processing
- Email Automation
- HTML Templates (Jinja2)
- File System Automation
- Modular Software Architecture
- Business Metrics
- Clean Code
- Separation of Concerns

---

# Author

**Matheus Giuliano**

Python Automation • Data Analysis • Process Automation • Business Intelligence

If you enjoyed this project, consider leaving a ⭐ on the repository.
