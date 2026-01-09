#!/usr/bin/env python3
"""
Advanced Port Scanner with Banner Grabbing
hh8-minor-project-1: Identifies service versions on open ports
Tools: Nmap, Python
"""

import argparse
import nmap
import csv
import json
from datetime import datetime

def scan_target(target, ports):
    """Run Nmap scan with version detection + banner grabbing"""
    nm = nmap.PortScanner()
    scan_args = "-sV --script=banner --host-timeout 30s"
    
    print(f"[+] Scanning {target}:{ports}...")
    nm.scan(target, ports, arguments=scan_args)
    
    print(f"[DEBUG] Hosts found: {nm.all_hosts()}")
    
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports_open = nm[host][proto].keys()
            for port in sorted(ports_open):
                service = nm[host][proto][port]
                
                scripts = service.get('script', {})
                banner = next(iter(scripts.values()), '') if scripts else ''
                
                results.append({
                    'host': host,
                    'port': port,
                    'state': service.get('state', ''),
                    'service': service.get('name', ''),
                    'product': service.get('product', ''),
                    'version': service.get('version', ''),
                    'extrainfo': service.get('extrainfo', ''),
                    'banner': banner[:100]
                })
    return results

def print_results(results):
    """Print formatted table"""
    print("\n" + "="*90)
    print("SCAN RESULTS - Banner Grabbing Complete (sorted by port)")
    print("="*90)
    for r in results:
        print(f"{r['host']}:{r['port']:5d} {r['state']:7} "
              f"{r['service']:12} {r['product']:20} {r['version']} | {r['banner']}")

def save_csv(results, filename):
    """Export asset inventory as CSV"""
    if not results:
        print(f"[!] No scan results to save")
        return
    
    fieldnames = ['host','port','state','service','product','version','extrainfo','banner']
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"[+] Asset inventory saved: {filename} ({len(results)} services)")

def main():
    parser = argparse.ArgumentParser(description="Advanced port scanner - hh8 internship project")
    parser.add_argument("target", help="Target (scanme.nmap.org)")
    parser.add_argument("-p", "--ports", default="22,80,443,9929", help="Ports to scan")
    parser.add_argument("--csv", help="Save CSV export")
    args = parser.parse_args()
    
    results = scan_target(args.target, args.ports)
    print_results(results)
    
    if args.csv:
        save_csv(results, args.csv)

if __name__ == "__main__":
    main()

