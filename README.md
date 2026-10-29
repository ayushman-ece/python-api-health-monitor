# 📡 Python API Health Monitor

A Python command-line monitoring tool that checks whether websites and HTTP API endpoints are responding, measures response time, records HTTP status codes, and stores monitoring results in a CSV report.

This project is part of my Python project portfolio and my long-term journey toward Data Science, Machine Learning, and AI.

---

## 🚀 Project Overview

Websites and APIs can experience downtime, slow responses, connection errors, or unexpected HTTP status codes.

The Python API Health Monitor helps check endpoint availability and maintain a local history of monitoring results.

### Application Workflow

```text
Enter Website or API URL
          ↓
Validate URL
          ↓
Send HTTP Request
          ↓
Measure Response Time
          ↓
Capture HTTP Status
          ↓
Classify Result
          ↓
Display Monitoring Report
          ↓
Save Result to CSV
          ↓
View Recent Reports
```

---

## 🎯 Objective

The main objective is to build a modular monitoring utility while learning HTTP requests, response handling, timing measurements, CSV storage, and exception handling.

The project demonstrates:

- URL validation
- HTTP request handling
- Response-time measurement
- HTTP status-code inspection
- Connection and timeout error handling
- CSV report generation
- Persistent monitoring history
- Modular Python programming

---

## ✨ Features

- 🌐 Check websites and HTTP API endpoints
- 🔗 Automatically add HTTPS when a URL has no scheme
- ⏱️ Measure response time in milliseconds
- 📊 Display HTTP status codes
- 🟢 Identify successful HTTP responses
- 🔴 Report HTTP errors and connection failures
- 🧾 Save results to a CSV file
- 📋 View the ten most recent reports
- 🛡️ Apply a request timeout to avoid waiting indefinitely
- 🧩 Separate monitoring logic from the CLI

---

## 🧠 How It Works

### 1. URL Validation

The application checks that the supplied URL has a valid HTTP or HTTPS scheme and a network location.

### 2. HTTP Request

The project uses Python's `requests` library to send a GET request.

The request follows redirects and uses a 10-second timeout.

### 3. Response-Time Measurement

The application uses `time.perf_counter()` to measure elapsed time around the request.

The result is converted into milliseconds.

### 4. Result Classification

The application classifies results as follows:

| Result | Meaning |
|---|---|
| `UP` | HTTP response status indicates success, typically 2xx |
| `HTTP_ERROR` | An HTTP response was received, but its status indicates failure |
| `DOWN` | A request exception occurred, such as a connection or timeout error |

An HTTP error does not necessarily mean that the server is offline. For example, an endpoint can respond with `404 Not Found` while the server itself is reachable.

### 5. CSV Reporting

Each check is appended to `health_report.csv`.

The report includes:

- `checked_at` — UTC timestamp
- `url` — Requested URL
- `status_code` — HTTP response status, if available
- `response_ms` — Elapsed request time in milliseconds
- `result` — Monitoring classification
- `error` — Request exception details, if any

---

## 🗂️ Project Structure

```text
python-api-health-monitor/
│
├── main.py
├── health_monitor.py
├── requirements.txt
├── .gitignore
└── README.md
```

### `main.py`

Responsible for:

- Displaying the CLI menu
- Accepting the endpoint URL
- Displaying monitoring results
- Showing recent reports
- Handling user interaction

### `health_monitor.py`

Contains the monitoring logic:

- URL validation
- HTTP requests
- Response-time calculation
- Result classification
- CSV report storage
- Retrieval of recent reports

### `requirements.txt`

Defines the external dependency required by the project.

### `.gitignore`

Excludes generated reports, Python cache files, virtual environments, and local environment files from Git.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/python-api-health-monitor.git
```

### 2. Enter the project directory

```bash
cd python-api-health-monitor
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start the application:

```bash
python main.py
```

Available options:

```text
1. Check a URL
2. View recent reports
3. Exit
```

Select an option and follow the terminal prompts.

---

## 💻 Example

Example input:

```text
Enter website/API URL: https://www.python.org
```

Illustrative result:

```text
URL: https://www.python.org
Result: UP
HTTP status: 200
Response time: 185.42 ms
Report saved.
```

Actual status codes and response times depend on the endpoint and network conditions.

---

## 📦 Requirements

- Python 3.10 or newer recommended
- `requests` 2.32.x or a compatible release below version 3
- Internet access to reach external endpoints

Install the dependency with:

```bash
python -m pip install -r requirements.txt
```

---

## 🧰 Technologies Used

- **Python** — Application logic
- **Requests** — HTTP communication
- **Pathlib** — File path handling
- **CSV** — Monitoring report storage
- **Time** — Response-time measurement
- **Datetime** — UTC timestamps
- **URL parsing** — URL validation
- **Command-Line Interface** — User interaction

---

## 📚 What I Learned

Through this project, I practiced:

1. Structuring a modular Python application
2. Validating user-supplied URLs
3. Sending HTTP GET requests
4. Understanding HTTP status codes
5. Handling network exceptions and timeouts
6. Measuring elapsed time
7. Writing structured data to CSV
8. Reading saved monitoring history
9. Using virtual environments and dependency files
10. Keeping generated reports out of Git
11. Separating business logic from the CLI

---

## ⚠️ Limitations

This project is a local learning tool, not a production monitoring platform.

- It checks endpoints only when the user requests a check.
- It does not perform continuous or scheduled monitoring.
- It does not send alerts or notifications.
- It does not calculate uptime percentages or service-level agreements.
- A successful HTTP response does not guarantee that every application feature works.
- A failed request may result from DNS, TLS, firewall, network, or server problems.
- The CSV report can grow over time and currently has no rotation mechanism.

Only check endpoints you are authorized to access. Do not use this tool to send excessive requests to a service.

---

## 🔮 Future Improvements

Possible improvements include:

- Add continuous monitoring at configurable intervals
- Monitor multiple endpoints in one run
- Calculate uptime percentages
- Add average and percentile response-time statistics
- Generate charts from monitoring history
- Send alerts through email or Telegram
- Export summary reports
- Add retry policies and exponential backoff
- Add automated unit tests
- Build a Streamlit monitoring dashboard
- Package the tool for easier installation

---

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [https://github.com/ayushman-ece](https://github.com/ayushman-ece)

---

## 🛣️ Learning Journey

This project is part of my ongoing practical programming portfolio.

```text
Python Fundamentals
        ↓
Modular Applications
        ↓
File Handling and Data Storage
        ↓
HTTP APIs and Networking
        ↓
Automation and Monitoring
        ↓
Data Analysis
        ↓
Machine Learning
        ↓
LLMs, RAG and Agentic AI
```

My goal is to keep building progressively stronger projects while understanding the concepts behind them.

**Building practical skills, one project at a time. 🚀**