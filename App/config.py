CAMPUS="University of Virginia"
IS_DROPOFF_SEASON = True

OPENAI_MODEL="gpt-4.1-nano"
SQLALCHEMY_DATABASE_URL="sqlite:///./data/db/orders.db"

PDF_ORIENTATION = 2 # landscape
PDF_LEFT_MARGIN = 0.25
PDF_RIGHT_MARGIN = 0.25
PDF_TOP_MARGIN = 0.3
PDF_BOTTOM_MARGIN = 0.3
PDF_TITLE_SIZE = 20

ORDER_LIST_HEADERS_WIDTHS = {
    "Order ID": 8,
    "Name": 23,
    "Phone": 13,
    "Location": 30, # text wrap
    "Items Ct": 8,
    "Items": 30, # text wrap
    "Comments": 35, # text wrap
    "Pronunciation": 21,
    "Time Loaded": 13,
    "Time Delivered": 13,
}
ORDER_LIST_HEADERS_WRAPPED = ["Location", "Items", "Comments"]
ORDER_LIST_FOOTERS = [
    ["Automatically generated"]
]