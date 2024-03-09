import os
import requests
from bs4 import BeautifulSoup
import time
from pync import Notifier
import threading

# Determine the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use the determined directory to construct the path to the seen jobs file
SEEN_JOBS_FILE = os.path.join(BASE_DIR, 'seen_jobs.txt')

# URL of the university job postings webpage
URL = 'https://studentcenter.gatech.edu/campus-jobs'


def load_seen_jobs():
    """Load seen job IDs from a file into a set."""
    try:
        with open(SEEN_JOBS_FILE, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()  # Return an empty set if the file does not exist


def save_seen_job(job_id):
    """Append a new job ID to the seen jobs file."""
    with open(SEEN_JOBS_FILE, 'a') as file:
        file.write(job_id + '\n')


def fetch_job_postings(seen_jobs):
    """Fetch job postings and return new ones."""
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    labels = soup.find_all('label', string='Position Title')

    new_jobs = []
    for label in labels:
        # The job title is expected to be the next sibling of the <label> element
        job_title = label.next_sibling.strip()

        if job_title not in seen_jobs:
            new_jobs.append(job_title)
            seen_jobs.add(job_title)
            save_seen_job(job_title)  # Save the new job ID to the file

    return new_jobs

def job_checking_loop():
    while True:
        seen_jobs = load_seen_jobs()
        new_jobs = fetch_job_postings(seen_jobs)
        if new_jobs:
            print("New job postings found!")
            for job_id in new_jobs:
                Notifier.notify(f'New job posted: {job_id}', title='New Job Alert', open=URL)
        else:
            print("No new job postings found.")
            # I wanna open the file that stores the jobs when there are no new jobs
            Notifier.notify("No new jobs posted", title='Stay Tuned Alert', open=URL)

        # Wait before the next cycle (e.g., 1 day for job checking)
        time.sleep(60 * 60 * 24)

def main():
    Notifier.notify('The job tracking app is now running.', title='App Started', open=URL)
    # Start a new thread to run the job checking loop
    threading.Thread(target=job_checking_loop).start()
    while True:
        # Keep the main thread alive
        time.sleep(1)

# Run the main function if this script is executed
if __name__ == '__main__':
    main()
