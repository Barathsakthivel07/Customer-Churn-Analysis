# Customer Churn Analysis — Business Insights Report

## 1. Executive Summary

This project analyzes a synthetic telecom customer dataset containing 1,000 customer records using Python, Pandas, and Matplotlib.

The analysis identified an overall customer churn rate of **28.9%**, meaning 289 customers left the company while 711 customers remained.

The main objective was to identify customer groups associated with higher churn rates and recommend strategies that could improve retention.

## 2. Key Findings

### Finding 1: Contract Type Influences Churn Patterns

- Month-to-month contracts: 37.5% churn
- One-year contracts: 16.2% churn
- Two-year contracts: 19.8% churn

**Insight:** Customers using month-to-month contracts have higher churn rates than customers on longer-term contracts.

**Recommendation:** Test incentives for switching to annual contracts, such as discounts or additional benefits, while monitoring profitability and customer satisfaction.

### Finding 2: New Customers Have Higher Churn

- 0–12 months: 40.0%
- 13–24 months: 30.2%
- 25–48 months: 29.7%
- 49+ months: 23.4%

**Insight:** Customers within their first year have the highest churn rate, suggesting an opportunity to strengthen early customer engagement.

**Recommendation:** Introduce onboarding assistance, service check-ins, and personalized support during the first 12 months.

### Finding 3: Support Issues Are Associated With Customer Churn

- No support tickets: 19.8% churn
- 1–2 support tickets: 29.1% churn
- 3+ support tickets: 43.3% churn

**Insight:** Customers with more support tickets tend to have higher churn rates.

**Recommendation:** Identify customers with repeated complaints, review recurring service issues, and prioritize follow-up actions.

### Finding 4: Payment Methods Show Different Churn Rates

- Mailed check: 32.6%
- Electronic check: 32.4%

**Insight:** These payment groups show churn rates above the overall average of 28.9%.

**Recommendation:** Investigate billing difficulties and payment experiences before proposing changes to payment options.

## 3. Recommended Business Actions

**Priority 1 — Improve early customer retention**

Create an onboarding and customer engagement program for customers in their first year.

**Priority 2 — Address recurring support issues**

Flag customers with three or more support tickets and investigate unresolved problems.

**Priority 3 — Evaluate contract incentives**

Test offers that encourage interested month-to-month customers to consider longer-term plans.

**Priority 4 — Improve payment experiences**

Collect customer feedback and investigate friction in billing and payment processes.

## 4. KPIs to Monitor

- Overall customer churn rate
- Churn rate by contract type
- Churn rate by customer tenure
- Churn rate by support ticket frequency
- Customer retention rate
- Customer support resolution time

## 5. Limitations

This project uses synthetic customer data. Its findings demonstrate data analysis techniques but should not be interpreted as measured results from a real telecom company.

The relationships identified are descriptive associations, not evidence of causation. The proposed retention strategies should be validated using customer research and controlled experiments.

## 6. Conclusion

The analysis identified higher churn rates among newer customers, month-to-month subscribers, and customers with repeated support interactions.

These findings provide a starting point for customer retention strategies focused on onboarding, customer service, and contract experience.

Future work could include customer-level risk segmentation, cohort analysis, predictive modeling, and experiments to measure the impact of retention initiatives.