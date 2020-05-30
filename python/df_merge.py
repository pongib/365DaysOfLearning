# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on='branch_id')

# Print merge_by_id
print(merge_by_id)


# Merge revenue & managers on 'city' & 'branch': combined
# suffix for change columns name.
combined = pd.merge(revenue, managers, left_on='city', right_on='branch', suffixes=['_revenue', '_managers'])

revenue['change'] = revenue['state']

revenue = revenue.drop(columns='state')

# can be multi column
combined = pd.merge(revenue, managers, left_on=['city', 'change'], right_on=['branch', 'state'])

# Print combined
print(combined)


# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on=['branch_id', 'city', 'state'])

# Print combined
print(combined)