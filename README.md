# customer_segmentation

Dataset info:

InvoiceNo: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation

StockCode: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.

Description: Product (item) name. Nominal.

Quantity: The quantities of each product (item) per transaction. Numeric.

InvoiceDate: Invoice Date and time. Numeric, the day and time when each transaction was generated.

UnitPrice: Unit price. Numeric, Product price per unit in sterling.

CustomerID: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.

Country: Country name. Nominal, the name of the country where each customer resides.

Cluster mapping

0: Occasional customers

1: Lost Customers

2: Champions

3: Potential Loyalists

4: Top Customers

api usage:
1. Install uvicorn
2. uvicorn api.main:app --reload
3. http://127.0.0.1:8000/docs
4. Write RFM values
5. You get the prediction cluster + name