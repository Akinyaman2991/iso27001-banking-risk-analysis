from risk_calculator import BankingRiskCalculator
from tabulate import tabulate
import json

def generate_markdown_report():
    calculator = BankingRiskCalculator("data/banking_assets.json", "data/threats_vulnerabilities.json")
    risks = calculator.calculate_risks()

    table_data = []
    for r in risks:
        table_data.append([
            r["risk_id"],
            r["asset_name"],
            r["threat_name"],
            r["risk_score"],
            r["risk_level"],
            r["iso_control"],
            r["bddk_clause"]
        ])

    headers = ["Risk ID", "Asset Name", "Threat Vector", "Score", "Level", "ISO 27001:2022", "BDDK Clause"]
    markdown_table = tabulate(table_data, headers=headers, tablefmt="github")

    report_content = f"""# 🏦 Executive Information Security Risk Assessment Report

## 1. Overview
This report presents the quantitative risk evaluation for critical banking assets based on **ISO/IEC 27001:2022** standards and **BDDK Information Systems Regulations**.

## 2. Calculated Risk Register

{markdown_table}

---
*Report generated automatically by Banking Risk Engine.*
"""

    with open("docs/Risk_Assessment_Report.md", "w", encoding="utf-8") as f:
        f.write(report_content)

    print("[+] Report generated successfully at: docs/Risk_Assessment_Report.md")

if __name__ == "__main__":
    generate_markdown_report()