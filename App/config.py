from datetime import date

CAMPUS="University of Virginia"
MOVE_DATE=date(2025, 8, 23)

OPENAI_MODEL="gpt-4.1-nano"
ORDER_LIST_OUTPUT_FILE_NAME = f"Data/output/order_list_formatted_{MOVE_DATE}.xlsx"

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/db/orders.db"
