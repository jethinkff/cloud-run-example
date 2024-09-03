import pandas as pd

# Data for the real estate listings
data = [
    ["251 Topsail Ct, Foster City, CA 94404", "$1,999,888", "4 bds", "2 ba", "1,900 sqft", "House for sale", "Open: Tue 10am-1pm"],
    ["259 Stilt Ct, Foster City, CA 94404", "$2,200,000", "4 bds", "2 ba", "1,760 sqft", "House for sale", "Price cut: $73,000 (Aug 12)"],
    ["823 Columba Ln, Foster City, CA 94404", "$1,480,000", "2 bds", "3 ba", "1,603 sqft", "Townhouse for sale", "Price cut: $110,000 (Aug 23)"],
    ["5204 Admiralty Ln #5204, Foster City, CA 94404", "$699,000", "2 bds", "2 ba", "998 sqft", "Condo for sale", "49 days on Zillow"],
    ["1023 Lido Ln, Foster City, CA 94404", "$1,500,000", "2 bds", "2 ba", "1,395 sqft", "Condo for sale", "14 days on Zillow"],
    ["720 Promontory Point Ln APT 2305, Foster City, CA 94404", "$1,388,000", "3 bds", "3 ba", "2,224 sqft", "Condo for sale", "11 days on Zillow"],
    ["1054 Galley Ln, Foster City, CA 94404", "$1,348,000", "3 bds", "3 ba", "1,530 sqft", "Townhouse for sale", "11 days on Zillow"],
    ["674 Portofino Ln, Foster City, CA 94404", "$1,225,000", "2 bds", "2 ba", "1,490 sqft", "Condo for sale", "Open: Tue 10am-1pm"],
    ["916 Crane Ave, Foster City, CA 94404", "$2,050,000", "4 bds", "3 ba", "2,160 sqft", "House for sale", "6 days on Zillow"],
    ["1049 Shell Blvd APT 5, Foster City, CA 94404", "$780,000", "2 bds", "2 ba", "1,042 sqft", "Condo for sale", "17 days on Zillow"],
    ["264 Bonita Ln, Foster City, CA 94404", "$1,375,000", "3 bds", "3 ba", "1,630 sqft", "Townhouse for sale", "56 days on Zillow"],
    ["118 Cityhomes Ln, Foster City, CA 94404", "$1,188,000", "2 bds", "3 ba", "1,530 sqft", "Townhouse for sale", "24 days on Zillow"],
    ["1191 Compass Ln APT 104, Foster City, CA 94404", "$1,168,000", "3 bds", "2 ba", "1,593 sqft", "Condo for sale", "Open: Sun 3-5pm"],
    ["1057 Shell Blvd APT 1, Foster City, CA 94404", "$799,000", "2 bds", "2 ba", "994 sqft", "Condo for sale", "Price cut: $26,000 (Aug 26)"],
    ["1061 Beach Park Blvd APT 216, Foster City, CA 94404", "$906,000", "2 bds", "2 ba", "1,286 sqft", "Condo for sale", "Price cut: $18,800 (Aug 13)"],
    ["7207 Admiralty Ln #7207, Foster City, CA 94404", "$749,500", "2 bds", "2 ba", "998 sqft", "Condo for sale", "26 days on Zillow"],
    ["704 Starfish Ln, Foster City, CA 94404", "$1,748,000", "4 bds", "4 ba", "2,081 sqft", "New construction", "Open: Sat 11am-4pm"],
    ["842 Juno Ln #74, Foster City, CA 94404", "$1,288,000", "3 bds", "3 ba", "1,330 sqft", "Townhouse for sale", "68 days on Zillow"],
    ["815 Sea Spray Ln APT 214, Foster City, CA 94404", "$629,000", "1 bd", "1 ba", "953 sqft", "Condo for sale", "16 days on Zillow"],
    ["811 Balboa Ln, San Mateo, CA 94404", "$1,150,000", "2 bds", "2 ba", "1,395 sqft", "Condo for sale", "Price cut: $48,000 (Aug 15)"],
    ["830 Balboa Ln, San Mateo, CA 94404", "$1,750,000", "3 bds", "3 ba", "2,140 sqft", "Condo for sale", "75 days on Zillow"],
    ["1111 Compass Ln APT 209, Foster City, CA 94404", "$725,000", "1 bd", "1 ba", "990 sqft", "Condo for sale", "Price cut: $20,000 (Aug 28)"],
    ["Laguna Vista Plan 3 Plan, Laguna Vista, SummerHill Homes", "$1,798,000+", "4 bds", "4 ba", "2,081 sqft", "New construction", "335 days on Zillow"],
    ["4214 Admiralty Ln, San Mateo, CA 94404", "$717,000", "2 bds", "2 ba", "998 sqft", "Condo for sale", "Price cut: $3,000 (Aug 29)"],
    ["1131 Compass Ln APT 217, Foster City, CA 94404", "$698,000", "1 bd", "1 ba", "878 sqft", "Condo for sale", "Open: Sun 1-4pm"],
    ["800 Sea Spray Ln APT 217, Foster City, CA 94404", "$660,000", "1 bd", "1 ba", "1,053 sqft", "Condo for sale", "Price cut: $30,000 (Aug 07)"],
    ["569 Pilgrim Dr, San Mateo, CA 94404", "$1,898,000", "4 bds", "4 ba", "2,081 sqft", "New construction", "Price cut: $50,000 (Aug 18)"],
    ["573 Pilgrim Ln, Foster City, CA 94404", "$1,948,000", "4 bds", "4 ba", "2,194 sqft", "New construction", "Open: Sat 1-4pm"],
    ["Laguna Vista Plan 4 Plan, Laguna Vista, SummerHill Homes", "", "4 bds", "4 ba", "", "New construction", ""]
]

# Create a DataFrame
columns = ["Address", "Price", "Bedrooms", "Bathrooms", "Size", "Type", "Additional Info"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
csv_file_path = "./foster_city_real_estate.csv"
df.to_csv(csv_file_path, index=False)

print(f"CSV file has been saved to: {csv_file_path}")
