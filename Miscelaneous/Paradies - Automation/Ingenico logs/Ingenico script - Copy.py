file = open("Logs.txt")
text = file.read()
file.seek(0)
file.close()
total_txn = text.count("Chip card inserted")
total_failures = text.count("(damaged/invalid card)")
percentage = (total_failures / total_txn) * 100

if percentage < 10:
    if total_failures == 1:
        print(f"Out of a total of {str(total_txn)} transactions, there was only 1 line where the chip reader detected a damaged/invalid card.")
    elif total_failures == 0:
        print(f"There is a total of {str(total_txn)} successful transactions. No errors were found.")
        print("There is no need for escalation.")
    else:
        print(f"Out of a total of {str(total_txn)} transactions, there were only {str(total_failures)} lines where the chip reader detected a damaged/invalid card.")
elif percentage > 10 and percentage < 30:
	print(f"Out of a total of {str(total_txn)} transactions, there were {str(total_failures)} where the chip reader detected a damaged/invalid card.")
	print("However, the failure percentage is not that high. The chip reader may be dirty.")
else:
    print(f"Out of a total of {str(total_txn)} transactions, there were {str(total_failures)} where the chip reader detected a damaged/invalid card.")
    print("The failure percentage is high, and the chip reader may be damaged. The device would need to be replaced.")

print(f"\nFailure percentage: {percentage:1.2f}%")

if total_txn < 12:
	print(f"\nOnly {str(total_txn)} transactions were evaluated. You may want to test with more transactions as the total percentage may be misleading.")

input()