from utils.extract import scrape_main
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_gsheet
from utils.load import save_to_postgresql

if __name__ == "__main__":
    df_raw = scrape_main()
    df_clean = clean_data(df_raw)
    
    if not df_clean.empty:
        save_to_csv(df_clean)
        save_to_gsheet(df_clean)
        save_to_postgresql(df_clean, db_url="postgresql://etl_user:admin@localhost:5432/etl_pemda")
    else:
        print("[WARN] No data to save.")