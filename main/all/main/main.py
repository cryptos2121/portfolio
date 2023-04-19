# main.py

# from aws_utils import check_message
from portfolio_utils import read_portfolio_file

def main():
    portfolio, header, rows = read_portfolio_file("https://raw.githubusercontent.com/mytestlab123/lambda/main/arbitrum.csv")
    print("portfolio ==>", portfolio)
    print("header ==>", header)
    print("rows ==>", rows)


if __name__ == "__main__":
    main()