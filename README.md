# Campus Job Finder

## Overview
Campus Job Finder is a Python application designed to help students and staff at educational institutions stay informed about new job postings on their campus job boards. It automates the process of checking for new postings and notifies users through macOS notifications.

## Features
- **Automated Monitoring**: Scans specified campus job boards for new postings at regular intervals.
- **Real-time Notifications**: Alerts users via macOS notifications when new job opportunities are detected.
- **Background Operation**: Runs unobtrusively in the background, ensuring minimal distraction and resource usage.

## Getting Started

### Prerequisites
- Python 3.x
- pip for installing dependencies

### Installation
1. Clone the repository:
`git clone https://github.com/yebyyy/Campus-Job-Finder.git`
2. Navigate to the project directory:
`cd Campus-Job-Finder`
3. Install required dependencies:
`pip install -r requirements.txt`

### Usage
Run the application:
The application will start monitoring the job board URL specified in the script and notify you of new postings.

## Customization
Modify `main.py` to change the job board URL and the frequency of checks:
- Change `URL` to your campus job board.
- Adjust `CHECK_INTERVAL` for how often the application checks for new jobs (default is every 3 days).

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or add new features.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
