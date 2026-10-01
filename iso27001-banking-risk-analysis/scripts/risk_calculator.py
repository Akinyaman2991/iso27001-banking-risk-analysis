import json
from pathlib import Path
from typing import List, Dict

class BankingRiskCalculator:
    def __init__(self, asset_file: str, threat_file: str):
        self.asset_path = Path(asset_file)
        self.threat_path = Path(threat_file)
        self.assets = self._load_json(self.asset_path)
        self.threats = self._load_json(self.threat_path)

    def _load_json(self, path: Path) -> Dict:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def calculate_risks(self) -> List[Dict]:
        risk_register = []

        for asset in self.assets:
            category = asset["category"]
            category_threats = self.threats.get(category, [])

            for threat in category_threats:
                av = asset["asset_value"]
                t = threat["threat_score"]
                v = threat["vulnerability_score"]

                # Likert 1-5 çarpımı (Max Score: 125)
                risk_score = round(av * t * v, 2)

                if risk_score >= 81:
                    level = "CRITICAL"
                    action = "Immediate Control Implementation & CISO/Board Escalation"
                elif risk_score >= 46:
                    level = "HIGH"
                    action = "Apply Security Remediation within 30 Days"
                elif risk_score >= 16:
                    level = "MEDIUM"
                    action = "Include in Next Sprint Backlog"
                else:
                    level = "LOW"
                    action = "Routine Monitoring / Accept Risk"

                risk_register.append({
                    "risk_id": f"RSK-{asset['asset_id']}-{threat['id']}",
                    "asset_name": asset["asset_name"],
                    "threat_name": threat["name"],
                    "risk_score": risk_score,
                    "risk_level": level,
                    "recommended_action": action,
                    "iso_control": threat["iso_control"],
                    "bddk_clause": threat["bddk_clause"]
                })

        return risk_register

if __name__ == "__main__":
    calculator = BankingRiskCalculator("data/banking_assets.json", "data/threats_vulnerabilities.json")
    results = calculator.calculate_risks()
    print(f"[+] Risk Calculation Complete. Generated {len(results)} Risk Records.")