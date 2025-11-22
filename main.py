from finlab import data
import csv

def main():
    stock_count = data.get("price:收盤價")
    stock_count.to_csv("stock_counts.csv")
    

if __name__ == "__main__":
    main()
