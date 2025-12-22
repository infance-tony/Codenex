from mlxtend.datasets import load_online_retail
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Load the Online Retail dataset from UCI (via mlxtend)
df = load_online_retail()

# Preprocess the data: group by InvoiceNo to create baskets
basket = df.groupby('InvoiceNo')['Description'].apply(list).reset_index()

# Encode the transactions
te = TransactionEncoder()
te_ary = te.fit(basket['Description']).transform(basket['Description'])
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display the top rules
print(rules.head())