"""Customer churn exploratory analysis using Pandas and Matplotlib."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
DATA = BASE / 'data' / 'customer_churn.csv'
CHARTS = BASE / 'charts'
CHARTS.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    required = {'customer_id', 'tenure_months', 'monthly_charges', 'contract_type', 'payment_method', 'internet_service', 'support_tickets', 'churn'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f'Missing required columns: {sorted(missing)}')
    df = df.drop_duplicates(subset='customer_id').copy()
    df['monthly_charges'] = pd.to_numeric(df['monthly_charges'], errors='coerce')
    df['tenure_months'] = pd.to_numeric(df['tenure_months'], errors='coerce')
    df['support_tickets'] = pd.to_numeric(df['support_tickets'], errors='coerce')
    df['churn'] = df['churn'].astype(str).str.strip().str.lower().map({'yes':1,'no':0})
    df = df.dropna(subset=['churn','monthly_charges','tenure_months','contract_type'])
    df['churn'] = df['churn'].astype(int)
    print(f'Customers analyzed: {len(df):,}')
    print(f'Overall churn rate: {df.churn.mean():.1%}')
    print(f'Avg monthly charges (churned): ${df.loc[df.churn==1, "monthly_charges"].mean():.2f}')
    print(f'Avg monthly charges (retained): ${df.loc[df.churn==0, "monthly_charges"].mean():.2f}')

    def save_bar(series, title, ylabel, filename):
        fig, ax = plt.subplots(figsize=(9,5))
        series.plot(kind='bar', ax=ax, color='#2A75A9')
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xlabel('')
        ax.set_ylim(0, max(5, float(series.max())*1.2))
        ax.tick_params(axis='x', rotation=20)
        for i, value in enumerate(series.values):
            ax.text(i, value + max(1,float(series.max())*.02), f'{value:.1f}%', ha='center')
        fig.tight_layout()
        fig.savefig(CHARTS / filename, dpi=160)
        plt.close(fig)

    counts = df['churn'].value_counts().reindex([0,1], fill_value=0)
    fig, ax = plt.subplots(figsize=(7,5))
    ax.bar(['Retained','Churned'], counts.values, color=['#2A75A9','#E07A5F'])
    ax.set_title('Customer Retention vs Churn')
    ax.set_ylabel('Number of customers')
    fig.tight_layout(); fig.savefig(CHARTS/'01_churn_distribution.png',dpi=160); plt.close(fig)

    by_contract = (df.groupby('contract_type')['churn'].mean()*100).sort_values(ascending=False)
    save_bar(by_contract, 'Churn Rate by Contract Type', 'Churn rate (%)', '02_contract_churn.png')
    by_payment = (df.groupby('payment_method')['churn'].mean()*100).sort_values(ascending=False)
    save_bar(by_payment, 'Churn Rate by Payment Method', 'Churn rate (%)', '03_payment_churn.png')
    df['tenure_group'] = pd.cut(df['tenure_months'], bins=[-1,12,24,48,1000], labels=['0–12 months','13–24 months','25–48 months','49+ months'])
    by_tenure = df.groupby('tenure_group', observed=True)['churn'].mean()*100
    save_bar(by_tenure, 'Churn Rate by Customer Tenure', 'Churn rate (%)', '04_tenure_churn.png')
    df['ticket_group'] = pd.cut(df['support_tickets'], bins=[-1,0,2,1000], labels=['0','1–2','3+'])
    by_tickets = df.groupby('ticket_group', observed=True)['churn'].mean()*100
    save_bar(by_tickets, 'Churn Rate by Support Tickets', 'Churn rate (%)', '05_support_churn.png')

    summary = pd.DataFrame({'segment': ['Overall'] + ['Contract: '+x for x in by_contract.index] + ['Payment: '+x for x in by_payment.index] + ['Tenure: '+str(x) for x in by_tenure.index] + ['Support tickets: '+str(x) for x in by_tickets.index], 'churn_rate_pct': [df.churn.mean()*100] + by_contract.tolist() + by_payment.tolist() + by_tenure.tolist() + by_tickets.tolist()})
    summary.to_csv(BASE/'churn_summary.csv',index=False)
    print('\nChurn by contract:\n', by_contract.round(1).to_string())
    print('\nCreated five charts in charts/ and churn_summary.csv')

if __name__ == '__main__':
    main()
