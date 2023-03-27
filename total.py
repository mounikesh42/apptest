# with open('overall.txt', 'r') as f1, open('Today.txt', 'r') as f2, open('yes.txt', 'w') as f3:
#     # Read the contents of the files
#     yesterday_items = set(line.strip() for line in f1)
#     today_items = set(line.strip() for line in f2)
#     # Find the items that are present in yesterday.txt and remove them from today.txt
#     excluded_items = today_items - yesterday_items
#     # Write the excluded items to yes.txt
#     f3.write('\n'.join(excluded_items))



# Open the files
with open('yes.txt', 'r') as f1, open('latest.txt', 'r') as f2, open('untouched.txt', 'w') as f3:
    # Read the contents of the files
    yes_items = set(line.strip() for line in f1)
    latest_items = set(line.strip() for line in f2)
    # Find the items that are present in latest.txt but not in yes.txt
    untouched_items = latest_items - yes_items
    # Write the untouched items to untouched.txt
    f3.write('\n'.join(untouched_items))
