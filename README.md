# 🏦 ISO 27001:2022 & BDDK Banking Information Security Risk Assessment Engine

[![ISO 27001](https://img.shields.io/badge/Standard-ISO%2FIEC%2027001%3A2022-blue.svg)](https://www.iso.org/standard/27001)
[![ISO 27005](https://img.shields.io/badge/Standard-ISO%2FIEC%2027005%3A2022-blue.svg)](https://www.iso.org/standard/75288.html)
[![BDDK Compliant](https://img.shields.io/badge/Compliance-BRSA%2FBDDK%20Regulation-green.svg)](https://www.bddk.org.tr/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)

This project is an **automated information security risk analysis, threat modeling, and regulatory audit engine** designed specifically for banking and financial infrastructures (Core Banking, SWIFT, Mobile/Internet Banking, ATM Networks).

The system performs quantitative and qualitative risk calculations by combining requirements from **ISO/IEC 27001:2022 (Annex-A Controls)**, **ISO 27005 Risk Management Standard**, and the **BRSA (BDDK) Regulation on Information Systems and Electronic Banking Services**, generating executive-ready GRC reports.

---

## 🎯 Purpose and Target Audience

In financial institutions, information security risk assessment processes are often managed through complex spreadsheets, leading to version control issues, human errors, and loss of audit trails. This automation engine provides:
- **ISMS & GRC Specialists:** Enables managing the risk inventory as code (**Risk-as-Code**).
- **Internal Auditors & Examiners:** Simplifies fast traceability and evidence creation during BRSA (BDDK) and ISO 27001 audits.
- **CISO & Executive Management:** Accelerates decision-making with automatically generated summary reports.

---

## ✨ Key Features

- 📌 **Advanced Asset Inventory Management:** Confidentiality, Integrity, and Availability (CIA) valuation tailored to banking data categories (Personal Data, Customer Secrets, Financial Data).
- 🔗 **Dual Regulatory Mapping (Cross-Mapping):** Simultaneous mapping of each identified vulnerability to both ISO 27001:2022 control clauses (e.g., *A.8.8 Management of Technical Vulnerabilities*) and relevant BRSA (BDDK) regulatory articles (e.g., *BRSA Article 14 - Penetration Testing and Vulnerability Management*).
- 📐 **Flexible Risk Calculation Formula:** Metric model based on asset value, threat likelihood, and vulnerability impact rating.
- 📝 **Automated Documentation Generation:** Converts calculated risk matrices, action plans, and statistics directly into GitHub-Flavored Markdown and HTML formats.
- 🔍 **Filtering and Action Prioritization:** Automatic CISO alerting mechanism and SLA definitions for critical and high-level risks.

---

## 📐 Risk Assessment Methodology

Risk scores are calculated using a **1-5 Likert Scale** (ranging from 1 to 125 points):

$$\text{Risk Score (R)} = \text{Asset Value (AV)} \times \text{Threat Likelihood (T)} \times \text{Vulnerability Impact (V)}$$

### Risk Levels and Response Matrix

| Score Range | Risk Level | Description / Action Required | Response SLA |
| :--- | :--- | :--- | :--- |
| **81 - 125** | 🔴 **CRITICAL** | Direct threat to system stability or regulatory compliance. Immediate CISO escalation required. | **24 Hours - 7 Days** |
| **46 - 80** | 🟠 **HIGH** | Vulnerabilities with high impact potential. Implement additional security controls. | **30 Days** |
| **16 - 45** | 🟡 **MEDIUM** | Control deficiencies or secondary system risks. Include in upcoming sprint planning. | **90 Days** |
| **1 - 15** | 🟢 **LOW** | Acceptable risk level. Routine monitoring is sufficient. | **180 Days / Annual Review** |

---

## 🏗️ System Architecture and Data Flow

```text
  ┌─────────────────────────────────────────────────────────┐
  │                      DATA SOURCES                       │
  │  ┌───────────────────────────┐ ┌─────────────────────┐ │
  │  │   banking_assets.json     │ │threats_vulnerabilities│ │
  │  │ (Asset / CIA Valuation)   │ │   .json (Threats)   │ │
  │  └─────────────┬─────────────┘ └──────────┬──────────┘ │
  └────────────────┼──────────────────────────┼────────────┘
                   │                          │
                   ▼                          ▼
  ┌─────────────────────────────────────────────────────────┐
  │                    CALCULATION ENGINE                   │
  │            scripts/risk_calculator.py                   │
  │  - Risk Score Calculation (CIA x T x V)                 │
  │  - ISO 27001:2022 Annex-A Control Mapping               │
  │  - BRSA (BDDK) Clause Mapping                           │
  └────────────────────────┬────────────────────────────────┘
                           │
                           ▼
  ┌─────────────────────────────────────────────────────────┐
  │                    REPORT GENERATOR                     │
  │            scripts/report_generator.py                  │
  │  - Markdown & HTML Format Conversion                    │
  │  - Action Plan & SLA Definition                         │
  └────────────────────────┬────────────────────────────────┘
                           │
                           ▼
  ┌─────────────────────────────────────────────────────────┐
  │                     OUTPUT DOCUMENT                     │
  │            docs/Risk_Assessment_Report.md               │
  └─────────────────────────────────────────────────────────┘
