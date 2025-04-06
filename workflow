name: Run Python Script
on:
  schedule:
    - cron: '*/15 * * * *'  # Runs every 15 minutes
jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run script
        run: python arbitrage.py
