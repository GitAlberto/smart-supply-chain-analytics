===============================================================
Data dictionary - French
===============================================================

| Champ | Description |
|---|---|
| Type | Type de transaction effectuée |
| Days for shipping (real) | Jours réels de livraison du produit |
| Days for shipment (scheduled) | Jours de livraison prévus |
| Benefit per order | Bénéfice par commande |
| Sales per customer | Ventes totales par client |
| Delivery Status | Statut de livraison : En avance, En retard, Annulée, Dans les délais |
| Late_delivery_risk | Retard probable : 1 = oui, 0 = non |
| Category Id | Code catégorie produit |
| Category Name | Nom de la catégorie produit |
| Customer City | Ville d'achat du client |
| Customer Country | Pays d'achat du client |
| Customer Email | Email du client |
| Customer Fname | Prénom du client |
| Customer Id | Identifiant client |
| Customer Lname | Nom du client |
| Customer Password | Mot de passe masqué |
| Customer Segment | Segment client : Particulier, Entreprise, Bureau à domicile |
| Customer State | État du magasin d'achat |
| Customer Street | Rue du magasin d'achat |
| Customer Zipcode | Code postal client |
| Department Id | Code du département magasin |
| Department Name | Nom du département magasin |
| Latitude | Latitude du magasin |
| Longitude | Longitude du magasin |
| Market | Marché de livraison : Afrique, Europe, LATAM, Asie-Pacifique, USCA |
| Order City | Ville de destination de la commande |
| Order Country | Pays de destination de la commande |
| Order Customer Id | Code commande client |
| order date (DateOrders) | Date de la commande |
| Order Id | Identifiant de la commande |
| Order Item Cardprod Id | Code produit (lecteur RFID) |
| Order Item Discount | Valeur de la remise |
| Order Item Discount Rate | Taux de remise |
| Order Item Id | Identifiant de l'article |
| Order Item Product Price | Prix sans remise |
| Order Item Profit Ratio | Ratio de profit par article |
| Order Item Quantity | Nombre de produits par commande |
| Sales | Chiffre d'affaires |
| Order Item Total | Montant total par commande |
| Order Profit Per Order | Profit par commande |
| Order Region | Région de livraison mondiale |
| Order State | État de la région de livraison |
| Order Status | Statut : Complète, En attente, Fermée, Paiement en attente, Annulée, En traitement, Fraude suspectée, En attente, Révision paiement |
| Product Card Id | Code produit |
| Product Category Id | Code catégorie produit |
| Product Description | Description du produit |
| Product Image | Lien image produit |
| Product Name | Nom du produit |
| Product Price | Prix du produit |
| Product Status | Stock : 1 = indisponible, 0 = disponible |
| Shipping date (DateOrders) | Date et heure exacte d'expédition |
| Shipping Mode | Mode d'expédition : Classe Standard, Première Classe, Deuxième Classe, Même Jour |








====================================================
Data dictionary - English
====================================================
FIELDS,DESCRIPTION
Type,:  Type of transaction made
Days for shipping (real)     ,:  Actual shipping days of the purchased product
Days for shipment (scheduled),:  Days of scheduled delivery of the purchased product
Benefit per order,:  Earnings per order placed
Sales per customer,:  Total sales per customer made per customer
Delivery Status,":  Delivery status of orders: Advance shipping , Late delivery , Shipping canceled , Shipping on time"
Late_delivery_risk           ,":  Categorical variable that indicates if sending is late (1), it is not late (0)."
Category Id,:  Product category code
Category Name,:  Description of the product category
Customer City,:  City where the customer made the purchase
Customer Country,:  Country where the customer made the purchase
Customer Email,:  Customer's email
Customer Fname,:  Customer name
Customer Id,:  Customer ID
Customer Lname,:  Customer lastname
Customer Password,:  Masked customer key
Customer Segment,":  Types of Customers: Consumer , Corporate , Home Office"
Customer State,:  State to which the store where the purchase is registered belongs
Customer Street,:  Street to which the store where the purchase is registered belongs
Customer Zipcode,:  Customer Zipcode
Department Id,:  Department code of store
Department Name,:  Department name of store
Latitude,:  Latitude corresponding to location of store
Longitude,:  Longitude corresponding to location of store
Market,":  Market to where the order is delivered : Africa , Europe , LATAM , Pacific Asia , USCA"
Order City,:  Destination city of the order
Order Country,:  Destination country of the order
Order Customer Id,:  Customer order code
order date (DateOrders),:  Date on which the order is made
Order Id,:  Order code
Order Item Cardprod Id,:  Product code generated through the RFID reader
Order Item Discount,:  Order item discount value
Order Item Discount Rate     ,:  Order item discount percentage
Order Item Id,:  Order item code
Order Item Product Price     ,:  Price of products without discount
Order Item Profit Ratio,:  Order Item Profit Ratio
Order Item Quantity,:  Number of products per order
Sales,:  Value in sales
Order Item Total  ,:  Total amount per order
Order Profit Per Order,:  Order Profit Per Order
Order Region,":  Region of the world where the order is delivered :  Southeast Asia ,South Asia ,Oceania ,Eastern Asia, West Asia , West of USA , US Center , West Africa, Central Africa ,North Africa ,Western Europe ,Northern , Caribbean , South America ,East Africa ,Southern Europe , East of USA ,Canada ,Southern Africa , Central Asia ,  Europe , Central America, Eastern Europe , South of  USA "
Order State,:  State of the region where the order is delivered
Order Status,":  Order Status : COMPLETE , PENDING , CLOSED , PENDING_PAYMENT ,CANCELED , PROCESSING ,SUSPECTED_FRAUD ,ON_HOLD ,PAYMENT_REVIEW"
Product Card Id,:  Product code
Product Category Id,:  Product category code
Product Description,:  Product Description
Product Image,:  Link of visit and purchase of the product
Product Name,:  Product Name
Product Price,:  Product Price
Product Status,":  Status of the product stock :If it is 1 not available , 0 the product is available "
Shipping date (DateOrders)   ,:  Exact date and time of shipment
Shipping Mode,":  The following shipping modes are presented : Standard Class , First Class , Second Class , Same Day"
