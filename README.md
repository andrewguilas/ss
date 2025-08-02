# SS

This is a command-line interface where you can upload customer data (as a `.csv`) and interact with it.

## TODO

### Stage 1 - CLI App (due 8/3)

- [x] Generate order list as .csv
- [x] Format spreadsheet with .xlsx
- [x] Output .xslx as .pdf
- [x] Store orders in SQL
- [x] Set truck & driver of customer (add truck & driver property)
- [x] Add Truck model with truck_id, truck_number, truck_driver
- [ ] Add truck & route commands
- [ ] Add route order
- [ ] Create tests
- [ ] Merge existing customer spreadsheet to add customers' specific items

### Stage 2 - Discord App (due 8/6)

- [ ] Add typechecking
- [ ] Make app into a Discord bot
- [ ] Run app remotely on Heroku
- [ ] Store data with an online db

### Stage 3 - Extras (no deadline)

- [ ] Add customers' photos
- [ ] Add an easy way to bulk message customers with Google Voice or something else

## To Build

1. `Create .env` with the following secrets:
```
OPENAI_API_KEY=...
```

2. Download libraries with `pip install -r requirements.txt`

3. Set up database with `py setup.py`

4. Upload `order_list.csv` in `data\input\`

## To Run

1. Run the app with `py main.py ...`

## API Reference

### app/order_list

`upload_order_list(csv_file_name)`

`generate_order_list(pdf_file_name, date)`

`print_order_list(date, truck_number)`
