# 🏦 ISO 27001:2022 & BDDK Banking Sector Information Security Risk Assessment Engine

[![ISO 27001](https://img.shields.io/badge/Standard-ISO%2FIEC%2027001%3A2022-blue.svg)](https://www.iso.org/standard/27001)
[![BDDK Compliant](https://img.shields.io/badge/Compliance-BDDK%20Banking%20Regs-green.svg)](https://www.bddk.org.tr/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-brightgreen.svg)](https://www.python.org/)

An automated Governance, Risk, and Compliance (GRC) assessment framework designed for the banking and financial services sector, compliant with **ISO/IEC 27001:2022**, **ISO 27005**, and **BDDK Regulations**.

---

## 🏗️ Architecture & Workflow

```text
[ Asset Inventory (JSON) ] ──┐
                             ├──> [ Risk Engine (Python) ] ──> [ Risk Register & Report (MD) ]
[ Threat Database (JSON) ] ──┘                                        │
                                                                       ▼
                                                          [ ISO Annex A & BDDK Mapping ]