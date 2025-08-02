# SS

This is a command-line interface where you can upload customer data (as a `.csv`) and interact with it.

## TODO
- [x] Generate order list as .csv
- [x] Format spreadsheet with .xlsx
- [x] Output .xslx as .pdf
- [x] Store orders in SQL
- [x] Set truck & driver of customer (add truck & driver property)
- [ ] Add Truck model with truck_id, truck_number, truck_driver
- [ ] Reorder customers according to a set driving route (add order property)
- [ ] Merge existing customer spreadsheet to add customers' specific items
- [ ] Make app into a Discord bot
- [ ] Run app remotely on Heroku
- [ ] Add customers' photos
- [ ] Store data with an online db
- [ ] Add an easy way to bulk message customers with Google Voice or something else

## API

### app/order_list

`upload_order_list(csv_file_name)`

`generate_order_list(pdf_file_name, date)`
