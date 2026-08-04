# JOIN_KEY_ANALYSIS

Generated from Phase 1 header discovery across loaded workbooks.

| Candidate Key | Header Hints | Workbook Coverage | Worksheet Coverage | Confidence % | Locations |
| --- | --- | --- | --- | --- | --- |
| NDC | NDC, NDC code, NDC Code | 7 | 7 | 70.0 | 07-30_inv.xlsx::Sheet1, Awards.xlsx::Sheet1, CIP.xlsx::Sheet1, Headers.xlsx::Sheet1, Mat_Desc,_MOQ_,_Material_#.xlsx::Sheet1, Strend.xlsx::Sheet1, sales_summ.xlsx::Sheet1 |
| Customer | Customer, Sold-to party Name, PH_SOLDTO_NAME | 7 | 7 | 70.0 | Awards.xlsx::Sheet1, Buying_groups.xlsx::Sheet1, Headers.xlsx::Sheet1, Open_Order_Summary.xlsx::Sheet1, Strend.xlsx::Sheet1, raw_OB.xlsx::Sheet1, sales_summ.xlsx::Sheet1 |
| Sold-to Party | Sold-to party, Sold to party, PH_SOLDTO_NAME | 5 | 5 | 50.0 | Awards.xlsx::Sheet1, Headers.xlsx::Sheet1, Open_Order_Summary.xlsx::Sheet1, raw_OB.xlsx::Sheet1, sales_summ.xlsx::Sheet1 |
| Lookup | Lookup, x | 4 | 4 | 40.0 | Awards.xlsx::Sheet1, Open_Order_Summary.xlsx::Sheet1, Strend.xlsx::Sheet1, sales_summ.xlsx::Sheet1 |
| Sales Order | Sales Order No., SO#, Sales Order Qty | 4 | 4 | 40.0 | Headers.xlsx::Sheet1, Open_Order_Summary.xlsx::Sheet1, raw_OB.xlsx::Sheet1, sales_summ.xlsx::Sheet1 |
| Material Number | HANA Material, Matl._x000d_
Code, Material Number | 2 | 2 | 20.0 | Mat_Desc,_MOQ_,_Material_#.xlsx::Sheet1, sales_summ.xlsx::Sheet1 |
| SKU | SKU | 2 | 2 | 20.0 | 07-30_inv.xlsx::Sheet1, Open_Order_Summary.xlsx::Sheet1 |