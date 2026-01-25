# hh8-minor-project-1: Advanced Port Scanner

Short Description: Banner grabbing - service versions detection
Brief: Nmap + Python scanner exports CSV asset inventory

Tools Used:
- Nmap (brew install nmap) [web:1]
- Python 3 + python-nmap [web:15] 
- macOS Terminal

How to Run:
git clone https://github.com/Shayzad0809/hh8-minor-project-1.git
cd hh8-minor-project-1
python3 -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python src/advanced_port_scanner.py scanme.nmap.org -p 22,80 --csv results.csv

Demo Results (scanme.nmap.org):
45.33.32.156:22 open ssh OpenSSH 6.6.1p1 Ubuntu | SSH banner grabbed
45.33.32.156:80 open http Apache 2.4.7 | Apache/2.4.7 (Ubuntu)
45.33.32.156:9929 open nping-echo | Binary banner data

[+] CSV saved: results.csv (4 services)

What Learned:
- Nmap -sV version scan + banner NSE script [web:31]
- python-nmap library usage [web:15]
- CSV asset inventory export [web:32]
- GitHub project workflow

Asset Inventory: Import CSV → track services/versions/patches
Legal: scanme.nmap.org = official test target [web:34]













