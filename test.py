from detector import scan_sql_injection


url = "http://testphp.vulnweb.com/listproducts.php?cat=1"


# if __name__ == "__main__":
scan_sql_injection(url)
