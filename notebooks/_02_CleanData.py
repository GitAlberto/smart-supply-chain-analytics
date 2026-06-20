import pandas as pd

# ─────────────────────────────────────────
# 1. CHARGEMENT
# ─────────────────────────────────────────
df = pd.read_csv("../data/raw/DataCoSupplyChainDataset.csv", encoding="latin-1")
print(f"Shape initiale : {df.shape}")

# ─────────────────────────────────────────
# 2. SELECTION DES COLONNES
# ─────────────────────────────────────────
columns_to_keep = [
    'Days for shipping (real)',
    'Days for shipment (scheduled)',
    'Delivery Status',
    'Late_delivery_risk',
    'Shipping Mode',
    'order date (DateOrders)',
    'shipping date (DateOrders)',
    'Market',
    'Order Region',
    'Order Country',
    'Customer Segment',
    'Order Status',
    'Category Name',
    'Product Name',
    'Order Item Quantity',
    'Sales',
    'Benefit per order',
    'Order Profit Per Order',
    'Order Item Profit Ratio'
]

df_c = df[columns_to_keep].copy()
print(f"Shape après sélection : {df_c.shape}")

# ─────────────────────────────────────────
# 3. RENOMMAGE DES COLONNES
# ─────────────────────────────────────────
df_c = df_c.rename(columns={
    'order date (DateOrders)'       : 'order_date',
    'shipping date (DateOrders)'    : 'expedition_date',
    'Days for shipping (real)'      : 'delivery_days_real',
    'Days for shipment (scheduled)' : 'delivery_days_scheduled',
    'Delivery Status'               : 'delivery_status',
    'Late_delivery_risk'            : 'late_delivery_risk',
    'Shipping Mode'                 : 'shipping_mode',
    'Market'                        : 'market',
    'Order Region'                  : 'order_region',
    'Order Country'                 : 'order_country',
    'Customer Segment'              : 'customer_segment',
    'Order Status'                  : 'order_status',
    'Category Name'                 : 'category_name',
    'Product Name'                  : 'product_name',
    'Order Item Quantity'           : 'quantity',
    'Sales'                         : 'sales',
    'Benefit per order'             : 'benefit_per_order',
    'Order Profit Per Order'        : 'profit_per_order',
    'Order Item Profit Ratio'       : 'profit_ratio'
})

# ─────────────────────────────────────────
# 4. CONVERSION DES DATES
# ─────────────────────────────────────────
df_c['order_date']      = pd.to_datetime(df_c['order_date'])
df_c['expedition_date'] = pd.to_datetime(df_c['expedition_date'])

# ─────────────────────────────────────────
# 5. COLONNES CALCULEES
# ─────────────────────────────────────────
df_c['delivery_date_real']      = df_c['expedition_date'] + pd.to_timedelta(df_c['delivery_days_real'], unit='d')
df_c['delivery_date_scheduled'] = df_c['expedition_date'] + pd.to_timedelta(df_c['delivery_days_scheduled'], unit='d')
df_c['shipping_delay']          = df_c['delivery_days_real'] - df_c['delivery_days_scheduled']

# ─────────────────────────────────────────
# 6. EXTRACTION TEMPORELLE
# ─────────────────────────────────────────
df_c['order_year']       = df_c['order_date'].dt.year
df_c['order_month']      = df_c['order_date'].dt.month
df_c['order_month_name'] = df_c['order_date'].dt.strftime('%B')
df_c['order_quarter']    = df_c['order_date'].dt.quarter

# ─────────────────────────────────────────
# 7. SUPPRESSION DES DOUBLONS
# ─────────────────────────────────────────
df_c = df_c.drop_duplicates()
print(f"Shape après suppression doublons : {df_c.shape}")

# ─────────────────────────────────────────
# 8. CONTROLES QUALITE
# ─────────────────────────────────────────
assert df_c.isnull().sum().sum() == 0, "Valeurs manquantes détectées !"
assert df_c.duplicated().sum() == 0, "Doublons détectés !"
assert (df_c['delivery_date_real'] >= df_c['expedition_date']).all(), "Dates incohérentes !"
print("Contrôles qualité : OK !")

# ─────────────────────────────────────────
# 9. EXPORT
# ─────────────────────────────────────────
df_c.to_csv("../data/processed/supply_chain_clean.csv", index=False)
print(f"Shape finale : {df_c.shape}")
print("Export réussi → data/processed/supply_chain_clean.csv !")